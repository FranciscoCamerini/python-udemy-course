n = int(input('Quantas matérias serão consideradas no cálculo da média? '))
print('')

nota_total = 0
peso_total = 0
menor_nota = 10000
maior_nota = 0

for i in range(n):
    nome = input(f'Nome da {i+1}a matéria:  ')

    peso = float(input(f'Peso da materia "{nome}": '))
    while peso <= 0:
        print('O peso deve ser um valor positivo')
        peso = float(input(f'Peso da materia "{nome}": '))
    peso_total = peso_total + peso

    nota = float(input(f'Nota obtida na materia "{nome}": '))
    while nota < 0:
        print('A nota deve ser um valor maior ou igual a zero')
        nota = float(input(f'Nota obtida na materia "{nome}": '))
    if nota < menor_nota:
        menor = nome
        menor_nota = nota
    if nota > maior_nota:
        maior = nome
        maior_nota = nota
    nota_total = nota_total + nota * peso

    print('')

nota_final = nota_total / peso_total

print(f'NOTA FINAL = {nota_final:.2f}')
print('')
print(f'MATERIA COM A MENOR NOTA = {menor}')
print('')
print(f'MATERIA COM A MAIOR NOTA = {maior}')
