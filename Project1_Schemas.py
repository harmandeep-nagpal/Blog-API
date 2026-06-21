from pydantic import BaseModel

# INPUT Schema 
class BlogCreate(BaseModel):
    title : str
    content : str

class BlogResponse(BaseModel):
    id : int
    title: str
    content : str

    class Config:
        from_attributes = True