from pydantic import BaseModel


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