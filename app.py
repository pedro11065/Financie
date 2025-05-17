from src.model.db import Db
from src.model.user.user import User


data = User(fullname="Pedro Henrique", 
            cpf="50774811803", 
            email="pedrohenriquesilvaquixabeira@gmail.com",
            phone="13974256075",
            password="32372403", 
            birthday="2006-03-13")


table = "users"
db = Db(table)

#db.users.create.user()

user = db.users.search.by_email(data)

#update = db.users.update.user()
print(user.__dict__)



