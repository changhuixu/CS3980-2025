from contextlib import asynccontextmanager
import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from db.db_context import init_database
from logging_setup import setup_logging
from routers.todo import todo_router
from routers.user import user_router
from routers.movie import movie_router

setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup event
    logger.info("Application starts...")
    await init_database()
    yield
    # on shutdown event
    logger.info("Application shuts down...")


app = FastAPI(title="Todo App", version="2.0.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(todo_router, tags=["Todos"], prefix="/todos")
app.include_router(user_router, tags=["Users"], prefix="/users")
app.include_router(movie_router, tags=["Movies"], prefix="/movies")


# uvicorn.run(app, host="localhost", port=8000)
