import psycopg2, uuid
from colorama import Fore, Style

from settings.db import *

def db_search_user(user : object): # Cria um usuário usando as informações do user_info como parametro, todos os dados são temporários.
    
    print(Fore.CYAN + '[Banco de dados] ' + Style.RESET_ALL + 'Registrando novo usuário...')
    
    database = Db_connect 
    conn = database.make_connection
    cur = conn.cursor()
 
    cur.execute(f"SELECT * from users WHERE id = '{user.uuid}' or email = '{user.email}';")
    conn.commit()

    cur.close()
    conn.close()
