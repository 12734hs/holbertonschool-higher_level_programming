#!/usr/bin/python3
"""HIIIIIIIIIIIIII"""
from sqlalchemy import column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'state'
    id = column(Integer, primary_key=True, nullable=False)
    name = column(String(128))
