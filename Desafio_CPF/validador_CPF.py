"""
Este programa lê um numero no formato CPF (xyz.abc.ijk-mn),
no qual os ultimos 2 digitos são gerados a partir de um algoritmo
aplicado aos 9 primeiros digitos, atestando, ou não, a sua validade.
"""
while True:
    cpf1 = input('Digite um CPF para ser validado: ')
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

    if cpf1 == cpf:
        print('Válido!')
    else:
        print('Inválido!')
