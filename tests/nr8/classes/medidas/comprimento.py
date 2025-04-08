class comprimento:

    def __init__(self, dados):
        self.meio : str = dados[0]
        self.valor : float = dados[1]
        self.recomendacao : str
        self.situacao : bool
        self.nome : str = "comprimento"

    def verificar(self, dado):
        #print(f"Verificando comprimento: Nada a verificar!")
        recomendacao = f" - Nada consta."
        self.situacao = True
        self.recomendacao = recomendacao