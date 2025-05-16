from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from colorama import Fore, Style

import logging
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

from src.model.user.user import * 
from src.settings.db import Db_connect


class Users:

    def __init__(self, user):

        self.user = user
        self.db = Db_connect()
        self.engine = create_engine(self.db.engine, echo=False)
        self.session = Session(self.engine)

        self.search = self.Search(self)
        self.create = self.Create(self, self.user)


    class Create:

        def __init__(self, parent, user_data):        
            self.parent = parent
            self.user_data = user_data
        
        def user(self):

            try:
                
                self.parent.user.encrypt()
                self.parent.session.add(self.user_data.self_to_table())
                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + "User created successfully!" + Style.RESET_ALL)

                return True       
            
            except Exception as e:

                logging.error(str(e))

                print(Fore.RED + Style.BRIGHT + "Error creating user!" + Style.RESET_ALL)

                return False
            
            finally:
               
                self.parent.session.close() ; self.parent.engine.dispose()

    class Search:
        
        def __init__(self, parent):
            # Establish a reference to the parent Db_user instance
            self.parent = parent

        def by_id(self):

            try:

                search = self.parent.session.query(table_users).filter_by(id=self.parent.user.uuid).first()

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
                
                user.decrypt()

                return user

            except Exception as e:

                logging.error(str(e))

                print(Fore.RED + Style.BRIGHT + "Error reading user!" + Style.RESET_ALL)

                return False
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()

        def by_email(self):
                
            try:

                search = self.parent.session.query(table_users).filter_by(email=self.parent.user.email).first()

                print(Fore.GREEN + Style.BRIGHT + "User search ended successfully!" + Style.RESET_ALL)


                user:object = User(

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


                user.decrypt()

                return user

            except Exception as e:

                logging.error(str(e))

                print(Fore.RED + Style.BRIGHT + "Error reading user!" + Style.RESET_ALL)

                return False      
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()            


    def update(self):

        try:

            self.user.encrypt()

            self.session.query(table_users).filter_by(id=self.user.uuid).first()
            self.session._update_impl(self.user.to_table)
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
            self.session.delete(self.user.to_table)

            self.session.commit()

            print(Fore.GREEN + Style.BRIGHT + "User deleted successfully!" + Style.RESET_ALL)

            return True
        
        except Exception as e:

            logging.error(str(e.orig))

            print(Fore.RED + Style.BRIGHT + "Error deleting user!" + Style.RESET_ALL)

            return False
        
        finally:
            self.session.close() ; self.engine.dispose()