from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({"Hello": "World"})


app = Starlette(debug=True, routes=[Route("/", homepage)])
