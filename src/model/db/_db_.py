from src.model.tables.users import Users
from src.model.tables.assets import Assets

class Db:

    def __init__(self, type):
        
        if type == 'users':
            self.users : object = Users()

        if type == 'assets':
            self.assets: object = Assets()