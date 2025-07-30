from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship,Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

from ..database import Base,SessionLocal


# Base = declarative_base()

class Clientes(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    cpfcnpj = Column(String, unique=True, index=True)
    name = Column(String)
    contato = Column(String)
    celular = Column(String)
    user_id = mapped_column(ForeignKey("users.id"))
    user = relationship("Users")
    notas = relationship("Notas")
