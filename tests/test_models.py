import unittest
from pydantic import ValidationError
from app.models import EventRequest, Event, LeagueEnum

class TestModels(unittest.TestCase):
    def test_event_request_valid(self):
        # Test valid EventRequest
        data = {'league': LeagueEnum.NFL, 'startDate': '2024-01-01', 'endDate': '2024-01-10'}
        event_request = EventRequest(**data)
        self.assertEqual(event_request.league, LeagueEnum.NFL)
        self.assertEqual(event_request.startDate, '2024-01-01')
        self.assertEqual(event_request.endDate, '2024-01-10')

    def test_event_request_invalid(self):
        # Test invalid EventRequest (missing required fields)
        with self.assertRaises(ValidationError):
            EventRequest()

    def test_event_valid(self):
        # Test valid Event
        data = {
            'eventId': '1', 'eventDate': '2024-01-01', 'eventTime': '12:00:00',
            'homeTeamId': 'H1', 'homeTeamRank': 1, 'homeTeamRankPoints': 100,
            'homeTeamNickName': 'Team1', 'homeTeamCity': 'City1',
            'awayTeamId': 'A1', 'awayTeamRank': 2, 'awayTeamRankPoints': 90,
            'awayTeamNickName': 'Team2', 'awayTeamCity': 'City2'
        }
        event = Event(**data)
        self.assertEqual(event.eventId, '1')
        self.assertEqual(event.eventDate, '2024-01-01')
        self.assertEqual(event.eventTime, '12:00:00')

    def test_event_invalid(self):
        # Test invalid Event (missing required fields)
        with self.assertRaises(ValidationError):
            Event()

if __name__ == '__main__':
    unittest.main()
