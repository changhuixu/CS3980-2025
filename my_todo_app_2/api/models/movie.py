from beanie import Document
from pydantic import BaseModel


# don't redefine "id" field. Here, we use the default MongoDB objectId
class Movie(Document):
    title: str
    year: int
    created_by: str

    class Settings:
        name = "movies"


class MovieRequest(BaseModel):
    title: str
    year: int
