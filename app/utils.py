import logging
from aiohttp import ClientSession, ClientResponseError
from .models import Event, EventRequest,LeagueEnum
from .config import DOCKER_CONTAINER_URL


async def get_scoreboard_data(league: LeagueEnum) -> list[dict]:
    url = f"{DOCKER_CONTAINER_URL}/{league}/scoreboard"
    return await fetch_data_from_url(url)


async def get_team_rankings_data(league: LeagueEnum) -> list[dict]:
    url = f"{DOCKER_CONTAINER_URL}/{league}/team-rankings"
    return  await fetch_data_from_url(url)


async def fetch_data_from_url(url: str) -> dict:
    try:
        async with ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Raise exception for non-2xx status codes
                return await response.json()
    except ClientResponseError as e:
        raise Exception(f"Error fetching data from Docker/URL: {str(e)}")   


async def process_events(request_data: EventRequest) -> list[Event]:
    try:
        scoreboard_data = await get_scoreboard_data(request_data.league)
        rankings_data = await get_team_rankings_data(request_data.league)
    except Exception as e:
        # Handle error fetching data
        logging.error(f"Error fetching data: {e}")
        return []

    events = []

    rankings_dict = {ranking['teamId']: ranking for ranking in rankings_data}
    
    for event in scoreboard_data:

        event_date, event_time = event["timestamp"].split("T")
        home_ranking = rankings_dict.get(event['home']['id'])
        away_ranking = rankings_dict.get(event['away']['id'])
        # Extract relevant data from scoreboard
        event_obj = Event(
            eventId=event["id"],
            eventDate=event_date,
            eventTime=event_time,
            homeTeamId=event["home"]["id"],
            homeTeamRank=home_ranking['rank'],
            homeTeamRankPoints=home_ranking['rankPoints'],
            homeTeamNickName=event["home"]["nickName"],
            homeTeamCity=event["home"]["city"],
            awayTeamId=event["away"]["id"],
            awayTeamNickName=event["away"]["nickName"],
            awayTeamCity=event["away"]["city"],
            awayTeamRank=away_ranking['rank'],  
            awayTeamRankPoints=away_ranking['rankPoints'],
        )

        if request_data.startDate and event_obj.eventDate < request_data.startDate:
            continue
        if request_data.endDate and event_obj.eventDate > request_data.endDate:
            continue

        events.append(event_obj)

    return events
