from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError  # Import para capturar erros do SQLAlchemy
from sqlalchemy import update
from sqlalchemy import delete

from colorama import Fore, Style

import logging, traceback
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

from src.model.asset.asset import * 
from src.settings.db.db import Db_connect
from src.model.asset.asset import table_assets # Certifique-se de importar table_users corretamente


class Assets:

    def __init__(self):

        self.db = Db_connect()
        self.engine = create_engine(self.db.engine, echo=False)
        self.session = Session(self.engine)

        self.search = self.Search(self)
        self.create = self.Create(self)
        self.update = self.Update(self)
        self.delete = self.Delete(self)


    class Create:

        def __init__(self, parent):        
            self.parent = parent
        
        def asset(self, asset_data):

            try:
                
                self.parent.session.add(asset_data.self_to_table())
                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + "Asset created successfully!" + Style.RESET_ALL)

                return True       
            
            except Exception as e:

                print(str(e))

                print(Fore.RED + Style.BRIGHT + "Error reading or searching Asset!" + Style.RESET_ALL)

                return False
            
            finally:
               
                self.parent.session.close() ; self.parent.engine.dispose()

    class Search:
        
        def __init__(self, parent):
            # Establish a reference to the parent Db_user instance
            self.parent = parent

        def by_id(self, id):

            try:

                search = self.parent.session.query(table_assets).filter_by(id=id).first()

                print(Fore.GREEN + Style.BRIGHT + "Asset search by id ended successfully!" + Style.RESET_ALL)

                asset = Asset(
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
                

                return asset

            except Exception as e:

                logging.error(str(e))

                print(Fore.RED + Style.BRIGHT + "Error reading asset!" + Style.RESET_ALL)

                return False
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()

        def by_user_id(self, user_id):
                
            try:

                search = self.parent.session.query(table_assets).filter_by(user_id=user_id).first()

                print(Fore.GREEN + Style.BRIGHT + "Asset search by user id ended successfully!" + Style.RESET_ALL)

                if search is not None: 

                    print(Fore.GREEN + Style.BRIGHT + "Asset founded!" + Style.RESET_ALL)

                    asset = Asset(
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
                    

                    return asset
                
                else: print(Fore.RED + Style.BRIGHT + "Asset not founded." + Style.RESET_ALL)

            except Exception as e:

                logging.error(str(e))

                print(Fore.RED + Style.BRIGHT + "Error reading or searching asset!" + Style.RESET_ALL)

                return False      
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()            


    class Update:

        def __init__(self, parent):
            self.parent = parent

        def asset(self, id, column, data):

            try:
                
                sql = (
                    update(table_assets)
                    .where(table_assets.id == id)
                    .values({column: data})
                )

                self.parent.session.execute(sql)  
                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + f"Asset {column} updated successfully!" + Style.RESET_ALL)

                return True

            except SQLAlchemyError as e:
                
                logging.error(str(e))
                print(Fore.RED + Style.BRIGHT + "Error updating asset!" + Style.RESET_ALL)
                print(e)

                return False

            finally:
                self.parent.session.close()
                self.parent.engine.dispose()


    class Delete:

        def __init__(self, parent):        
            self.parent = parent

        def asset(self, id):

            try:

                sql = (
                    delete(table_assets)
                    .where(table_assets.id == id)
                )

                self.parent.session.execute(sql)  
                self.parent.session.commit()


                print(Fore.GREEN + Style.BRIGHT + "Asset deleted successfully!" + Style.RESET_ALL)

                return True
            
            except Exception as e:

                logging.error(str(e.orig))

                print(Fore.RED + Style.BRIGHT + "Error deleting asset!" + Style.RESET_ALL)

                return False
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()