from fastapi import FastAPI
from app.api import books, reviews

app = FastAPI(title="Book Review Service")

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(reviews.router, prefix="/books", tags=["Reviews"])
