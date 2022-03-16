#
# Crie uma função1 que recebe uma função2 como parametro e retorne o valor da funcao2 executada
#


def func1(funcao):
    return funcao()


def func2():
    return 2


var = func1(func2)

print(var)

# Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada.
# Faça a funcao1 executar duas funcoes que recebam um numero diferente de argumentos
#


def fnc1(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fnc2(x):
    return f'Opa, {x}!'


def fnc3(x, y):
    return f'E aí, {x} {y}!'


var = fnc1(fnc2, 'salve')
var1 = fnc1(fnc3, 'salve', 'manin')
print(var)
print(var1)
