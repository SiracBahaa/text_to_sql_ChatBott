# Company Database Chatbot

This project introduces a conversational bot that translates natural language inputs into SQL queries, executes these queries, and returns the results as natural language responses. It allows users to interact with a database seamlessly through everyday language. The AI models generate SQL queries and interpret query results, utilizing structured output techniques to format responses, which makes it easier for users to understand complex data insights. Although the system currently supports data modification operations like INSERT, UPDATE, and DELETE, it does not yet implement robust security measures for these actions. Future versions could incorporate guardrails to ensure safer handling of database modifications. The project uses 2 AI models:
- Gemini 1.5 Flash for SQL query generation
- Gemini 2.0 Flash for natural language response generation

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install requirements: `pip install -r requirements.txt`
5. Create a `.env` file and add your GEMINI_API_KEY and DB_PATH.
6. Run the chatbot via Gradio Interface: `python app.py`
