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


@app.get("/skills")
def skills():
    jobs = list_jobs(limit=100)

    skills_list = [
        "AWS",
        "Docker",
        "Terraform",
        "Kubernetes",
        "Python",
        "Linux"
    ]

    result = {skill: 0 for skill in skills_list}

    for job in jobs:
        text = job["title"].lower()

        for skill in skills_list:
            if skill.lower() in text:
                result[skill] += 1

    return result


@app.get("/top-skills")
def top_skills():
    jobs = list_jobs(limit=100)

    skills_list = [
        "AWS",
        "Docker",
        "Terraform",
        "Kubernetes",
        "Python",
        "Linux"
    ]

    result = {skill: 0 for skill in skills_list}

    for job in jobs:
        text = job["title"].lower()

        for skill in skills_list:
            if skill.lower() in text:
                result[skill] += 1

    sorted_skills = sorted(result.items(), key=lambda x: x[1], reverse=True)

    return {"top_skills": sorted_skills}