from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from db.database import SessionLocal
from models.user import User
from schemas.user import UserCreate

router =APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register (user:UserCreate,db:session=Depends(get_db)):
    new_user=User(name=user.name,
              email=user.email,
              password=user.password,
              role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message":" User Created Successfully"}