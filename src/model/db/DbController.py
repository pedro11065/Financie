from src.model.db.tables.users import Users
from src.model.db.tables.assets import Assets
from src.model.db.tables.liabilities import Liabilities
from src.model.db.tables.transactions import Transactions

class Db:

    def __init__(self, type):
        
        if type == 'users':
            self.users : object = Users()

        if type == 'assets':
            self.assets: object = Assets()
       
        if type == 'liabilities':
            self.transactions: object = Liabilities()

        if type == 'transactions':
            self.transactions: object = Transactions()