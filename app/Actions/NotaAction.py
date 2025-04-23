from sqlalchemy.orm import Session
from sqlalchemy import select

from ..Tables import Notas,Clientes

from ..Schemas import User



def get_notas(db: Session, user_id: int):
    return db.query(Notas).join(Notas.cliente).filter(Clientes.user_id == user_id).get()


def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()

def create_user(db: Session, user: User.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = Users(
    email=user.email,
    hashed_password=fake_hashed_password,
    name=user.name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user