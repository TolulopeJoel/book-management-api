from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_book():
    response = client.post("/books", json={"title": "Test Book", "author": 
"Author", "published_year": 2023})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_book():
    response = client.post("/books", json={"title": "Another Book", 
"author": "Author", "published_year": 2023})
    book_id = response.json()["id"]
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Another Book"

def test_update_book():
    response = client.post("/books", json={"title": "Update Book", 
"author": "Author", "published_year": 2023})
    book_id = response.json()["id"]
    response = client.put(f"/books/{book_id}", json={"title": "Updated 
Book", "author": "New Author", "published_year": 2024})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Book"

def test_delete_book():
    response = client.post("/books", json={"title": "Delete Book", 
"author": "Author", "published_year": 2023})
    book_id = response.json()["id"]
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Delete Book"

