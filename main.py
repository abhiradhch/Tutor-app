from fastapi import FastAPI
from db.database import engine,Base
from models import user
from routes import auth

app = FastAPI()
app.include_router(auth.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Backend is running"}