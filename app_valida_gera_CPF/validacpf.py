def validacpf(cpf1):
    cpf1 = str(cpf1)

    cpf1 = cpf1.replace('.', '')
    cpf1 = cpf1.replace('-', '')

    if not cpf1 or len(cpf1) != 11:
        return False

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
        return True
    else:
        return False