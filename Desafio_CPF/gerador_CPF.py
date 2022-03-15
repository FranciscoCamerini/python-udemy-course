# 
#  esse programa gera um numero de CPF válido
#

from random import randint
numero = str(randint(100000000, 999999999))

cpf1 = numero
cpf1 = cpf1.replace('.', '')
cpf1 = cpf1.replace('-', '')

cpf = cpf1[0:9]

soma = 0
count = 10
for i in range(9):
    soma += int(cpf[i]) * count
    count -= 1
if 11 - (soma % 11) > 9:
    cpf += '0'
else:
    cpf += str(11 - soma % 11)

soma = 0
count = 11
for j in range(10):
    soma += int(cpf[j]) * count
    count -= 1
if 11 - (soma % 11) > 9:
    cpf += '0'
else:
    cpf += str(11 - soma % 11)

print(cpf)
