from sqlalchemy.orm import Session
from sqlalchemy import select

from ..Tables import Users,Clientes

from ..Schemas import UserSchema

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()

def authenticate_user(db:Session, email: str, password: str):
    # 1. Get user from DB
    user = get_user_by_email(db,email) 
    if not user:
        return False
    # 2. Verify password
    if not verify_password(password, user.hashed_password):
        return False
    return user


def get_user_by_email(db: Session, email: str):
    user = db.query(Users).filter(Users.email == email).first()
    return user
    # return User.UserResource(user)

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserSchema.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = Users(
    email=user.email,
    hashed_password=hashed_password,
    name=user.name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user