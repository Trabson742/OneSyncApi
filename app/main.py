from typing import Union, Annotated
from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .Tables import Users
from .Actions import Auth 
from .Schemas import User
# from . import Actions, Models, Schemas
from .database import SessionLocal, engine, Base
from uuid import uuid4


Base.metadata.create_all(engine)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "teste"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})
  rand_token = uuid4()
  # encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  # access_token = manager.create_access_token(data={"sub": email})
  return {"access_token": rand_token}

# Dependency
def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
  db_user = Auth.get_user_by_email(db, email=form_data.username)
  if db_user is None or db_user.hashed_password != (form_data.password+"notreallyhashed"):
    raise HTTPException(status_code=400, detail="Incorrect email or password")
  access_token = create_access_token(data={"sub": form_data.username})
  return {"access_token": access_token, "token_type": "bearer"}


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
  return {"token": token}

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


