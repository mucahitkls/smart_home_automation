from pydantic import BaseModel
from typing import Optional, List


class LightDetails(BaseModel):
    name: str
    state: str
    color: str
    brightness: int
    mode: str
    available_modes: Optional[List[str]]

