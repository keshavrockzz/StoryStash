import os

class Config:
    MONGO_USER = os.getenv("MONGO_USER", "admin1")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "password")
    MONGO_URI = os.getenv("MONGO_URI", f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@localhost:27017/bookstore?authSource=bookstore")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "bookstore")
    APP_PORT = int(os.getenv("APP_PORT", 5000))
    APP_DEBUG = os.getenv("APP_DEBUG", "true").lower() == "true"
