from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum

class LeagueEnum(Enum):
    NFL: str = "NFL"


class EventRequest(BaseModel):
    league: LeagueEnum
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
    """class Config:
        arbitrary_types_allowed = True  # """


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
