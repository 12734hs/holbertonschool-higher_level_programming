#!/usr/bin/python3
"""HIIIIIIIIIIIIII"""
from sqlalchemy import Сolumn, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'state'
    id = Сolumn(Integer, primary_key=True, nullable=False)
    name = Сolumn(String(128))
