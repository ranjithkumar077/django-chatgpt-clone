# Django ChatGPT Clone

A clean and modern AI chat web app built with Django, featuring a responsive interface and support for OpenAI or OpenRouter-based models.

## Overview

This project is a lightweight chat application where users can type prompts into a polished web interface and receive AI-generated responses in real time. It was designed to be simple to run, easy to understand, and flexible enough for future customization.

## Highlights

- Django-powered backend
- Attractive responsive chat interface
- Real-time prompt and response flow
- Supports both OpenAI and OpenRouter API keys
- Local secret configuration using `.env.local`
- Easy starting point for learning Django + AI integration

## Interface

The app includes:

- A modern split-layout landing screen
- Styled user and assistant message bubbles
- Enter-to-send behavior
- Friendly status messages while requests are processing
- Mobile-friendly responsive layout

## Tech Stack

- Python
- Django
- OpenAI Python SDK
- HTML, CSS, and JavaScript

## Project Structure

```text
CHATGPT/
|-- ChatGPT/
|   |-- templates/
|   |   `-- index.html
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   `-- wsgi.py
|-- .env.local.example
|-- .gitignore
|-- manage.py
`-- README.md
```

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install django openai
```

3. Create a local config file named `.env.local` in the project root.

4. If you are using OpenAI, add:

```env
OPENAI_API_KEY=your_openai_key
```

5. If you are using OpenRouter, add:

```env
OPENROUTER_API_KEY=your_openrouter_key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o-mini
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Why This Project

This project is useful for:

- Practicing Django fundamentals
- Understanding API integration in web apps
- Building a personal AI assistant interface
- Creating a base for future AI-powered projects

## Security Note

- Do not commit `.env.local`
- Keep your API keys private
- Use environment-based configuration for production deployments

## Author

Made by **Ranjith Kumar**

GitHub: [ranjithkumar077](https://github.com/ranjithkumar077)

## Future Improvements

- Conversation history storage
- User authentication
- Multiple model selection
- Better loading and error states
- Dark mode and theme switching

## License

This project is open for learning, customization, and personal development use.
