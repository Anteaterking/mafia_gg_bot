import datetime as dt
from dataclasses import dataclass
from typing import List

from mafiagg_sdk.models.base import Base


@dataclass
class UserSessionResponse(Base):
    id: int
    username: str
    email: str
    time_format: str
    host_banned_usernames: List[str]
    is_patreon_linked: bool
    is_active_patreon: bool
    needs_verification: bool
    created_at: dt.datetime

    def __post_init__(self):
        if isinstance(self.createdAt, str):
            self.createdAt = dt.datetime.fromisoformat(self.createdAt)
