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
-   **security.py** → API key authentication and authorization\
-   **errors.py** → centralized error messages\
-   **database.py** → database configuration and session management

This architecture improves maintainability, scalability, testability,
and security.

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

## Authentication

Most endpoints are protected using an API Key.

The API key must be sent using the header:

-   `X-API-Key: super-secret-key`

Authentication behavior:

-   `401 Unauthorized` → Missing API key\
-   `403 Forbidden` → Invalid API key

The **/health** endpoint is public and does not require authentication.

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
    Public health check

-   **GET /routes**\
    Returns a paginated list of transport routes
    -   Pagination: limit, offset
    -   Filtering: status=active | suspended
    -   Requires API Key

-   **GET /routes/{id}**\
    Returns a specific route by ID

    -   `404` if the route does not exist
    -   Requires API Key

-   **GET /routes?status=active\|suspended**\
    Filters routes by status

    -   `422` if the status value is invalid

-   **GET /alerts**\
    Endpoint prepared for future database integration
    -   Requires API Key

------------------------------------------------------------------------

## Pagination Response Format

**GET /routes**

``` json
{
  "total": 25,
  "limit": 10,
  "offset": 0,
  "data": [
    {
      "id": 1,
      "name": "Route Downtown - North",
      "status": "active"
    }
  ]
}
```

------------------------------------------------------------------------

## Error Handling

The API uses global error handling with predictable JSON responses:

-   `404 Not Found` → Resource does not exist\
-   `422 Unprocessable Entity` → Invalid input or query parameters\
-   `401 Unauthorized` → Missing API key\
-   `403 Forbidden` → Invalid API key

------------------------------------------------------------------------

## Testing

Automated tests with Pytest cover:

-   Routes behavior and validation\
-   Pagination and filtering\
-   Security (API key enforcement)\
-   Health endpoint isolation

All tests are passing and aligned with the API contract.

------------------------------------------------------------------------

## API Documentation

FastAPI provides interactive documentation:

-   Swagger UI: `/docs`\
-   ReDoc: `/redoc`

------------------------------------------------------------------------

## Project Status

Core backend features are complete:

-   Database-backed routes\
-   Clean layered architecture\
-   API key security\
-   Pagination and filtering\
-   Global error handling\
-   High test coverage

Next planned steps:

-   Alerts database integration\
-   API versioning\
-   Extended metadata and analytics\
-   External data ingestion