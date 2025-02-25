from fastapi import FastAPI
from todo_routes import todo_router

app = FastAPI(title="My Todo App")
app.include_router(todo_router)


@app.get("/")
async def welcome() -> dict:
    return {"msg": " Hello"}
