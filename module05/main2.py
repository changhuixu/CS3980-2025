from typing import Annotated
from fastapi import FastAPI, Path


app = FastAPI(
    title="ChimichangApp",
    description="string description",
    summary="Deadpool's favorite app. Nuff said.",
    version="3.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/items/{item_id}")
async def get_item_by_id(
    item_id: Annotated[
        int,
        Path(
            ge=0,
            le=1000,
            multiple_of=3,
        ),
    ]
) -> dict:
    return {"item_id": item_id}
