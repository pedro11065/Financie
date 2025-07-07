from src.model.db.tables.users import Users
from src.model.db.tables.assets import Assets
from src.model.db.tables.liabilities import Liabilities
from src.model.db.tables.transactions import Transactions

class Db:

    def __init__(self):
        
        self.users : object = Users()

        self.assets: object = Assets()

        self.liabilities: object = Liabilities()

        self.transactions: object = Transactions()