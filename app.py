from src.model.user.db_user import Db_user
from src.model.user.user import User

import bcrypt, uuid

user = User(fullname="Pedro Henrique", 
            cpf="50774811803", 
            email="pedrohenriquesilvaquixabeira@gmail.com",
            phone="13974256075",
            password="32372403", 
            birthday="2006-03-13")

db_user = Db_user(user)
#db_user.create()

user = db_user.serch_by_email()
print(user.fullname)
print(user.email)

