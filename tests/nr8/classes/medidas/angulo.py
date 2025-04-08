class angulo:

    def __init__(self, dados):
        self.meio : str = dados[0]
        self.valor : float = dados[1]
        self.fonte : str
        self.nr : int
        self.situacao : bool
        self.recomendacao : str
        self.nome : str = "angulo"
        

    def verificar(self, dado):

        tabela = {
            "rampa": [-20, 20],
            "passarela": [-20, 20],
            "escada": [20, 45]
        }

        #print(f"Verificando angulo: {self.meio} - {self.valor}")

        try:
            min_largura = tabela[self.meio][0]
            max_largura = tabela[self.meio][1]
        except:
            False, 'Nada consta.'

        if self.valor < min_largura:
            recomendacao = f"- O angulo de inclinação da rampa {self.meio} deve ser maior que {min_largura} graus."
            self.situacao = False
            self.recomendacao = recomendacao

        elif self.valor > max_largura:
            recomendacao = f"- O angulo de inclinação da rampa {self.meio} deve ser menor que {max_largura} graus."
            self.situacao = False
            self.recomendacao = recomendacao

        else:
            recomendacao = f"- Nada Consta."
            self.situacao = True
            self.recomendacao = recomendacao

