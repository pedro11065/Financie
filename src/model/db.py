from src.model.user.users import Users

class Db:

    def __init__(self, type, data):
        
        if type == 'user':
            self.users : object = Users(data)