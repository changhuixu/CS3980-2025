async def app(scope, receive, send):
    assert scope["type"] == "http"

    await send({"type": "http.response.start", "status": 200, "headers": []})
    await send({"type": "http.response.body", "body": b"Hello world!"})
