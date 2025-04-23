from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Date
from sqlalchemy.orm import relationship,Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

from ..database import Base,SessionLocal


# Base = declarative_base()

class Notas(Base):
    __tablename__ = "notas"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    valor = Column(String)
    mes = Column(String)
    ano = Column(String)
    createdAt= Column(Date)
    cliente_id = mapped_column(ForeignKey("clientes.id"))
    cliente = relationship("Clientes")
    user_id = mapped_column(ForeignKey("users.id"))
    user = relationship("Users")
