#!/usr/bin/python3
"""a script that prints the State object with the
name passed as argument from database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State

if __name__ == '__main__':
    """prints number of state object with name
    that is passed as argument
    """
    usr, pswd, dbname, sname = sys.argv[1:5]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pswd, dbname))

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == sname).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
