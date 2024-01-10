from pydantic import BaseModel
from typing import List


class DeviceBase(BaseModel):
    name: str
    state: str


class DeviceCreate(DeviceBase):
    device_type_id: int


class Device(DeviceBase):
    device_id: int
    user_id: int

    class Config:
        orm_mode = True


# Base schema for LightAttributes
class LightAttributesBase(BaseModel):
    color: str
    brightness: int
    mode: str
    available_modes: List[str]


# Schema for creating new LightAttributes
class LightAttributesCreate(LightAttributesBase):
    pass


# Schema for returning LightAttributes from the database
class LightAttributesInDB(LightAttributesBase):
    light_id: int



# Base schema for ThermostatAttributes
class ThermostatAttributesBase(BaseModel):
    current_temperature: int
    mode: str


# Schema for creating new ThermostatAttributes
class ThermostatAttributesCreate(ThermostatAttributesBase):
    min_temperature: int
    max_temperature: int
    available_modes: List[str]


# Schema for returning ThermostatAttributes from the database
class ThermostatAttributesInDB(ThermostatAttributesBase):
    thermostat_id: int



# Base schema for TvAttributes
class TvAttributesBase(BaseModel):
    current_channel: int
    current_volume: int
    current_mode: str


# Schema for creating new TvAttributes
class TvAttributesCreate(TvAttributesBase):
    max_channel: int
    max_volume: int
    available_modes: List[str]


# Schema for returning TvAttributes from the database
class TvAttributesInDB(TvAttributesBase):
    tv_id: int


class DoorAttributesBase(BaseModel):
    lock_state: str


# Schema for creating new DoorAttributes
class DoorAttributesCreate(DoorAttributesBase):
    pass


# Schema for returning DoorAttributes from the database
class DoorAttributesInDB(DoorAttributesBase):
    door_id: int
