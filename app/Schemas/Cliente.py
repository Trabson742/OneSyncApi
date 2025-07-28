from pydantic import BaseModel


class Cliente():
    class ClienteBase(BaseModel):
        nome: str
        cpfcnpj: str
        email: str

    class ClienteCreate(ClienteBase):
        pass

    class Cliente(ClienteBase):
        id: int
        is_active: bool

        class Config:
            orm_mode = True

    class ClienteResource(ClienteBase):
        id: int
        is_active: bool

        class Config:
            orm_mode = True
