from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError  # Import para capturar erros do SQLAlchemy
from sqlalchemy import update
from sqlalchemy import delete

from colorama import Fore, Style

import logging, traceback
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
        
        def user(self, user_obj):

            try:
                
                user_obj.encrypt()
                self.parent.session.add(user_obj.self_to_table())
                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + "User created successfully!" + Style.RESET_ALL)

                return True, "User created successfully!"
            
            except Exception as e:

                if hasattr(e, 'orig') and 'already exists.' in str(e.orig):
                    print(Fore.RED + Style.BRIGHT + "User already exists!" + Style.RESET_ALL)
                    return False, "User already exists!"
                
                else:
                    print(Fore.RED + Style.BRIGHT + "Error creating user!" + Style.RESET_ALL)
                    return False, "Error creating user!"
                
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

                user = User(
                    id=str(search.id),
                    fullname=search.full_name,
                    cpf=search.cpf,
                    phone=search.phone,
                    email=search.email,
                    password_hash=search.password_hash,
                    birthday=search.birthday,
                    lgpd_consent=search.lgpd_consent,
                    created_at=search.created_at,
                    updated_at=search.updated_at,
                    deleted_at=search.deleted_at
                )
                
                user.decrypt()

                print(Fore.GREEN + Style.BRIGHT + "User search by id ended successfully!" + Style.RESET_ALL)

                return user, "User search by id ended successfully!"

            except Exception as e:

                logging.error(str(e))
                print(traceback.format_exc())
                print(Fore.RED + Style.BRIGHT + "Error searching user!" + Style.RESET_ALL)

                return False, "Error searching user!"
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()

        def by_email(self, email):
                
            try:

                search = self.parent.session.query(table_users).filter_by(email=email).first()

                if search is not None: 


                    user = User(
                        id=str(search.id),
                        fullname=search.full_name,
                        cpf=search.cpf,
                        phone=search.phone,
                        email=search.email,
                        password_hash=search.password_hash,
                        birthday=search.birthday,
                        lgpd_consent=search.lgpd_consent,
                        created_at=search.created_at,
                        updated_at=search.updated_at,
                        deleted_at=search.deleted_at
                    )

                    user.decrypt()

                    print(Fore.GREEN + Style.BRIGHT + "User founded!" + Style.RESET_ALL)

                    return user, "User founded!"
            
                print(Fore.RED + Style.BRIGHT + "User not founded." + Style.RESET_ALL)
                return False, "User not founded!"


            except Exception as e:

                logging.error(str(e))
                print(traceback.format_exc())
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


        #--------------------------------------------------------------------


        def balance(self, user_id, value, operation):

            try:

                if operation == "sum":
                
                    sql = (
                        update(table_users)
                        .where(table_users.id == user_id)
                        .values(balance=table_users.balance + value)
                    )


                elif operation == "deduct": #EU SEI que um else é mais que o suficiente, é só para faciliar o entendimento

                    sql = (
                        update(table_users)
                        .where(table_users.id == user_id)
                        .values(balance=table_users.balance - value)
                    )


                self.parent.session.execute(sql)  
                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + f"User balance updated successfully!" + Style.RESET_ALL)

                return True

            except SQLAlchemyError as e:
                
                logging.error(str(e))
                print(Fore.RED + Style.BRIGHT + "Error updating balance!" + Style.RESET_ALL)
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


# ==============================================================================

