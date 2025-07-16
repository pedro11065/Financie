from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError  # Import para capturar erros do SQLAlchemy
from sqlalchemy import update
from sqlalchemy import delete

from src.config.colors import *
from src.config.methods import *

import logging, traceback,datetime
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

from src.model.classes.liability import * 
from src.model.db.DbConnect import Db_connect
from src.model.classes.liability import table_liabilities

class Liabilities:

    def __init__(self):

        self.db = Db_connect()
        self.engine = create_engine(self.db.engine, echo=False)
        self.session = Session(self.engine)

        self.search = self.Search(self)
        self.create = self.Create(self)
        self.update = self.Update(self)
        self.delete = self.Delete(self)


# ==============================================================================
#region CREATE

    class Create: 

        def __init__(self, parent):        
            self.parent = parent
        
        def liability(self, liability_obj):

            try:
                
                self.parent.session.add(liability_obj.self_to_table())
                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + "Liability created successfully!" + Style.RESET_ALL)

                return True       
            
            except Exception as e:

                print(str(e))
                print(traceback.format_exc())
                print(Fore.RED + Style.BRIGHT + "Error reading or searching liability!" + Style.RESET_ALL)

                return False
            
            finally:
               
                self.parent.session.close() ; self.parent.engine.dispose()


# ==============================================================================
#region SEARCH

    class Search:
        
        def __init__(self, parent):
            # Establish a reference to the parent Db_user instance
            self.parent = parent

        def by_id(self, user_id, id):

            try:

                filter_data = {'user_id': user_id, 'id': id}
                filter_data = {key: value for (key, value) in filter_data.items() if value}

                search = (
                    self.parent.session.query(table_liabilities)
                    .filter_by(**filter_data)
                    .filter(table_liabilities.deleted_at.isnot(None))
                    .first()
                )

                print(green("Liability search by id ended successfully!"))

                liability = Liability(
                    id=str(search.id),
                    user_id=str(search.user_id),
                    name=search.name,
                    description=search.description,
                    category=search.category,
                    status=search.status,
                    location=search.location,
                    created_at=search.created_at,
                    updated_at=search.updated_at,
                    deleted_at=search.deleted_at
                )
                

                return liability

            except Exception as e:

                logging.error(str(e))
                print(traceback.format_exc())
                print(red("Error reading liability!"))

                return False
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()


        def by_user_id(self, user_id):
            try:
                search = self.parent.session.query(table_liabilities).filter_by(user_id=user_id).all()

                print(green("Liability search by user id ended successfully!"))

                if search:  
                    print(green(f"{len(search)} Liability(s) founded!"))

                    liabilities = []

                    for record in search:
                        
                        liability = Liability(
                            id=str(record.id),
                            user_id=str(record.user_id),
                            name=record.name,
                            description=record.description,
                            category=record.category,
                            status=record.status,
                            location=record.location,
                            created_at=record.created_at,
                            updated_at=record.updated_at,
                            deleted_at=record.deleted_at
                        )
                        liabilities.append(liability)

                    return liabilities 

                else:
                    print(red("Liability not founded."))
                    return []  

            except Exception as e:
                logging.error(str(e))
                print(traceback.format_exc())
                print(red("Error reading or searching liability!"))
                return False

            finally:
                self.parent.session.close()
                self.parent.engine.dispose()     


# ==============================================================================
#region UPDATE

    class Update:

        def __init__(self, parent):
            self.parent = parent

        def liability(self, user_id, id, column, value):

            try:

                sql1 = (
                    update(table_liabilities)
                    .where((table_liabilities.id == id) & (table_liabilities.user_id == user_id))
                    .values({column: value})
                )
                self.parent.session.execute(sql1)

                
                sql2 = (
                    update(table_liabilities)
                    .where((table_liabilities.id == id) & (table_liabilities.user_id == user_id))
                    .values({'updated_at': datetime.now()})
                )
                self.parent.session.execute(sql2)


                self.parent.session.commit()

                print(green(f"Liability {column} updated successfully!"))

                return True

            except SQLAlchemyError as e:
                
                print(traceback.format_exc())
                print(red("Error updating liability!"))
                print(e)

                return False

            finally:
                self.parent.session.close()
                self.parent.engine.dispose()


# ==============================================================================
#region DELETE

    class Delete:

        def __init__(self, parent):        
            self.parent = parent

        def liability(self, user_id, id):

            try:
                sql = (
                    update(table_liabilities)
                    .where((table_liabilities.id == id) & (table_liabilities.user_id == user_id))
                    .values(deleted_at=datetime.now())
                )

                result = self.parent.session.execute(sql)
                self.parent.session.commit()

                if result.rowcount > 0:
                    print(green("Liability deleted successfully!"))
                    return True

                print(red("Liability not found or not deleted."))
                return False
            
            except Exception as e:

                print(traceback.format_exc())
                print(red("Error deleting liability!"))

                return False
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()