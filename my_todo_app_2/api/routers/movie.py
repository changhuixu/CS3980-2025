import logging
from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, Path, HTTPException, status

from auth.jwt_auth import TokenData
from models.movie import Movie, MovieRequest

from typing import Annotated

from models.user import ensure_admin_role
from routers.user import get_user

movie_router = APIRouter()
logger = logging.getLogger(__name__)


@movie_router.post("", status_code=status.HTTP_201_CREATED)
async def add_new_movie(
    r: MovieRequest, user: Annotated[TokenData, Depends(get_user)]
) -> Movie:
    logger.info(f"{user.username} is trying to add a movie")
    new_movie = Movie(title=r.title, year=r.year, created_by=user.username)
    new_movie = await Movie.insert_one(new_movie)
    logger.info("new movie added")
    return new_movie


@movie_router.get("")
async def get_all_movies(user: Annotated[TokenData, Depends(get_user)]) -> list[Movie]:
    ensure_admin_role(user)
    return await Movie.find_all().to_list()


@movie_router.get("/my")
async def get_my_movies(user: Annotated[TokenData, Depends(get_user)]) -> list[Movie]:
    if not user or not user.username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Please login.",
        )
    return await Movie.find(Movie.created_by == user.username).to_list()


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


@movie_router.delete("/{id}")
async def delete_movie_by_id(
    id: PydanticObjectId, user: Annotated[TokenData, Depends(get_user)]
) -> dict:
    ensure_admin_role(user)
    movie = await Movie.get(id)
    if movie:
        await movie.delete()
        return {"message": "movie deleted"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The movie with ID={id} is not found.",
    )
