"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente:

Atributos: número da conta, nome do correntista e saldo.
Métodos: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""


class ContaCorrente:
    def __init__(self, conta, nome, saldo=0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def depositar(self, dep):
        self.saldo += dep
        return self.saldo

    def sacar(self, sac):
        self.saldo -= sac
        return self.saldo

    def __str__(self) -> str:
        return (
            "======================================\n"
            f"| Número da Conta: {c.conta}\n"
            f"| Nome do Correntista: {c.nome}\n"
            f"| Saldo: R${c.saldo},00"
        )


c = ContaCorrente(12345, "David")
print(c)
c.alterarNome("David Freitas")
print(c)
c.depositar(3800)
print(c)
c.sacar(425)
print(c)
