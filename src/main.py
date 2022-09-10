from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import services
import schemas
import utils

app = FastAPI()

services.create_database()

@app.post("/users/", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate, db: Session = Depends(services.get_db)):
    db_user = services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Email is Already in Use"
        )
    return services.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 5,
    db: Session = Depends(services.get_db)):
    users = services.get_users(db=db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(services.get_db)):
    db_user = services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="User Does not Exist"
        )
    return db_user

@app.post("/users/{user_id}/address/", response_model=schemas.Address)
def create_address(
    user_id: int,
    address: schemas.AddressCreate,
    db: Session = Depends(services.get_db)):
    if not utils.validate_longitude_and_lattitude(
        longitude=address.longitude, 
        lattitude=address.lattitude
        ):
        raise HTTPException(
            status_code=400, detail="Longitude or Lattitude is Invalid"
        )
    db_user = services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="User Does not Exist"
        )
    return services.create_address(db=db, address=address, user_id=user_id)

@app.get("/address/", response_model=List[schemas.Address])
def read_addresses(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(services.get_db)):
    addresses = services.get_addresses(db=db, skip=skip, limit=limit)
    return addresses

@app.get("/address/{address_id}", response_model=schemas.Address)
def read_address(address_id: int, db: Session = Depends(services.get_db)):
    address = services.get_address(db=db, address_id=address_id)
    if address is None:
        raise HTTPException(
            status_code=404, detail="Address Does not Exist"
        )
    return address

@app.delete("/address/{address_id}")
def delete_address(address_id: int, db: Session = Depends(services.get_db)):
    count = services.delete_address(db=db, address_id=address_id)
    return {
        "message": f"Deleted: {address_id}",
        "count" : count
        }

@app.put("/address/{address_id}", response_model=schemas.Address)
def update_address(
    address_id: int,
    address: schemas.AddressCreate,
    db: Session = Depends(services.get_db)):
    if not utils.validate_longitude_and_lattitude(
        longitude=address.longitude, 
        lattitude=address.lattitude
        ):
        raise HTTPException(
            status_code=400, detail="Longitude or Lattitude is Invalid"
        )
    return services.update_address(db=db, address=address, address_id=address_id)