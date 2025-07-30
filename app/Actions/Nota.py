from sqlalchemy.orm import Session
from app.Tables.Notas import Notas
from app.Schemas.NotaSchema import NotaSchema

def get_notas(
        db: Session,
        cliente_id: int = None,
        user_id: int = None,
        ano: str = None,
        mes: str = None,
):
    query = db.query(Notas)

    if cliente_id:
        query = query.filter(Notas.cliente_id == cliente_id)
    if user_id:
        query = query.filter(Notas.user_id == user_id)
    if ano:
        query = query.filter(Notas.ano == ano)
    if mes:
        query = query.filter(Notas.mes == mes)

    return query.all()

def create_nota(
        db: Session, nota: NotaSchema.NotaCreate
):
    db_nota = Notas(**nota.dict())
    db.add(db_nota)
    db.commit()
    db.refresh(db_nota)
    return db_nota
    return query.all()
