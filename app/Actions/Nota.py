from sqlalchemy.orm import Session
from app.Tables.Notas import Nota

def get_notas(
        db: Session,
        cliente_id: int = None,
        user_id: int = None,
        ano: str = None,
        mes: str = None,
):
    query = db.query(Nota)

    if cliente_id:
        query = query.filter(Nota.cliente_id == cliente_id)
    if user_id:
        query = query.filter(Nota.user_id == user_id)
    if ano:
        query = query.filter(Nota.ano == ano)
    if mes:
        query = query.filter(Nota.mes == mes)

    return query.all()
