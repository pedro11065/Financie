import psycopg2, uuid
from colorama import Fore, Style

from settings.db import *

def db_create_user(user : object): # Cria um usuário usando as informações do user_info como parametro, todos os dados são temporários.
    print(Fore.CYAN + '[Banco de dados] ' + Style.RESET_ALL + 'Registrando novo usuário...')
    
    database = Db_connect 
    conn = database.make_connection
    cur = conn.cursor()

    cur.execute(f"INSERT INTO users (id, fullname, email, password, birthday, cpf) VALUES ('{user.uuid}', '{user.fullname}', '{user.email}', '{user.password}', '{user.birthday}', '{user.cpf}');")
    conn.commit()

    cur.close()
    conn.close()

