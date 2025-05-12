from src.model.user.CreateUser import db_create_user
from src.model.user.user import User

user = User(fullname="Pedro Henrique", 
            cpf="50774811803", 
            email="pedrohenriquesilvaquixabeira@gmail.com", 
            password="32372403", 
            birthday="2006-03-13")

db_create_user(user)