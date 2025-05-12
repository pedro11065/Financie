import os, json
from sqlalchemy.orm import DeclarativeBase

import logging
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

class Db_connect:

    def __init__(self):

        self.check = False
        self.host = ""
        self.database = ""
        self.user = ""
        self.password = ""
        self.engine = ""

        self.read_db_info()



    def read_db_info(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'db.json') 

        try:
            with open(file_path, "r") as file:
                config = json.load(file)
            
            self.host = config['db']['host']
            self.database = config['db']['database']
            self.user = config['db']['user']
            self.password = config['db']['password']

            self.check = True

            #postgresql://user:password@localhost:5432/dbname
            self.engine=f"postgresql://{self.user}:{self.password}@{self.host}:5432/{self.database}"
        
        except Exception as error:
            print(f"Erro: {error}")
            self.check = False
        
class Base(DeclarativeBase):
    pass
