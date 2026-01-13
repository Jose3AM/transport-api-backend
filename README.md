# Transport API Backend

Backend API developed with **FastAPI** to expose basic information about urban transport routes and alerts.

This project is the foundation of a platform focused on providing **updated and reliable** public transport information, designed to scale with real data sources and intelligent services such as chatbots.

## Technologies

- Python  
- FastAPI  
- Uvicorn  

## Installation and Execution

1. Create and activate a virtual environment

bash
python -m venv transport-api-env
source transport-api-env/bin/activate  # Linux / Mac
transport-api-env\Scripts\activate     # Windows

2. Install dependencies

pip install -r requirements.txt

3. Run the server

uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Health Check
GET /health

Verifies that the API is running correctly.

{
  "status": "ok"
}

What the API Does:
-Provides structured information about transport routes
-Exposes alerts related to specific routes
-Returns consistent and predictable JSON responses
-Designed with validation and QA-first principles

Available Endpoints
-GET /health
  Checks API status
-GET /routes
  Returns a list of available transport routes
-GET /alerts
  Returns a list of alerts associated with transport routes

Example Response
GET /routes
[
  {
    "id": 1,
    "name": "Route Downtown - North",
    "status": "active"
  },
  {
    "id": 2,
    "name": "Route South - Downtown",
    "status": "suspended"
  }
]

API Documentation

FastAPI automatically generates interactive API documentation:
-Swagger UI: /docs
-ReDoc: /redoc

Project Status

This project is under active development and will evolve to include:
-Real data sources
-Database integration
-Automated testing
-AI-powered chatbot services

- The API includes explicit error handling, returning meaningful HTTP status codes such as 404 when a requested resource does not exist.
