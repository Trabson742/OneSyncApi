from pydantic import BaseModel
from .Cliente import ClienteCreate

class NotaBase(BaseModel):
    score: int
    tipo: str

class NotaCreate(NotaBase):
    Cliente: ClienteCreate

# class User(UserBase):
#     id: int
#     is_active: bool
#     class Config:
#         orm_mode = True