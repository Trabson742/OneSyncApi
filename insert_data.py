from sqlalchemy.orm import Session
from datetime import date

from app.Tables.Users import Users
from app.Tables.Clientes import Clientes
from app.Tables.Notas import Notas
from app.database import SessionLocal, engine, Base

def create_tables():
    Base.metadata.create_all(bind=engine)

def insert_sample_data(db: Session):
    # Inserir usuários
    user1 = Users(email="user1@example.com", name="Usuário Teste 1", hashed_password="hashed_password_1", is_active=True)
    user2 = Users(email="user2@example.com", name="Usuário Teste 2", hashed_password="hashed_password_2", is_active=True)
    db.add_all([user1, user2])
    db.commit()
    db.refresh(user1)
    db.refresh(user2)

    # Inserir clientes
    clienteA = Clientes(cpfcnpj="111.111.111-11", name="Cliente A", contato="clienteA@email.com", celular="11987654321", user_id=user1.id)
    clienteB = Clientes(cpfcnpj="222.222.222-22", name="Cliente B", contato="clienteB@email.com", celular="22987654321", user_id=user1.id)
    clienteC = Clientes(cpfcnpj="333.333.333-33", name="Cliente C", contato="clienteC@email.com", celular="33987654321", user_id=user2.id)
    db.add_all([clienteA, clienteB, clienteC])
    db.commit()
    db.refresh(clienteA)
    db.refresh(clienteB)
    db.refresh(clienteC)

    # Inserir notas
    nota1 = Notas(tipo="NPS", valor="9", mes="Julho", ano="2025", createdAt=date(2025, 7, 26), cliente_id=clienteA.id, user_id=user1.id)
    nota2 = Notas(tipo="NPS", valor="7", mes="Julho", ano="2025", createdAt=date(2025, 7, 26), cliente_id=clienteB.id, user_id=user1.id)
    nota3 = Notas(tipo="NPS", valor="10", mes="Julho", ano="2025", createdAt=date(2025, 7, 26), cliente_id=clienteC.id, user_id=user2.id)
    db.add_all([nota1, nota2, nota3])
    db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    try:
        create_tables() # Certifica-se de que as tabelas existem antes de inserir dados
        insert_sample_data(db)
        print("Dados de exemplo inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        db.close()