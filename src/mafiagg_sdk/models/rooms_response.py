from dataclasses import dataclass
from typing import List

from mafiagg_sdk.models.base import Base
from mafiagg_sdk.models.room import Room


@dataclass
class RoomsResponse(Base):
    rooms: List[Room]
    unlisted_count: int
