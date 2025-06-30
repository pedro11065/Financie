from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError  # Import para capturar erros do SQLAlchemy
from sqlalchemy import update
from sqlalchemy import delete

from colorama import Fore, Style

import logging
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

from src.model.classes.user import * 
from src.model.db.DbConnect import Db_connect
from src.model.classes.user import table_users  # Certifique-se de importar table_users corretamente


class Users:

    def __init__(self):

        self.db = Db_connect()
        self.engine = create_engine(self.db.engine, echo=False)
        self.session = Session(self.engine)

        self.search = self.Search(self)
        self.create = self.Create(self)
        self.update = self.Update(self)
        self.delete = self.Delete(self)


# ==============================================================================

    class Create:

        def __init__(self, parent):        
            self.parent = parent
        
        def user(self, user_data):

            try:
                
                user_data.encrypt()
                self.parent.session.add(user_data.self_to_table())
                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + "User created successfully!" + Style.RESET_ALL)

                return True       
            
            except Exception as e:

                print(str(e.orig))

                print(Fore.RED + Style.BRIGHT + "Error reading or searching user!" + Style.RESET_ALL)

                return False
            
            finally:
               
                self.parent.session.close() ; self.parent.engine.dispose()


# ==============================================================================

    class Search:
        
        def __init__(self, parent):
            # Establish a reference to the parent Db_user instance
            self.parent = parent

        def by_id(self, id):

            try:

                search = self.parent.session.query(table_users).filter_by(id=id).first()

                print(Fore.GREEN + Style.BRIGHT + "User search by id ended successfully!" + Style.RESET_ALL)

                user = User(
                    id=str(search.id),
                    fullname=search.full_name,
                    cpf=search.cpf,
                    phone=search.phone,
                    email=search.email,
                    password=search.password,
                    birthday=search.birthday,
                    lgpd_consent=search.lgpd_consent,
                    created_at=search.created_at,
                    updated_at=search.updated_at,
                    deleted_at=search.deleted_at
                )
                
                user.decrypt()

                return user

            except Exception as e:

                logging.error(str(e))

                print(Fore.RED + Style.BRIGHT + "Error reading user!" + Style.RESET_ALL)

                return False
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()

        def by_email(self, email):
                
            try:

                search = self.parent.session.query(table_users).filter_by(email=email).first()

                print(Fore.GREEN + Style.BRIGHT + "User search by email ended successfully!" + Style.RESET_ALL)

                if search is not None: 

                    print(Fore.GREEN + Style.BRIGHT + "User founded!" + Style.RESET_ALL)

                    user = User(
                        id=str(search.id),
                        fullname=search.full_name,
                        cpf=search.cpf,
                        phone=search.phone,
                        email=search.email,
                        password=search.password_hash,
                        birthday=search.birthday,
                        lgpd_consent=search.lgpd_consent,
                        created_at=search.created_at,
                        updated_at=search.updated_at,
                        deleted_at=search.deleted_at
                    )

                    user.decrypt()

                    return user
                
                else: print(Fore.RED + Style.BRIGHT + "User not founded." + Style.RESET_ALL)

            except Exception as e:

                logging.error(str(e))

                print(Fore.RED + Style.BRIGHT + "Error reading or searching user!" + Style.RESET_ALL)

                return False      
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()            


# ==============================================================================

    class Update:

        def __init__(self, parent):
            self.parent = parent

        def user(self, id, column, data):

            try:
                
                sql = (
                    update(table_users)
                    .where(table_users.id == id)
                    .values({column: data})
                )

                self.parent.session.execute(sql)  
                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + f"User {column} updated successfully!" + Style.RESET_ALL)

                return True

            except SQLAlchemyError as e:
                
                logging.error(str(e))
                print(Fore.RED + Style.BRIGHT + "Error updating user!" + Style.RESET_ALL)
                print(e)

                return False

            finally:
                self.parent.session.close()
                self.parent.engine.dispose()


# ==============================================================================

    class Delete:

        def __init__(self, parent):        
            self.parent = parent

        def user(self, id):

            try:

                sql = (
                    delete(table_users)
                    .where(table_users.id == id)
                )

                self.parent.session.execute(sql)  
                self.parent.session.commit()


                print(Fore.GREEN + Style.BRIGHT + "User deleted successfully!" + Style.RESET_ALL)

                return True
            
            except Exception as e:

                logging.error(str(e.orig))

                print(Fore.RED + Style.BRIGHT + "Error deleting user!" + Style.RESET_ALL)

                return False
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()