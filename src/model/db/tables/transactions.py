from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError  # Import para capturar erros do SQLAlchemy
from sqlalchemy import update
from sqlalchemy import delete

from colorama import Fore, Style

import logging, traceback, datetime
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

from src.model.classes.transaction import * 
from src.model.db.DbConnect import Db_connect
from src.model.classes.transaction import table_transactions

class Transactions:

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
        
        def transaction(self, transaction_obj):

            try:
                
                self.parent.session.add(transaction_obj.self_to_table())
                self.parent.session.commit()

                print(Fore.GREEN + Style.BRIGHT + "Transaction created successfully!" + Style.RESET_ALL)

                return True       
            
            except Exception as e:

                print(str(e))
                print(traceback.format_exc())
                print(Fore.RED + Style.BRIGHT + "Error reading or searching transaction!" + Style.RESET_ALL)

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

                search = self.parent.session.query(table_transactions).filter_by(**filter_data).first()
                
                transaction = Transaction(

                    id=search.id,
                    user_id=search.user_id,
                    asset_id=search.asset_id,
                    liability_id=search.liability,
                    credit_card_id=search.credit_card_id,
                    statement_id=search.statement_id,
                    transaction_type=search.transaction_type,
                    payment_method=search.payment_method,
                    payment_status=search.payment_status,
                    currency=search.currency,
                    amount=search.amount,
                    created_at=search.created_at,
                    updated_at=search.updated_at,
                    deleted_at=search.deleted_at
                )
                
                print(Fore.GREEN + Style.BRIGHT + "Transaction search by id ended successfully!" + Style.RESET_ALL)
                
                return transaction

            except Exception as e:

                logging.error(str(e))
                print(traceback.format_exc())
                print(Fore.RED + Style.BRIGHT + "Error reading Transaction!" + Style.RESET_ALL)

                return False
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()


        def by_user_id(self, user_id):
            try:
                search = self.parent.session.query(table_transactions).filter_by(user_id=user_id).all()

                print(Fore.GREEN + Style.BRIGHT + "Transaction search by user id ended successfully!" + Style.RESET_ALL)

                if search:  
                    print(Fore.GREEN + Style.BRIGHT + f"{len(search)} Transaction(s) founded!" + Style.RESET_ALL)

                    transactions = []

                    for record in search:
                        
                        asset = Transaction(
                            id=record.id,
                            user_id=record.user_id,
                            asset_id=record.asset_id,
                            liability_id=record.liability_id,
                            credit_card_id=record.credit_card_id,
                            statement_id=record.statement_id,
                            transaction_type=record.transaction_type,
                            payment_method=record.payment_method,
                            payment_status=record.payment_status,
                            currency=record.currency,
                            amount=record.amount,
                            created_at=record.created_at,
                            updated_at=record.updated_at,
                            deleted_at=record.deleted_at
                        )
                        transactions.append(asset)

                    return transactions

                else:
                    print(Fore.RED + Style.BRIGHT + "Transaction not founded." + Style.RESET_ALL)
                    return []  

            except Exception as e:
                logging.error(str(e))
                print(traceback.format_exc())
                print(Fore.RED + Style.BRIGHT + "Error reading or searching transaction!" + Style.RESET_ALL)
                return False

            finally:
                self.parent.session.close()
                self.parent.engine.dispose()     


# ==============================================================================

    class Update:

        def __init__(self, parent):
            self.parent = parent

        def transaction(self, user_id, id, column, value):

            try:

                sql1 = (
                    update(table_transactions)
                    .where((table_transactions.id == id) & (table_transactions.user_id == user_id))
                    .values({column: value})
                )
                self.parent.session.execute(sql1)

                
                sql2 = (
                    update(table_transactions)
                    .where((table_transactions.id == id) & (table_transactions.user_id == user_id))
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

        def transaction(self, user_id, id):

            try:

                sql = (
                    delete(table_transactions)
                    .where((table_transactions.id == id) & (table_transactions.user_id == user_id))
                )

                self.parent.session.execute(sql)
                self.parent.session.commit()


                print(Fore.GREEN + Style.BRIGHT + "Transaction deleted successfully!" + Style.RESET_ALL)

                return True
            
            except Exception as e:

                logging.error(str(e.orig))

                print(Fore.RED + Style.BRIGHT + "Error deleting transaction!" + Style.RESET_ALL)

                return False
            
            finally:
                self.parent.session.close() ; self.parent.engine.dispose()