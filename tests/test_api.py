import unittest
from app import create_app

class FlaskMongoDBTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_get_books(self):
        response = self.app.get('/api/books')
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
        response = self.app.post('/api/books', json={"title": "Test Book", "author": "Author Name"})
        self.assertEqual(response.status_code, 201)

    def test_delete_book(self):
        self.app.post('/api/books', json={"title": "Temp Book", "author": "Temp Author"})
        response = self.app.delete('/api/books/Temp Book')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
