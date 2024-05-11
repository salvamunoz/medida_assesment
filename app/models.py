from pydantic import BaseModel
from typing import Optional

class LeagueEnum(str):
    NFL = "NFL"


class EventRequest(BaseModel):
    league: LeagueEnum
    startDate: Optional[str] = None
    endDate: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True


class Event(BaseModel):
    eventId: str
    eventDate: str
    eventTime: str
    homeTeamId: str
    homeTeamNickName: str
    homeTeamCity: str
    homeTeamRank: int
    homeTeamRankPoints: float
    awayTeamId: str
    awayTeamNickName: str
    awayTeamCity: str
    awayTeamRank: int
    awayTeamRankPoints: float
