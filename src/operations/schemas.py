from pydantic import BaseModel

class BookCreate(BaseModel):
    id: int
    name: str
    author: str
    category: str
    year: int