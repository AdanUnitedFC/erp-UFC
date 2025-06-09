from fastapi import FastAPI
from app.routers import auth
from app.routers import upload
from app.routers import data
from app.routers import history
from app import models
from app.database import engine

app = FastAPI(title="UFC Intrasys API", version="1.0")

app.include_router(auth.router, tags=["Auth"])
app.include_router(upload.router)
app.include_router(data.router)
app.include_router(history.router)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API UFC Intrasys en funcionamiento"}

