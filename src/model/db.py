from src.model.user.users import Users
from src.model.asset.assets import Assets

class Db:

    def __init__(self, type):
        
        if type == 'users':
            self.users : object = Users()

        if type == 'assets':
            self.assets: object = Assets()