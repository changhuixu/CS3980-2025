from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from auth import Token, TokenData, create_access_token, decode_jwt_token
from hash_pass import HashPassword

in_memory_db = [
    {
        "username": "hi",
        "password": "$2b$12$hGcmUmfAsOTyc3hnmSCqq.o4gTKUmM5dbK4x6KCrAcGHn.RyA9jP2",  # hi123
    }
]

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
hash_password = HashPassword()


def get_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    print(token)
    return decode_jwt_token(token)


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    ## Authenticate user by verifying the user in DB
    username = form_data.username
    for u in in_memory_db:
        if u["username"] == username:
            authenticated = hash_password.verify_hash(form_data.password, u["password"])
            if authenticated:
                access_token = create_access_token({"username": username})
                return Token(access_token=access_token)

    raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/users/me")
async def read_my_username(user: Annotated[TokenData, Depends(get_user)]) -> TokenData:
    return user
