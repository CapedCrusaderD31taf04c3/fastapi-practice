from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine, Base

def create_database():
    return Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    password = user.password
    db_user = models.User(email=user.email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_addresses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Address).offset(skip).limit(limit).all()

def create_address(db: Session, address: schemas.AddressCreate, user_id: int):
    address = models.Address(**address.dict(), user_id=user_id)
    db.add(address)
    db.commit()
    db.refresh(address)
    return address

def get_address(db: Session, address_id: int):
    return db.query(models.Address).filter(models.Address.id == address_id).first()

def delete_address(db: Session, address_id: int):
    count = db.query(models.Address).filter(models.Address.id == address_id).delete()
    db.commit()
    return count

def update_address(db: Session, address_id: int, address: schemas.AddressCreate):
    db_address = get_address(db=db, address_id=address_id)
    db_address.longitude = address.longitude
    db_address.lattitude = address.lattitude
    db.commit()
    db.refresh(db_address)
    return db_address