from api.db import init_db, upsert_job

def insert_sample_jobs():
    jobs = [
        {
            "title": "Cloud Engineer",
            "company": "Amazon",
            "location": "Dublin",
            "url": "https://example.com/aws-job",
            "source": "sample"
        },
        {
            "title": "DevOps Engineer",
            "company": "Google",
            "location": "Dublin",
            "url": "https://example.com/google-job",
            "source": "sample"
        },
        {
            "title": "Platform Engineer",
            "company": "Stripe",
            "location": "Dublin",
            "url": "https://example.com/stripe-job",
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
    insert_sample_jobs()