from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="Electronics Inventory System")


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(auth.router)
