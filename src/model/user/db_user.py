from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from colorama import Fore, Style

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

            print(Fore.GREEN + Style.BRIGHT + "User created successfully!" + Style.RESET_ALL)

            return True
        
        
        except Exception as e:

            logging.error(str(e))

            print(Fore.RED + Style.BRIGHT + "Error creating user!" + Style.RESET_ALL)

            return False
        
        finally:
            self.session.close() ; self.engine.dispose()

    def serch_by_id(self):

        try:

            user = self.session.query(table_users).filter_by(id=self.user.uuid).first()

            print(Fore.GREEN + Style.BRIGHT + "User read successfully!" + Style.RESET_ALL)

            return user


        except Exception as e:

            logging.error(str(e))

            print(Fore.RED + Style.BRIGHT + "Error reading user!" + Style.RESET_ALL)

            return False
        

        
        finally:
            self.session.close() ; self.engine.dispose()

    def serch_by_email(self):
            
            try:
    
                search = self.session.query(table_users).filter_by(email=self.user.email).first()
    
                print(Fore.GREEN + Style.BRIGHT + "User read successfully!" + Style.RESET_ALL)

    
                user = User(

                    fullname=search.fullname,
                    cpf=search.cpf,
                    phone=search.phone,
                    email=search.email,
                    password=search.password,
                    birthday=search.birthday
                    # lgpd_consent=search.lgpd_consent,
                    # created_at=search.created_at,
                    # updated_at=search.updated_at,
                    # deleted_at=search.deleted_at
                    )


                return user
    
    
            except Exception as e:
    
                logging.error(str(e))
    
                print(Fore.RED + Style.BRIGHT + "Error reading user!" + Style.RESET_ALL)
    
                return False
            
            
            finally:
                self.session.close() ; self.engine.dispose()            
   
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

            print(Fore.GREEN + Style.BRIGHT + "User updated successfully!" + Style.RESET_ALL)

            return True
        
        except Exception as e:

            logging.error(str(e.orig))

            print(Fore.RED + Style.BRIGHT + "Error updating user!" + Style.RESET_ALL)

            return False
        
        finally:
            self.session.close() ; self.engine.dispose()

    def delete(self):

        try:

            user = self.session.query(table_users).filter_by(id=self.user.uuid).first()
            user.deleted_at = datetime.now()

            self.session.commit()

            print(Fore.GREEN + Style.BRIGHT + "User deleted successfully!" + Style.RESET_ALL)

            return True
        
        except Exception as e:

            logging.error(str(e.orig))

            print(Fore.RED + Style.BRIGHT + "Error deleting user!" + Style.RESET_ALL)

            return False
        
        finally:
            self.session.close() ; self.engine.dispose()