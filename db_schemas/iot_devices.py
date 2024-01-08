from pydantic import BaseModel


class LightAttributes(BaseModel):
    brightness: int
    color: str
    mode: str


class ThermostatAttributes(BaseModel):
    current_temperature: int
    target_temperature: int
    mode: int


class TvAttributes(BaseModel):
    current_channel: int
    current_volume: int
    current_mode: str


class DoorAttributes(BaseModel):
    door_state: str
    lock_state: str
