"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente:

Atributos: número da conta, nome do correntista e saldo.
Métodos: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""


class ContaCorrente:
    def __init__(self, conta, nome, saldo):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def depositar(self, dep):
        return self.saldo + dep

    def sacar(self, sac):
        return self.saldo - sac
