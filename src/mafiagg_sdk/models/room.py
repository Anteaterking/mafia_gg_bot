import datetime as dt
from dataclasses import dataclass

from mafiagg_sdk.models.base import Base
from mafiagg_sdk.models.user import User


@dataclass
class Room(Base):
    id: str
    name: str
    has_started: bool
    player_count: int
    setup_size: int
    host_user: User
    created_at: dt.datetime

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at = dt.datetime.fromisoformat(self.created_at)
