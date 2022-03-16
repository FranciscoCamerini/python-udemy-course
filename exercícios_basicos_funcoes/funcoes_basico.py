# 1 Crie um funcao que exibe uma saudação com os paramentros saudacao e nome
#
#
def cumprimento(saudacao='Ola', nome='Usuário'):
    return saudacao + nome


var = cumprimento()

print(var)

# 2 Crie uma função que recebe 3 numeros e exibe a soma deles
#
#


def soma3(x=0, y=0, z=0):
    return x + y + z


soma = soma3(4, 3, 11)

print(soma)

# 3 Crie uma função que recebe 2 numeros. O primeiro é um valor e o segundo um percentual.
#   Retorne o valor do primeiro numero  somado  do aumento percentual do mesmo
#


def aumento(a, b):
    return a * (b / 100 + 1)


num = float(input('Digite um número: '))
per = input('Digite o aumento percentual para o numero: ')
per = float(per.replace('%', ''))

new_num = aumento(num, per)

print(f'Numero com o aumento percentual = {new_num:.2f}')

# 4 Se o parametro da função for divisivel por 2, retorne fizz, se o parametro da funcao
#   for divisivel por 5, retorne buzz. Se o parametro da funcao for divisivel por 5 e 3,
#   retorne Fizzbuzz, caso contrario retorne o numero enviado


def fizz_buzz(a=1):
    if (a % 5 == 0) and (a % 3 == 0):
        return f'FizzBuzz, {a} é divisivel por 5 e 3'
    elif a % 2 == 0:
        return f'Fizz, {a} é divisivel por 2'
    elif a % 5 == 0:
        return f'Buzz, {a} é divisivel por 5'
    else:
        return a


while True:
    numero = input('Digite um numero inteiro: ')

    while not numero.isnumeric():
        numero = input('ERRO, digite novamente: ')

    temp = int(numero)

    print(fizz_buzz(temp))
