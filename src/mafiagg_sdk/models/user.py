import datetime as dt
from dataclasses import dataclass

from mafiagg_sdk.models.base import Base


@dataclass
class User(Base):
    id: str
    username: str
    active_patreon: bool
    created_at: dt.datetime

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at = dt.datetime.fromisoformat(self.created_at)
