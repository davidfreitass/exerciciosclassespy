from time import sleep


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, lado):
        self.lado = lado
        return self.lado

    def area(self):
        return self.lado * self.lado


q = Quadrado(10)
print("Lado: ", q.lado)
print(f"Área: {q.area()}m²")
print("Mudando lado...")
sleep(2)
q.mudarLado(5)
print("Novo Lado: ", q.lado)
print("Calculando nova área...")
sleep(2)
print(f"Área: {q.area()}m²")
