from api.db import init_db, upsert_job

def insert_realistic_sample_jobs():
    jobs = [
        {
            "title": "Cloud Engineer AWS",
            "company": "Amazon",
            "location": "Dublin",
            "url": "https://example.com/aws-cloud-engineer",
            "source": "sample"
        },
        {
            "title": "DevOps Engineer Docker Kubernetes",
            "company": "Stripe",
            "location": "Dublin",
            "url": "https://example.com/devops-engineer",
            "source": "sample"
        },
        {
            "title": "Platform Engineer Terraform AWS",
            "company": "HubSpot",
            "location": "Dublin",
            "url": "https://example.com/platform-engineer",
            "source": "sample"
        },
        {
            "title": "Site Reliability Engineer Linux Python",
            "company": "Google",
            "location": "Dublin",
            "url": "https://example.com/sre-role",
            "source": "sample"
        }
    ]

    inserted = 0

    for job in jobs:
        if upsert_job(job):
            inserted += 1

    print(f"Inserted {inserted} jobs")


if __name__ == "__main__":
    init_db()
    insert_realistic_sample_jobs()