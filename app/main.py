from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import uvicorn

app = FastAPI()

# In-memory data store
books_db = {}

# Pydantic models
class Book(BaseModel):
    title: str
    author: str
    published_year: int = Field(..., gt=0, lt=9999)

class BookResponse(Book):
    id: int

# Utility function to find the next ID
def get_next_id():
    return max(books_db.keys(), default=0) + 1

# Endpoints
@app.post("/books", response_model=BookResponse)
def add_book(book: Book):
    book_id = get_next_id()
    books_db[book_id] = book.dict()
    return {**books_db[book_id], "id": book_id}

@app.get("/books", response_model=List[BookResponse])
def get_books():
    return [{"id": book_id, **book_data} for book_id, book_data in 
books_db.items()]

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": book_id, **books_db[book_id]}

@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: Book):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[book_id] = book.dict()
    return {"id": book_id, **books_db[book_id]}

@app.delete("/books/{book_id}", response_model=BookResponse)
def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    book_data = books_db.pop(book_id)
    return {"id": book_id, **book_data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

