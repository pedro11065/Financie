from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import logging

from src.model.user.user import * 
from src.settings.db import Db_connect



def db_create_user(user):

    db = Db_connect()

    engine = create_engine(db.engine, echo=True)
    session = Session(engine)

    session.add(user.to_table)
    session.commit()
    

