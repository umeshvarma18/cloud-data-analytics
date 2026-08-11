from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Cloud Data Analytics API"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Cloud Data Analytics API Running"
    }