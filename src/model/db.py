from src.model.user.users import Users

class Db:

    def __init__(self, type):
        
        if type == 'users':
            self.users : object = Users()