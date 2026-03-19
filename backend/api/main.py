from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(
    title="AI Research Paper Intelligence Platform",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Research Paper Platform Running"}