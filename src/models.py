from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    address = relationship("Address", back_populates="owner")

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(String)
    lattitude = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="address")