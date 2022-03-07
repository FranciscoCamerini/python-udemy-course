nome = 'Jorge'
idade = 19
altura = 1.85
peso = 72.5
ano = 2022

nascimento = ano - idade
imc = peso / altura ** 2

print(f'Dados de {nome}: ')
print(f'Idade: {idade}')
print(f'Altura: {altura}')
print(f'Peso: {peso}')
print(f'Ano de nascimento: {nascimento}')
print(f'IMC: {imc:.2f}')