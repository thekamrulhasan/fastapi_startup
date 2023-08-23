from sqlalchemy import Boolean, Column, Integer, String

from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=255), unique=True, index=True)
    full_name = Column(String(length=255))
    password = Column(String(length=100))
