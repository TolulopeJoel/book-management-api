# Simple Book Management API

This is a simple Book Management API built with FastAPI. The API supports 
basic CRUD operations for managing a collection of books.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## Setup

1. Clone the repository:

```sh
git clone https://github.com/yourusername/book_management_api.git
cd book_management_api
```

2. Install the dependencies:

```sh
pip install -r requirements.txt
```

3. Run the application:

```sh
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

- `POST /books`: Add a new book.
- `GET /books`: Retrieve a list of all books.
- `GET /books/{book_id}`: Retrieve details of a specific book by its ID.
- `PUT /books/{book_id}`: Update the details of a specific book by its ID.
- `DELETE /books/{book_id}`: Delete a specific book by its ID.

## Running Tests

To run the tests, use the following command:

```sh
pytest
```

## Documentation

The API documentation is automatically generated and available at `/docs` 
or `/redoc`.
