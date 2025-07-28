from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Notas(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    valor = Column(String)
    mes = Column(String)
    ano = Column(String)
    createdAt = Column(Date)

    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Clientes", back_populates="notas")

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("Users", back_populates="notas")
