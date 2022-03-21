# Faça uma lista com as seguintes opções:
#     adicionar tarefa
#     listar tarefas
#     opção de desfazer(desfaz ultima ação)
#     opção de refazer(refaz a ultima ação)

lista = ['Tarefa 1', 'Tarefa 2']

print(lista)
backup = []


def listitems(x):
    print()
    print(f'Lista: {x}')
    print()


def redo(z):
    if not backup:
        print('Nada a refazer')
    else:
        z.append(backup[-1])
        backup.pop()
        return


while True:
    act = input('Selecione uma ação (Adicionar, Listar, Desfazer, Refazer, Encerrar): ').capitalize()
    if act == 'Adicionar':
        ad = input('Digite a tarefa: ')
        lista.append(ad)
        continue
    if act == 'Listar':
        listitems(lista)
    if act == 'Desfazer':
        try:
            backup.append(lista[-1])
            lista.pop()
        except IndexError:
            print('Nada a desfazer')
            continue
    if act == 'Refazer':
        redo(lista)
    if act == 'Encerrar':
        break
