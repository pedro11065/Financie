from src.model.db import Db
from src.model.user.user import User

import bcrypt, uuid

data = User(fullname="Pedro Henrique", 
            cpf="50774811803", 
            email="pedrohenriquesilvaquixabeira@gmail.com",
            phone="13974256075",
            password="32372403", 
            birthday="2006-03-13")


type = "user"
db = Db(type, data)

db.users.create.user()

user = db.users.search.by_email()
print(user.__dict__)



