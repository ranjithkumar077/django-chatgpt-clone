# Django ChatGPT Clone

A simple Django chat interface that sends prompts to an AI model and displays responses in a clean conversational UI.

## Features

- Django-based backend and routing
- Simple responsive chat interface
- Supports OpenAI or OpenRouter style API keys
- Local configuration with `.env.local`

## Project Structure

```text
CHATGPT/
|-- ChatGPT/
|   |-- templates/
|   |   `-- index.html
|   |-- settings.py
|   |-- urls.py
|   `-- views.py
|-- .env.local.example
|-- db.sqlite3
|-- manage.py
`-- README.md
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install django openai
```

3. Create a local config file named `.env.local` in the project root.
4. Add one of these:

```env
OPENAI_API_KEY=your_openai_key
```

or

```env
OPENROUTER_API_KEY=your_openrouter_key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o-mini
```

5. Run the server:

```bash
python manage.py runserver
```

6. Open `http://127.0.0.1:8000/`

## Notes

- `.env.local` should not be committed.
- The included UI is meant to be lightweight and easy to customize.
