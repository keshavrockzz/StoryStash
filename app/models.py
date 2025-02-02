from pymongo import MongoClient
from flask import current_app

def get_db():
    """Establishes a connection to MongoDB using app config."""
    client = MongoClient(current_app.config['MONGO_URI'])
    db = client[current_app.config['DATABASE_NAME']]
    return db

class BookModel:
    """Handles database operations for books."""

    @staticmethod
    def create_book(book_data):
        db = get_db()
        return db.books.insert_one(book_data)

    @staticmethod
    def get_all_books():
        db = get_db()
        return list(db.books.find({}, {'_id': 0}))  # Excludes MongoDB's default _id field

    @staticmethod
    def delete_book(title):
        db = get_db()
        return db.books.delete_one({'title': title})
