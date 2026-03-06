from fastapi import FastAPI
from api.db import init_db, list_jobs

app = FastAPI(title="Cloud Job Analyzer API")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/jobs")
def jobs(limit: int = 50, location: str | None = None):
    items = list_jobs(limit=limit, location=location)
    return {"count": len(items), "items": items}