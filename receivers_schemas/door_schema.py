from pydantic import BaseModel


class DoorDetails(BaseModel):
    name: str
    device_type: str
    state: str
    lock_state: str
