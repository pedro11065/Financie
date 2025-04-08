class largura:

    def __init__(self, dados):
        self.meio : str = dados[0]
        self.valor : float = dados[1]
        self.fonte : str
        self.situacao : bool
        self.recomendacao : str
        self.nome : str = "largura"
        
    def verificar(self, dado):

        tabela = {
            "rampa": 50,
            "passarela": 70,
            "escada": 55    
        }

        #print(f"Verificando largura: {self.meio} - {self.valor}")

        min_largura = tabela[self.meio]

        if self.valor < min_largura:
            recomendacao = f"- A largura da {self.meio} deve ser maior que {min_largura} cm."
            self.situacao = False
            self.recomendacao = recomendacao
        
        else:
            recomendacao = f"- Nada Consta."
            self.situacao = True
            self.recomendacao = recomendacao
