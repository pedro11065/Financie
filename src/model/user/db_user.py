from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import logging
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

from src.model.user.user import * 
from src.settings.db import Db_connect


class Db_user:

    def __init__(self, user):

        self.user = user
        self.db = Db_connect()
        self.engine = create_engine(self.db.engine, echo=False)
        self.session = Session(self.engine)


    def create(self):

        try:

            self.session.add(self.user.to_table)
            self.session.commit()
            return True
        
        except Exception as e:

            logging.error(str(e.orig))
            return False
        
        finally:
            self.session.close()
            self.engine.dispose()

    def read(self):

        try:

            user = self.session.query(table_users).filter_by(id=self.user.uuid).first()
            return user
        
        except Exception as e:

            logging.error(str(e.orig))
            return False
        
        finally:
            self.session.close()
            self.engine.dispose()
   
    def update(self):

        try:

            user = self.session.query(table_users).filter_by(id=self.user.uuid).first()
            user.fullname = self.user.fullname
            user.cpf = self.user.cpf
            user.phone = self.user.phone
            user.email = self.user.email
            user.password = self.user.password
            user.birthday = self.user.birthday
            user.updated_at = datetime.now()

            self.session.commit()
            return True
        
        except Exception as e:

            logging.error(str(e.orig))
            return False
        
        finally:
            self.session.close()
            self.engine.dispose()

    def delete(self):

        try:

            user = self.session.query(table_users).filter_by(id=self.user.uuid).first()
            user.deleted_at = datetime.now()

            self.session.commit()
            return True
        
        except Exception as e:

            logging.error(str(e.orig))
            return False
        
        finally:
            self.session.close()
            self.engine.dispose()