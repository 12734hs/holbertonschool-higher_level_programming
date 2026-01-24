#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """EEEEEEEEVANGAT"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))
