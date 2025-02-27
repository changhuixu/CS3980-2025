from fastapi import APIRouter, status

from todo import Todo


todo_router = APIRouter()

todo_list = []


@todo_router.get("")
async def get_todos() -> dict:
    return {"todos": todo_list}


@todo_router.post("", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "new todo added"}
