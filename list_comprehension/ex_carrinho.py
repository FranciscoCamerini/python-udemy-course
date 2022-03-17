# Some o preço total dos produtos no carrinho
# usando list comprehension

carrinho = []
#                Produto      Preço
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', '10'))
carrinho.append(('Produto 3', 60))
...

total = sum([float(y) for x, y in carrinho])

print(f'TOTAL = {total}')
