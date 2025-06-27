from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.book import Book
from app.schemas.book import BookCreate, BookOut
from app.services.cache import get_cached_books, set_cached_books

router = APIRouter()

@router.get("/", response_model=list[BookOut])
def list_books(db: Session = Depends(get_db)):
    cached = get_cached_books()
    if cached:
        return cached
    books = db.query(Book).all()
    result = [BookOut.from_orm(b) for b in books]
    set_cached_books([b.dict() for b in result])
    return result

@router.post("/", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(title=book.title, author=book.author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
