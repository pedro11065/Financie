from src.model.db import Db
from src.model.user.user import User

import os

from src import *
from flask_cors import CORS
from flask import render_template

app = create_app()
CORS(app)  # O CORS é um sistema de segurança das requisições HTTP que verifica o método da API antes de chamá-lo.
app.app_context().push()
 
@app.errorhandler(404) # Manipulador para o erro 404
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(403) # Manipulador para o erro 403
def page_permission(e):
    return render_template('errors/403.html'), 403

if __name__ == '__main__':
    # Apenas irá rodar o aplicativo caso você inicie o arquivo main. 
    # Se não houvesse essa verificação, até mesmo uma importação desse arquivo iria rodar o programa.
    app.run(debug=True) #Responsável por iniciar o servidor web. O debug faz com que a cada alteração no código, o servidor web irá automaticamente reiniciar.
















