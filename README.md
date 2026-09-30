# Student Database AI Backend

AI-powered Student Database Management System built with FastAPI, Gemini, LangGraph and ChromaDB.

## Features

- Student CRUD operations
- FastAPI REST APIs
- Interactive Swagger API documentation
- Gemini API integration
- AI chatbot for student database interaction
- LangGraph-based AI workflow
- ChromaDB vector database integration
- Modular backend architecture

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Google Gemini API
- LangChain
- LangGraph
- ChromaDB
- Docker

  ## Project Structure

```text
student-database-ai-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── services.py
│   ├── ai_tools.py
│   ├── graph.py
│   ├── vector_store.py
│   ├── routes_students.py
│   └── routes_chatbot.py
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── render.yaml
├── requirements.txt
└── seed.py
```


## Installation

Clone the repository:

git clone https://github.com/Anupam27patel/student-database-ai-backend.git

cd student-database-ai-backend

## Environment Variables

Create a `.env` file based on `.env.example`.

Add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

## Run the Application

Install dependencies:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn app.main:app --reload

## API Documentation

Once the server is running, open Swagger UI:

http://127.0.0.1:8000/docs

## AI Chatbot

The project includes an AI chatbot powered by Gemini and LangGraph.

The chatbot is designed to interact with the student database through backend tools.

## Docker

Build the Docker image:

docker build -t student-database-ai-backend .

Run the container:

docker run -p 8000:8000 student-database-ai-backend

## Deployment

The project includes a `render.yaml` configuration for deployment on Render.

## Future Improvements

- Authentication and authorization
- PostgreSQL production database
- Automated testing
- CI/CD pipeline
- Improved AI agent capabilities
- Production monitoring and security

## Disclaimer

This project is intended for learning and demonstration purposes.
Do not use real student personal information without appropriate authentication, authorization, privacy, and security controls.

## Author

**Anupam Patel**

B.Tech CSE Student
