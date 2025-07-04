from src.model.db.DbController import Db
from src.model.settings.auth.auth0 import Auth0

from flask_login import login_manager

@login_manager.user_loader
def load_user(user):

    payload = {"id" : user.id, 
        "email": user.email, 
        "fullname": user.fullname, 
        "phone": user.phone, 
        "birthday": user.birthday}
    
    auth = Auth0()
    token = auth.encrypt(payload)

    return token

