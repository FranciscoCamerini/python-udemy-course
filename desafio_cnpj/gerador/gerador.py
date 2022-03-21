import random
import alg

while True:
    x = input('Gerar CNPJ? (s/n): ').lower()
    if x == 's':
        print()
        print(f'CNPJ GERADO = {alg.gera()}')
        print()
    else:
        break
