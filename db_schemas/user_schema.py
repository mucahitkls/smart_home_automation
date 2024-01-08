from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserLoginBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(UserLoginBase):
    password: str


class User(UserCreate):
    user_id: int

    class Config:
        orm_mode = True
