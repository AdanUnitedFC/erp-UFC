from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="UFC Intrasys API", version="1.0")

app.include_router(auth.router, tags=["Auth"])

@app.get("/")
def root():
    return {"message": "API UFC Intrasys en funcionamiento"}
