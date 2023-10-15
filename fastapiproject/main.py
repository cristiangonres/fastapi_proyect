from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    title : str
    author : str
    description : Optional[str] = None
    price : float
    pages : int
    published : bool

@app.get("/")
def index():
    return {"message":"Hola Pythonianos"}

@app.get("/books/{id}")
def get_book(id : int):
    return {"data": {id}}

@app.post("/books")
def create_book(book : Book):
    return {"message": f"libro {book.title} insertado correctamente"}