from pydantic import BaseModel
from typing import Optional, List


class ThermostatDetails(BaseModel):
    name: str
    state: str
    temperature: int
    min_temperature: int
    max_temperature: int
    mode: str
    available_modes: Optional[List[str]]
