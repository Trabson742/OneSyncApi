from typing import Union, Annotated
from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#projeto recurso
from .Tables import Users
from .Actions import Auth 
from .Schemas import User,NotaSchema
from .database import SessionLocal, engine, Base

#token config
from .token import JwtAuth

from uuid import uuid4

#config
Base.metadata.create_all(engine)
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency
def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()


#Usuários
@app.post("/users/")
def create_user(user: User.UserCreate, db: Session = Depends(get_db)):
  db_user = Auth.get_user_by_email(db, email=user.email)
  if db_user:
    raise HTTPException(status_code=400, detail="Email already registered")
  return Auth.create_user(db=db, user=user)
  

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  users = Auth.get_users(db, skip=skip, limit=limit)
  return users
################################################################################################

#Segurança/authenticação
@app.post("/token")
async def login_for_access_token(form_data: User.UserLogin, db: Session = Depends(get_db)):
  db_user = Auth.authenticate_user(db=db, email=form_data.username,password=form_data.password)
  if db_user is False:
    raise HTTPException(status_code=400, detail="Incorrect email or password")
  access_token = JwtAuth.create_access_token(data={"sub": db_user.email})
  return {"access_token": access_token, "token_type": "bearer"}


@app.get("/me/",response_model=User.UserResource)
async def current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
  return JwtAuth.get_current_user(db, token)
  return {"token": token}

#########################################################################################################3

#rota de teste na raiz
@app.get("/")
def read_root():
  return {"Hello": "World"}