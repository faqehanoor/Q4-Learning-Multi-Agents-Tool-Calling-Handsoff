🌿 Agentic Assistant with Gemini API
This project is an AI-powered multi-agent assistant built using Python, supporting tools and handoffs between agents. It utilizes Google’s Gemini API to respond to user queries about real-time information like location, breaking news, and educational topics like photosynthesis.

🚀 Features
✅ Multi-agent system with tool usage and handoffs

🌍 Retrieves current location

📰 Displays breaking news

🌱 Explains photosynthesis through a specialized agent

📦 Uses Gemini 2.0 Flash model for fast and reliable responses

🎨 Rich command-line interface output with rich

🧠 Powered By
Gemini API (Google AI)

agents framework (supports tools, runners, agents)

rich library for beautiful terminal UI

📁 File Structure

├── main.py             # Entry point of the assistant
├── agents/             # Custom agent framework/tools (assumed)
├── .env                # Contains API keys (GEMINI_API_KEY)
├── README.md           # Project documentation
🛠️ Requirements
Python 3.8+

Dependencies:

python-dotenv

rich

Your custom agents library

httpx or similar (used in AsyncOpenAI client)

🔐 Environment Variables
Create a .env file in your project root and add:

GEMINI_API_KEY=your_gemini_api_key_here

🧪 Usage
Run the agent system using:

uv run main.py
It will output:

Your current location

The latest breaking news

An explanation of photosynthesis

🧩 Example Output

Agent Execution Result
Handled by: main_agent



New Items:
- Your Current Location is Karachi, Pakistan!
- 📰 Monsoon Rains Hit Karachi Again ...

Final Output:
1. Your Current Location is Karachi, Pakistan!
2. 📰 Monsoon Rains Hit Karachi Again ...
3. Photosynthesis is the process by which green plants...
   
🤝 Contributing
Feel free to fork and contribute by adding new tools or agents!

📄 License
This project is for educational/demo purposes. Adapt and extend freely.

![WhatsApp Image 2025-07-27 at 00 24 07_0d51ecb5](https://github.com/user-attachments/assets/8204d318-4dd7-48ba-adfa-611be71e8db4)

![WhatsApp Image 2025-07-27 at 00 24 29_039c3feb](https://github.com/user-attachments/assets/6e73a2fd-dd98-499c-b214-64188b8290dc)

