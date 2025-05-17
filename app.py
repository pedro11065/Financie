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

#db.users.create.user(user)

user = db.users.search.by_email(user.email)
os.system("pause")

# user = db.users.search.by_id(user.id)
# os.system("pause")


id = user.id
column = ""
data = "Luiz Guilherme"


update = db.users.update.user(id, column, data)
print(update)





