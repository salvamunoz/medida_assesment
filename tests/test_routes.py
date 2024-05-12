import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.testing = True
        self.client = app.test_client()

    def test_polling_events(self):
        response = self.client.post('/events', json={'league': 'NFL'})
        self.assertEqual(response.status_code, 200)

    def test_polling_events_incorrect_body(self):
        response = self.client.post('/events', json={'league': 'NFL', 'incorrect_key': 'value'})
        self.assertEqual(response.status_code, 400)

    def test_polling_events_incorrect_league(self):
        response = self.client.post('/events', json={'league': 'NBA'})
        self.assertEqual(response.status_code, 400)

    def test_polling_events_invalid_endpoint(self):
        response = self.client.post('/event', json={'league': 'NFL'})
        self.assertEqual(response.status_code, 404)
