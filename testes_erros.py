try:
    a = int(input("Númerador: "))
    b = int(input("Denominador: "))
    resultado = a / b

except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")

except ZeroDivisionError:
    print("Não é possível dividir um número por zero.")

except KeyboardInterrupt:
    print("O usuário não inseriu os dados necessários.")

except Exception as error:
    print(f"O erro encontrado foi {error}.")

else:
    print(f"O resultado é {resultado:.1f}")
finally:
    print("Finalizando o programa... Volte Sempre!")
