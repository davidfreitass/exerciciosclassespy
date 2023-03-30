while True:
    try:
        inteiro = int(input("Digite um número inteiro: "))
    except ValueError:
        print("ERRO: por favor, digite um número inteiro válido.")
    else:
        break

while True:
    try:
        real = float(input("Digite um número real: "))
    except ValueError:
        print("ERRO: por favor, digite um número real válido.")
    else:
        break

print(f"O número inteiro digitado foi {inteiro} e o real foi {real}.")
