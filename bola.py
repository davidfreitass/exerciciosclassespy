class Bola:
    def __init__(self, cor: str, circunferencia: int, material: str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostraCor(self):
        return self.cor

    def trocaCor(self, cor):
        self.cor = cor
        return self.cor


b = Bola('branca', 15, 'couro')
print("Cor: ", b.mostraCor())
b.trocaCor('azul')
print("Nova cor: ", b.mostraCor())
