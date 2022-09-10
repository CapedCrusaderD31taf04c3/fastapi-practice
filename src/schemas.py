from typing import List
from pydantic import BaseModel

class _AddressBase(BaseModel):
    longitude: str
    lattitude: str

class AddressCreate(_AddressBase):
    pass

class Address(_AddressBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class _UserBase(BaseModel):
    email: str

class UserCreate(_UserBase):
    password: str

class User(_UserBase):
    id: int
    address: List[Address] = []

    class Config:
        orm_mode = True