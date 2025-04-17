import uuid

class User:

    def __init__(self, fullname, cpf, email, password, birthday):

        self.uuid : str = str(uuid.uuid4())
        self.fullname : str = fullname
        self.cpf : str = cpf
        self.email : str = email
        self.password : str = password
        self.birthday : str = birthday
        
