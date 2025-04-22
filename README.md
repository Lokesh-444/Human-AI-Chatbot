🤖 Human-AI Chatbot (Django + OpenAI)
A conversational AI chatbot web application built with Django and integrated with OpenAI's language model. This project simulates human-like interactions and supports file-based image generation using AI.

🚀 Features
💬 Chat with AI in a natural, real-time interface

🧠 OpenAI GPT API integration for intelligent, contextual responses

📂 Upload image files and receive AI-generated content

🖥️ Web-based interface with Django templating

🧪 Simple admin and backend management via Django admin

🛠️ Tech Stack
Backend: Python, Django

AI Integration: OpenAI API (chat completions + image generation)

Frontend: HTML, CSS (Django templates)

Database: SQLite (default)

Others: Django Forms, Django Views, Django ORM

📁 Project Structure
bash
Copy
Edit
Human-AI-Chatbot/
├── HumanChatbot/            # Django project root
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chatbot/                 # Django app
│   ├── templates/chatbot/   # HTML templates
│   ├── static/              # Static files (if any)
│   ├── aifunctions.py       # OpenAI-related functions
│   ├── forms.py             # Django form definitions
│   ├── models.py            # Database models
│   ├── views.py             # Request handlers
│   ├── urls.py              # App-specific routes
│   └── admin.py
├── uploads/                 # Uploaded files
├── db.sqlite3               # Default database
└── manage.py
🧑‍💻 Getting Started
Prerequisites
Python 3.x

pip

OpenAI API key

Setup Instructions
Clone the repository

bash
Copy
Edit
git clone https://github.com/Lokesh-444/Human-AI-Chatbot.git
cd Human-AI-Chatbot
Create and activate virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables

Create a .env file and add your OpenAI API key:

env
Copy
Edit
OPENAI_API_KEY=your_openai_key
Run migrations and start the server

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

✨ Example Use Cases
Simulate customer support interactions

Prototype conversational agents for projects

Experiment with file-to-image AI generation features

🤝 Contributions
Want to improve this project? Feel free to fork, submit pull requests, or create issues.

