from sqlalchemy import Column, Integer, ForeignKey, String, Index
from app.db.base import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    review_text = Column(String)
    rating = Column(Integer)

    __table_args__ = (Index("ix_review_book_id", "book_id"),)
