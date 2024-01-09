from pydantic import BaseModel
from typing import Optional, List


class TvDetails(BaseModel):
    name: str
    state: str
    current_channel: int
    current_volume: int
    current_mode: str
    max_channel: int
    max_volume: int
    available_modes: Optional[List[str]]
