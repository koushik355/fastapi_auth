from sqlalchemy.orm import Session
from . import models, schemas

userModel = models.User


def get_user(db: Session, user_id: int):
    return db.query(userModel).filter(userModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(userModel).filter(userModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(userModel).offset(skip).limit(limit).all()


item_model = models.Item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(item_model).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    password = 'fake_hashed_password'
    db_user = models.User(email=user.email, hashed_password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_item(db: Session, item: schemas.Item, user_id: int):
    db_item = item_model(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
