"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

from time import sleep


class Retângulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarLado(self, base, altura):
        self.base = base
        self.altura = altura

    def retornarLado(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2*(self.base + self.altura)


print("--- CALCULADOR DE PISOS ---")
b = int(input("Digite a base do retângulo: "))
a = int(input("Digite a altura do retângulo: "))
r = Retângulo(b, a)
sleep(1)
print(f"Área: {r.area()}m²")
sleep(1)
print(f"Perimetro: {r.perimetro()}m")
'''r.mudarLado(5, 10)
print("Mudando valor da base e altura...")
sleep(2)
print(f"Área: {r.area()}m²")
print(f"Perimetro: {r.perimetro()}m")'''
c2 = r.area() * 10000
p = c2 / 3600
sleep(1)
print("Calculando pisos...")
sleep(2)
print(
    f"Considerando um porcelanato 60x60cm, será necessário {p:.0f} pisos para a construção.")
