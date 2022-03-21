import random

k1 = '543298765432'

k1 = list(k1)


def gera():
    primeiro_digito = str(random.randint(0, 9))
    segundo_digito = str(random.randint(0, 9))
    segundo_bloco = str(random.randint(100, 999))
    terceiro_bloco = str(random.randint(100, 999))
    cnpj = primeiro_digito + segundo_digito + '.' + segundo_bloco + '.' + terceiro_bloco + '/0001-'

    temp = remove_carac(cnpj)
    temp = list(temp)

    for i in range(12):
        temp[i] = int(temp[i])
        k1[i] = int(k1[i])
        temp[i] *= k1[i]

    soma = 0
    for j in temp:
        soma += int(j)

    if 11 - (soma % 11) <= 9:
        cnpj += str(11 - (soma % 11))
    else:
        cnpj += '0'

    k2 = '6543298765432'
    k2 = list(k2)

    temp = remove_carac(cnpj)
    temp = list(temp)

    for i in range(13):
        temp[i] = int(temp[i])
        k2[i] = int(k2[i])
        temp[i] *= k2[i]

    soma = 0
    for j in temp:
        soma += int(j)

    if 11 - (soma % 11) <= 9:
        cnpj += str(11 - (soma % 11))
    else:
        cnpj += '0'

    return cnpj


def remove_carac(x):
    x = x.replace('.', '')
    x = x.replace('/', '')
    x = x.replace('-', '')
    return x
