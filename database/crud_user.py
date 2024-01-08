from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from passlib.context import CryptContext
from db_models.user_and_iot_devices import User
from db_schemas import user_schema

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user=user_schema.UserCreate):
    hashed_password_ = pwd_context.hash(user.password)
    db_user = User(email=user.email, username=user.username, password=hashed_password_, )
    db.add(db_user)

    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def update_user(db: Session, user_id: int, user: user_schema.UserCreate):
    db_user = get_user_by_id(db=db, user_id=user_id)
    if not db_user:
        return None
    for var, value in vars(user).items():
        setattr(db_user, var, value) if value else None

    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def delete_user(db: Session, user_id: int):
    db_user = get_user_by_id(db=db, user_id=user_id)
    if not db_user:
        return None

    try:
        db.delete(db_user)
        db.commit()
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        raise e
