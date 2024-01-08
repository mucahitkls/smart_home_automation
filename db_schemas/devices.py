from pydantic import BaseModel


class DeviceBase(BaseModel):
    name: str
    state: str


class DeviceCreate(DeviceBase):
    user_id: int
    device_type_id: int


class Device(DeviceBase):
    device_id: int

    class Config:
        orm_mode = True