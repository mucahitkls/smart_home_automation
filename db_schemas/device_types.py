from pydantic import BaseModel

class DeviceType(BaseModel):
    type_name: str


class DeviceTypeResponse(DeviceType):
    device_type_id: int

    class Config:
        orm_mode = True
