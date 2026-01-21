# Transport API Backend

Backend API developed with **FastAPI** that provides structured and
validated information about urban transport routes.

This project is designed as the foundation of a scalable transport
information platform, focused on **clean architecture, API quality, and
testability**, with future extensions such as real-time data sources and
intelligent services.

------------------------------------------------------------------------

## Technologies

-   Python
-   FastAPI
-   Uvicorn
-   SQLAlchemy
-   SQLite
-   Pytest

------------------------------------------------------------------------

## Project Architecture

The project follows a layered architecture:

-   **routers/** → HTTP endpoints and request handling\
-   **services/** → business logic\
-   **repositories/** → database access layer\
-   **models.py** → database models (SQLAlchemy)\
-   **schemas.py** → response and validation schemas (Pydantic)\
-   **errors.py** → centralized error messages\
-   **database.py** → database configuration and session management

This separation improves **maintainability, scalability, and
testability**.

------------------------------------------------------------------------

## Installation and Execution

1.  Create and activate a virtual environment:

``` bash
python -m venv transport-api-env
source transport-api-env/bin/activate   # Linux / Mac
transport-api-env\Scripts\activate    # Windows
```

2.  Install dependencies:

``` bash
pip install -r requirements.txt
```

3.  Run the server:

``` bash
uvicorn app.main:app --reload
```

The API will be available at:

    http://127.0.0.1:8000

------------------------------------------------------------------------

## Health Check

**GET /health**

Verifies that the API is running correctly.

``` json
{
  "status": "ok"
}
```

------------------------------------------------------------------------

## Available Endpoints

-   **GET /health**\
    Checks API status

-   **GET /routes**\
    Returns a list of available transport routes

-   **GET /routes/{id}**\
    Returns a specific route by ID

    -   `404` if the route does not exist

-   **GET /routes?status=active\|suspended**\
    Filters routes by status

    -   `422` if the status value is invalid

-   **GET /alerts**\
    Alerts endpoint prepared for future database integration

------------------------------------------------------------------------

## Example Response

**GET /routes**

``` json
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
```

------------------------------------------------------------------------

## Error Handling

The API uses explicit and consistent error handling:

-   `404 Not Found` → Resource does not exist\
-   `422 Unprocessable Entity` → Invalid input or query parameters

Error responses are returned as structured JSON objects.

------------------------------------------------------------------------

## API Documentation

FastAPI automatically generates interactive documentation:

-   Swagger UI: `/docs`\
-   ReDoc: `/redoc`

------------------------------------------------------------------------

## Project Status

This project is under active development.

Planned next steps: - Alerts database integration\
- Authentication\
- Extended test coverage\
- Data ingestion from external sources
