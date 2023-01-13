"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""
from time import sleep


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhercer(self, env):
        return self.idade + env

    def engordar(self, eng):
        return self.peso + eng

    def emagrecer(self, ema):
        return self.peso - ema

    def crescer(self, cre):
        return self.altura + cre


p = Pessoa("José", 15, 72, 165)
print(f"""Características de {p.nome}:
==============
Nome: {p.nome}
Idade: {p.idade} anos
Peso: {p.peso} kg
Altura: {p.altura} cm
==============""")
sleep(2)
while True:
    x = int(input(f"""O que deseja fazer com {p.nome}?
    [1] Envelhercer
    [2] Engordar
    [3] Emagrecer
    [4] Crescer
    Ou digite qualquer número para SAIR!
    Escolha: """))
    if x == 1:
        i = int(input(f"Deseja envelhercer {p.nome} em quantos anos? "))
        p.idade += i
        print("Atualizando...")
        sleep(1)
        print('-' * 30)
        print(f"{p.nome} agora tem {p.idade} anos!")
        if p.idade <= 21:
            p.altura = p.altura + (5 * i)
            print(f"{p.nome} também cresceu e agora tem {p.altura} cm.")
        print('-' * 30)
    elif x == 2:
        i = int(input(f"Deseja engordar {p.nome} em quantos kilos? "))
        p.peso += i
        print("Atualizando...")
        sleep(1)
        print('-' * 30)
        print(f"{p.nome} agora tem {p.peso} kg!")
        print('-' * 30)
    elif x == 3:
        i = int(input(f"Deseja emagrecer {p.nome} em quantos kilos? "))
        p.peso -= i
        print("Atualizando...")
        sleep(1)
        print('-' * 30)
        print(f"{p.nome} agora tem {p.peso} kg!")
        print('-' * 30)
    elif x == 4:
        i = int(input(f"Deseja crescer {p.nome} em quantos centímetros? "))
        p.altura += i
        print("Atualizando...")
        sleep(1)
        print('-' * 30)
        print(f"{p.nome} agora tem {p.altura} cm!")
        print('-' * 30)
    else:
        print("Saindo do programa...")
        break
