from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, Path, HTTPException, status

from auth.jwt_auth import TokenData
from models.movie import Movie, MovieRequest

from typing import Annotated

from routers.user import get_user

movie_router = APIRouter()


@movie_router.post("", status_code=status.HTTP_201_CREATED)
async def add_new_movie(r: MovieRequest) -> Movie:
    new_movie = Movie(title=r.title, year=r.year)
    await Movie.insert_one(new_movie)
    return new_movie


@movie_router.get("")
async def get_movies() -> list[Movie]:
    return await Movie.find_all().to_list()


@movie_router.get("/{id}")
async def get_movie_by_id(
    id: PydanticObjectId, user: Annotated[TokenData, Depends(get_user)]
) -> Movie:
    movie = await Movie.get(id)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The movie with ID={id} is not found.",
    )
