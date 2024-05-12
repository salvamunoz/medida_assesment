import unittest
from unittest.mock import patch
from app.utils import process_events, get_scoreboard_data, get_team_rankings_data
from app.models import Event, EventRequest, LeagueEnum

class TestUtils(unittest.IsolatedAsyncioTestCase):

    @patch("app.utils.get_scoreboard_data")
    @patch("app.utils.get_team_rankings_data")
    async def test_process_events(self, mock_get_team_rankings_data, mock_get_scoreboard_data):
        # Mock data
        scoreboard_data = [{"id": "1", "timestamp": "2023-03-08T18:30:00", "home": {"id": "1", "nickName": "Warriors", "city": "San Francisco"}, "away": {"id": "2", "nickName": "Lakers", "city": "Los Angeles"}}]
        rankings_data = [{"teamId": "1", "rank": "1", "rankPoints": "100"}, {"teamId": "2", "rank": "2", "rankPoints": "90"}]

        mock_get_scoreboard_data.return_value = scoreboard_data
        mock_get_team_rankings_data.return_value = rankings_data

        # Test process_events
        request_data = EventRequest(league=LeagueEnum.NFL)
        events = await process_events(request_data)

        self.assertEqual(len(events), 1)
        self.assertIsInstance(events[0], Event)
        self.assertEqual(events[0].eventId, "1")
        self.assertEqual(events[0].homeTeamId, "1")
        self.assertEqual(events[0].homeTeamRank, 1)
        self.assertEqual(events[0].homeTeamRankPoints, 100)
        self.assertEqual(events[0].homeTeamNickName, "Warriors")
        self.assertEqual(events[0].homeTeamCity, "San Francisco")
        self.assertEqual(events[0].awayTeamId, "2")
        self.assertEqual(events[0].awayTeamRank, 2)
        self.assertEqual(events[0].awayTeamRankPoints, 90)
        self.assertEqual(events[0].awayTeamNickName, "Lakers")
        self.assertEqual(events[0].awayTeamCity, "Los Angeles")

    @patch("app.utils.fetch_data_from_url")
    async def test_get_scoreboard_data(self, mock_fetch_data_from_url):
        # Mock data
        mock_fetch_data_from_url.return_value = [{"id": "1", "timestamp": "2024-01-01T12:00:00"}]

        # Test get_scoreboard_data
        scoreboard_data = await get_scoreboard_data(LeagueEnum.NFL)

        self.assertEqual(len(scoreboard_data), 1)
        self.assertEqual(scoreboard_data[0]["id"], "1")

    @patch("app.utils.fetch_data_from_url")
    async def test_get_team_rankings_data(self, mock_fetch_data_from_url):
        # Mock data
        mock_fetch_data_from_url.return_value = [{"teamId": "H1", "rank": 1, "rankPoints": 100}, {"teamId": "A1", "rank": 2, "rankPoints": 90}]

        # Test get_team_rankings_data
        rankings_data = await get_team_rankings_data(LeagueEnum.NFL)

        self.assertEqual(len(rankings_data), 2)
        self.assertEqual(rankings_data[0]["teamId"], "H1")


if __name__ == "__main__":
    unittest.main()
