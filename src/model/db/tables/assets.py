from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError  # Import para capturar erros do SQLAlchemy
from sqlalchemy import update
from sqlalchemy import delete

from colorama import Fore, Style

import logging, traceback,datetime
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

from src.model.classes.asset import * 
from src.model.db.DbConnect import Db_connect
from src.model.classes.asset import table_assets # Certifique-se de importar table_users corretamente


class Assets:

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
        
        def asset(self, asset_obj):

            try:
                
                self.parent.session.add(asset_obj.self_to_table())
                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + "Asset created successfully!" + Style.RESET_ALL)

                return True       
            
            except Exception as e:

                print(str(e))
                print(traceback.format_exc())
                print(Fore.RED + Style.BRIGHT + "Error reading or searching Asset!" + Style.RESET_ALL)

                return False
            
            finally:
               
                self.parent.session.close() ; self.parent.engine.dispose()


# ==============================================================================

    class Search:
        
        def __init__(self, parent):
            # Establish a reference to the parent Db_user instance
            self.parent = parent

        def by_id(self, user_id, id):

            try:

                filter_data = {'user_id': user_id, 'id': id}
                filter_data = {key: value for (key, value) in filter_data.items() if value}

                search = self.parent.session.query(table_assets).filter_by(**filter_data).first()
                
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
                
                print(Fore.GREEN + Style.BRIGHT + "Asset search by id ended successfully!" + Style.RESET_ALL)
                
                return asset

            except Exception as e:

                logging.error(str(e))
                print(traceback.format_exc())
                print(Fore.RED + Style.BRIGHT + "Error reading asset!" + Style.RESET_ALL)

                return False
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()


        def by_user_id(self, user_id):
            try:
                search = self.parent.session.query(table_assets).filter_by(user_id=user_id).all()

                print(Fore.GREEN + Style.BRIGHT + "Asset search by user id ended successfully!" + Style.RESET_ALL)

                if search:  
                    print(Fore.GREEN + Style.BRIGHT + f"{len(search)} Asset(s) founded!" + Style.RESET_ALL)

                    assets = []

                    for record in search:
                        
                        asset = Asset(
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
                        assets.append(asset)

                    return assets 

                else:
                    print(Fore.RED + Style.BRIGHT + "Asset not founded." + Style.RESET_ALL)
                    return []  

            except Exception as e:
                logging.error(str(e))
                print(traceback.format_exc())
                print(Fore.RED + Style.BRIGHT + "Error reading or searching asset!" + Style.RESET_ALL)
                return False

            finally:
                self.parent.session.close()
                self.parent.engine.dispose()     


# ==============================================================================

    class Update:

        def __init__(self, parent):
            self.parent = parent

        def asset(self, user_id, id, column, value):

            try:

                sql1 = (
                    update(table_assets)
                    .where((table_assets.id == id) & (table_assets.user_id == user_id))
                    .values({column: value})
                )
                self.parent.session.execute(sql1)

                
                sql2 = (
                    update(table_assets)
                    .where((table_assets.id == id) & (table_assets.user_id == user_id))
                    .values({'updated_at': datetime.now()})
                )
                self.parent.session.execute(sql2)


                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + f"Asset {column} updated successfully!" + Style.RESET_ALL)

                return True

            except SQLAlchemyError as e:
                
                logging.error(str(e))
                print(traceback.format_exc())
                print(Fore.RED + Style.BRIGHT + "Error updating asset!" + Style.RESET_ALL)
                print(e)

                return False

            finally:
                self.parent.session.close()
                self.parent.engine.dispose()


# ==============================================================================

    class Delete:

        def __init__(self, parent):        
            self.parent = parent

        def asset(self, user_id, id):

            try:

                sql = (
                    delete(table_assets)
                    .where((table_assets.id == id) & (table_assets.user_id == user_id))
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