# Cloud Job Analyzer

A cloud data pipeline project that collects tech job listings and exposes them through an API.

## Features
- Job scraping pipeline
- SQLite database storage
- FastAPI REST API
- Swagger documentation

## Tech Stack
- Python
- FastAPI
- SQLite
- Requests
- BeautifulSoup

## Run the Project

Activate environment

.venv\Scripts\activate

Run scraper

python -m scraper.scrape

Start API

uvicorn api.main:app --reload

Open

http://127.0.0.1:8000/docs