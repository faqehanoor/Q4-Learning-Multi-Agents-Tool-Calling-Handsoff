from dotenv import load_dotenv
import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, function_tool
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

load_dotenv()

console = Console()

@function_tool
def current_location():
    return "Your Current Location is Karachi, Pakistan!"

@function_tool
def breaking_news():
    return """📰 Monsoon Rains Hit Karachi Again
            Heavy monsoon showers have resumed in Karachi, causing urban flooding in several areas. The Pakistan Meteorological Department (PMD) has issued a warning for more rain over the weekend. Residents are advised to avoid unnecessary travel and stay updated through official advisories."""


async def main():
    MODEL_NAME = "gemini-2.0-flash"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    external_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model=MODEL_NAME,
        openai_client=external_client
    )

    config = RunConfig(
        model=model,
        model_provider=external_client
    )

    agent = Agent(
        name="plant_agent",
        instructions="You are a helpful assistant that can give a helpful and friendly concise explanation about photosynthesis.",
        model=model
    )

    main_agent = Agent(
        name="main_agent",
        instructions="You are a helpful assistant that can answer questions about various topics, including your current location, breaking news, and photosynthesis.",
        tools=[current_location, breaking_news],
        handoffs=[agent],
        model=model
    )

    result = await Runner.run(
        main_agent,
        """
        1. What is my current location?
        2. What is the latest breaking news?
        3. What is photosynthesis?
        """,
        run_config=config
    )

    console.rule("[bold blue]Agent Execution Result")
    console.print(Panel.fit(f"[bold green]Handled by:[/bold green] {result.last_agent.name}"))

    console.print("\n[bold yellow]New Items:[/bold yellow]")
    for item in result.new_items:
        console.print(f"- {item}")

    console.print("\n[bold magenta]Final Output:[/bold magenta]")
    console.print(Panel.fit(Markdown(result.final_output)))

if __name__ == "__main__":
    asyncio.run(main())
