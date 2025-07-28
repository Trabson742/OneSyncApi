# app/Actions.py

from sqlalchemy.orm import Session
from app.Tables import Clientes as ClienteModel
from ..Schemas.Cliente import ClienteCreate

def create_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = ClienteModel(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def get_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ClienteModel).offset(skip).limit(limit).all()
