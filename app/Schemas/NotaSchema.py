from pydantic import BaseModel
from datetime import date

class NotaSchema():
    class NotaBase(BaseModel):
        tipo: str
        valor: str
        mes: str
        ano: str
        # createdAt: date

    class NotaCreate(NotaBase):
        cliente_id: int
        user_id: int

    class NotaOut(NotaBase):
        id: int
        cliente_id: int
        user_id: int

        class Config:
            from_attributes = True
