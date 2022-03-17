"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
first_list = [1, 2, 3, 4, 5, 6, 7]
second_list = [2, 4, 6, 8]

try:
    lista_soma = [first_list[x] + second_list[x] for x in range(len(first_list))]
except:
    lista_soma = [first_list[x] + second_list[x] for x in range(len(second_list))]

#  Solução proposta ---->  lista_soma = [x + y for x, y in zip(first_list, second_list)]

print(lista_soma)
