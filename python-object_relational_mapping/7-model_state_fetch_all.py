#!/usr/bin/python3
"""BArcelona Visca"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
  """16-7"""
  engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

  Session = sessionmaker(bind=engine)
  session = Session()

  states = session.query(State).order_by(state.id).all()
  for i in states:
    print("{}: {}".format(i.id, state.name)

  session.close()
