from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends
from database.database import get_db
from database.crud_user import get_user_by_email, get_user_by_username
from db_models.user_and_iot_devices import User
from db_schemas.user_schema import User
from utils.utilities import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def verify_password(plain_text_password, hashed_password):
    return pwd_context.verify(plain_text_password, hashed_password)


def get_hashed_password(password):
    return pwd_context.hash(password)


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db=db, username=username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return True


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_schema)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    payload = decode_token(token)
    if payload is None:
        raise credentials_exception

    username: str = payload.get('sub')

    if username is None:
        raise credentials_exception

    user = get_user_by_username(db=db, username=username)

    if user is None:
        raise credentials_exception

    return user
