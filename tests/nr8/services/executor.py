from classes.rampa import *
from classes.medidas import *

dados = [8, "RA01","rampa", 10.0, 70.0, 200.0]

# rampa = rampa(dados)
# rampa.verificar()

# print(f'\n{rampa.angulo.nome}\n')
# print(rampa.angulo.situacao)
# print(rampa.angulo.recomendacao)

# print(f'\n{rampa.largura.nome}\n')
# print(rampa.largura.situacao)
# print(rampa.largura.recomendacao)

# print(f'\n{rampa.comprimento.nome}\n')
# print(rampa.comprimento.situacao)
# print(rampa.comprimento.recomendacao)


class executor:
    def __init__(self, nr, tipo, dados):
        self.nr = nr
        self.tipo = tipo
        self.dados = dados

    def executar(self):
        if self.tipo == 'rampa':
            rampa = rampa(self.dados)
            rampa.verificar()
            return rampa
        elif self.tipo == 'medidas':
            medidas = medidas(self.dados)
            medidas.verificar()
            return medidas
        else:
            raise ValueError("Tipo inválido")