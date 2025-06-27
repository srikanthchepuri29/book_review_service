from pydantic import BaseModel

class ReviewCreate(BaseModel):
    review_text: str
    rating: int

class ReviewOut(ReviewCreate):
    id: int
    book_id: int
    class Config:
        orm_mode = True
