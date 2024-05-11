import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.testing = True
        self.client = app.test_client()

    def test_polling_events(self):
        response = self.client.post('/events/NFL', json={'league': 'NFL'})
        self.assertEqual(response.status_code, 200)
