
k1 = '543298765432'

k1 = list(k1)


def valida(cnpj):
    cnpj_original = remove_carac(cnpj)
    novo_cnpj = remove_carac(cnpj)

    def sequencia(f):
        if f[0] * len(f) == f:
            return True
        else:
            return False

    if not sequencia(novo_cnpj):
        pass
    else:
        cnpj = input('ERRO, digite novamente: ')

    novo_cnpj = novo_cnpj[0:12]
    temp = list(novo_cnpj)
    for i in range(12):
        temp[i] = int(temp[i])
        k1[i] = int(k1[i])
        temp[i] *= k1[i]

    soma = 0
    for j in temp:
        soma += int(j)

    if 11 - (soma % 11) <= 9:
        novo_cnpj += str(11 - (soma % 11))
    else:
        novo_cnpj += '0'

    k2 = '6543298765432'
    k2 = list(k2)

    temp = list(novo_cnpj)
    for i in range(13):
        temp[i] = int(temp[i])
        k2[i] = int(k2[i])
        temp[i] *= k2[i]

    soma = 0
    for j in temp:
        soma += int(j)

    if 11 - (soma % 11) <= 9:
        novo_cnpj += str(11 - (soma % 11))
    else:
        novo_cnpj += '0'

    if cnpj_original == novo_cnpj:
        return print('O CNPJ digitado é valido')
    else:
        return print('O CNPJ digitado é inválido')


def remove_carac(x):
    x = x.replace('.', '')
    x = x.replace('/', '')
    x = x.replace('-', '')
    return x
