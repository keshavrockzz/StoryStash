from flask import Blueprint, jsonify, request, render_template_string, current_app
from .models import BookModel

api_blueprint = Blueprint('api', __name__)


# Homepage Route
@api_blueprint.route('/')
def homepage():
    return render_template_string("""
        <html>
            <head>
                <title>BookNest API</title>
                <style>
                    body { font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }
                    h1 { color: #333; }
                    ul { list-style: none; padding: 0; }
                    li { margin: 10px 0; }
                    a { text-decoration: none; color: #007BFF; }
                    a:hover { text-decoration: underline; }
                    .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>📚 Welcome to BookNest API!</h1>
                    <p>This API helps manage your book collection. Explore the available endpoints:</p>
                    <ul>
                        <li><a href="/books">View All Books (GET)</a></li>
                        <li><a href="/books" title="POST /api/books">Add a New Book (POST)</a></li>
                        <li><a href="#" onclick="alert('Use DELETE /books/<title> via Postman or curl!')">Delete a Book (DELETE)</a></li>
                    </ul>
                </div>
            </body>
        </html>
    """)

@api_blueprint.route('/books', methods=['GET'])
def get_books():
    books = list(current_app.db.books.find({}, {"_id": 0}))
    return jsonify({"books": books}), 200

@api_blueprint.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or not all(key in data for key in ["title", "author"]):
        return jsonify({"error": "Missing required fields: title, author"}), 400

    current_app.db.books.insert_one({"title": data["title"], "author": data["author"]})
    return jsonify({"message": "Book added successfully"}), 201

@api_blueprint.route('/books/<title>', methods=['DELETE'])
def delete_book(title):
    result = current_app.db.books.delete_one({"title": title})
    if result.deleted_count == 0:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({"message": "Book deleted successfully"}), 200
