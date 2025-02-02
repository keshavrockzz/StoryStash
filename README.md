# 📚 BookNest API

A simple, RESTful API built with **Flask** and **MongoDB** for managing a collection of books. This lightweight microservice is perfect for CRUD operations, easy deployment with Docker, and scalable for Kubernetes environments.

---

## 🚀 Features

- **CRUD Operations**: Create, Read, Update, and Delete books
- **MongoDB Integration**: Efficient data storage using PyMongo
- **Docker-Ready**: Containerized for smooth deployment
- **Environment Configurations**: Manage settings via `.env` and `Config` files
- **Unit Tests**: Built-in testing with Python's `unittest`

---

## 🗂️ Project Structure

```
BookNest-API/
├── app/                # Application code
│   ├── __init__.py     # App factory
│   ├── routes.py       # API endpoints
│   ├── models.py       # Data models (if extended)
│   └── config.py       # Configuration settings
├── tests/              # Unit tests
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
├── .env                # Environment variables
└── README.md           # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/booknest-api.git
cd booknest-api
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
MONGO_USER=admin
MONGO_PASSWORD=password
MONGO_URI=mongodb://admin:password@localhost:27017/
DATABASE_NAME=booknest
APP_PORT=5000
APP_DEBUG=true
```

### 4️⃣ Run the Application

```bash
python run.py
```

The API will be available at `http://localhost:5000/api`.

---

## 🐳 Docker Deployment

### Build the Docker Image

```bash
docker build -t booknest-api .
```

### Run the Container

```bash
docker run -p 5000:5000 --env-file .env booknest-api
```

---

## 🔗 API Endpoints

| Method | Endpoint                | Description             |
|--------|-------------------------|-------------------------|
| GET    | `/api/books`            | Fetch all books         |
| POST   | `/api/books`            | Add a new book          |
| DELETE | `/api/books/<title>`    | Delete a book by title  |

### Example Requests

**GET /api/books**

```bash
curl http://localhost:5000/api/books
```

**POST /api/books**

```bash
curl -X POST http://localhost:5000/api/books \
     -H "Content-Type: application/json" \
     -d '{"title": "The Alchemist", "author": "Paulo Coelho"}'
```

**DELETE /api/books/<title>**

```bash
curl -X DELETE http://localhost:5000/api/books/The%20Alchemist
```

---

## 🧪 Running Tests

```bash
python -m unittest discover tests
```

---

## 📦 Kubernetes (Optional)

You can deploy this API on a local Minikube cluster for CKAD practice. Example manifests:

- **Deployment**: `booknest-deployment.yaml`
- **Service**: `booknest-service.yaml`
- **ConfigMap & Secret**: For managing environment variables securely

*(Let me know if you'd like the YAML files too!)*

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a pull request

---

## 🙌 Acknowledgments

- **Flask** - Lightweight Python web framework
- **MongoDB** - NoSQL database for flexible data storage
- **Docker** - For easy containerization and deployment

Happy coding! 🚀

