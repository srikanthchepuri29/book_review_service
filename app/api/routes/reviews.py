from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.review import Review
from app.models.book import Book
from app.schemas.review import ReviewCreate, ReviewOut

router = APIRouter()

@router.get("/{book_id}/reviews", response_model=list[ReviewOut])
def list_reviews(book_id: int, db: Session = Depends(get_db)):
    return db.query(Review).filter(Review.book_id == book_id).all()

@router.post("/{book_id}/reviews", response_model=ReviewOut)
def create_review(book_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    if not db.query(Book).filter(Book.id == book_id).first():
        raise HTTPException(status_code=404, detail="Book not found")
    new_review = Review(book_id=book_id, **review.dict())
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
