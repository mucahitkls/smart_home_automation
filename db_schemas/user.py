from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    username: str
    email: str


class UserCreate(UserBase):
    hashed_password: str


class UserLogin(UserBase):
    pass


class User(UserCreate):
    pass
