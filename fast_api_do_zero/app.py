from fastapi import FastAPI

from fast_api_do_zero.routers import auth, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
