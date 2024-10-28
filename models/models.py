from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SignZodiac(Base):
    __tablename__ = 'signzodiac'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    sign = Column(String)
