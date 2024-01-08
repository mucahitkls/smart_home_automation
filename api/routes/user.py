from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from db_schemas import user_schema
from database.database import get_db
from database import crud_user
from services import authentication

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}}
)


@router.post('/register', response_model=user_schema.User)
async def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail='User already registered')
    return crud_user.create_user(db=db, user=user)


@router.post("/login")
async def login(user: user_schema.UserLogin, db: Session = Depends(get_db)):
    user = authentication.authenticate_user(db, user.username, user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    # Create a new access token
    access_token = authentication.create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get("/", response_model=List[user_schema.User])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_user.get_users(db=db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=user_schema.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_id(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@router.put("/{user_id}", response_model=user_schema.User)
async def update_user(user_id: int, user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return crud_user.update_user(db=db, user_id=user_id, user=user)


@router.delete("/{user_id}", response_model=user_schema.User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud_user.delete_user(db=db, user_id=user_id)
