from src.model.db import Db
from src.model.user.user import User

import os


user = User(fullname="Pedro Henrique", 
            cpf="50774811803", 
            email="pedrohenriquesilvaquixabeira@gmail.com",
            phone="13974256075",
            password="32372403", 
            birthday="2006-03-13")


table = "users"
db = Db(table)

db.users.create.user(user)

user = db.users.search.by_email(user.email)
user = db.users.search.by_id(user.id)

id = user.id ; column = "fullname" ;data = "Pedro Henrique Silva Quixabeira"
update = db.users.update.user(id, column, data)

delete = db.users.delete.user(id)








