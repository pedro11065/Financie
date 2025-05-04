import psycopg2, uuid
from colorama import Fore, Style

from settings.db import *

def db_create_user(user : object): # Cria um usuário usando as informações do user_info como parametro, todos os dados são temporários.
    print(Fore.CYAN + '[Banco de dados] ' + Style.RESET_ALL + 'Registrando novo usuário...')
    
    database = Db_connect 
    conn = database.make_connection
    cur = conn.cursor()

    cur.execute("UPDATE table_users SET fullname = %s, user_cpf = %s, email = %s, password = %s WHERE id = %s;", (user.fullname, user.cpf, user.email, user.password, user.uuid))
    conn.commit()

    cur.close()
    conn.close()
