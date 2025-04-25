import psycopg2, uuid
from colorama import Fore, Style

from settings.db import *

def db_delete_user(user : object): # Cria um usuário usando as informações do user_info como parametro, todos os dados são temporários.
   
    print(Fore.CYAN + '[Banco de dados] ' + Style.RESET_ALL + 'deletando usuário...')
    
    database = Db_connect 
    conn = database.make_connection
    cur = conn.cursor()

    cur.execute(f"DELETE FROM users WHERE cpf = '{user.cpf}' or id = '{user.uuid}';")
    conn.commit()

    cur.close()
    conn.close()
