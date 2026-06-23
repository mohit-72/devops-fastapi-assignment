import os

from fastapi import FastAPI
from dotenv import load_dotenv
import psycopg2
import redis

load_dotenv()

app = FastAPI(
    title="DevOps Assignment API",
    description="Production-ready FastAPI application for DevOps Engineer Technical Assignment.",
    version="1.0.0",
    contact={
        "name": "Mohit",
        "email": "YOUR_EMAIL_HERE"
    }
)


@app.get("/", tags=["API"])
def home():
    return {
        "message": "Welcome to DevOps FastAPI Assignment"
    }


@app.get("/health", tags=["Monitoring"])
def health():

    db_status = "Disconnected"
    redis_status = "Disconnected"

    # PostgreSQL Check
    try:
        conn = psycopg2.connect(
            host="postgres",
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )
        conn.close()
        db_status = "Connected"
    except Exception:
        pass

    # Redis Check
    try:
        r = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT")),
            decode_responses=True,
        )
        r.ping()
        redis_status = "Connected"
    except Exception:
        pass

    return {
        "status": "healthy",
        "postgres": db_status,
        "redis": redis_status
    }