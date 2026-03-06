import sqlite3
from pathlib import Path
from typing import Dict, List, Optional

DB_PATH = Path(__file__).resolve().parent.parent / "jobs.db"

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db() -> None:
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT,
                url TEXT NOT NULL UNIQUE,
                source TEXT NOT NULL,
                scraped_at TEXT DEFAULT (datetime('now'))
            );
        """)
        conn.commit()

def upsert_job(job: Dict) -> bool:
    # Returns True if inserted, False if already exists (duplicate URL)
    with get_conn() as conn:
        try:
            conn.execute("""
                INSERT INTO jobs (title, company, location, url, source)
                VALUES (?, ?, ?, ?, ?)
            """, (job["title"], job["company"], job.get("location"), job["url"], job["source"]))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

def list_jobs(limit: int = 50, location: Optional[str] = None) -> List[Dict]:
    query = "SELECT title, company, location, url, source, scraped_at FROM jobs"
    params = []
    if location:
        query += " WHERE location LIKE ?"
        params.append(f"%{location}%")
    query += " ORDER BY scraped_at DESC LIMIT ?"
    params.append(limit)

    with get_conn() as conn:
        rows = conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]