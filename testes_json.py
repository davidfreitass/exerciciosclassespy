import json

# Transformando arquivo tipo JSON em dicionário Python

carros_json = '{"Marca": "Volkswagen", "Modelo": "Jetta", "Ano": 2016, "Versao": "Highline 2.0 Tsi", "Cor": "Branco"}'
carros = json.loads(carros_json)

for item, valor in carros.items():
    print(f"{item}: {valor}")

print('-' * 50)

# Transformando um dicionário Python em um arquivo tipo JSON

carros = {"Marca": "Volkswagen", "Modelo": "Jetta",
          "Ano": 2016, "Versao": "Highline 2.0 Tsi", "Cor": "Branco"}
carros_json = json.dumps(carros, indent=4)

print(carros_json)

print('-' * 50)

# Lendo arquivos JSON em Python

with open("texto.json") as arquivo:
    novo_dicionario = json.load(arquivo)

for item, valor in novo_dicionario.items():
    print(f"{item}: {valor}")
