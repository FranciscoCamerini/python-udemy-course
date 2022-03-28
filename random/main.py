import random
import string

#  Gera um inteiro entre A e B
# inteiro = random.randint(10, 20)

# Gerar um aleatorio usando a funcao range()
inteiro = random.randrange(900, 1000, 10)

# Gera um flutuante entre A e B
# flutuante = random.uniform(10, 20)

# Gera um flutuante entre 0 e 1
flutuante = random.random()

lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny']
sorteio = random.choice(lista)
# sorteio = random.sample(lista, 2)
# sorteio = random.choices(lista, k=2)

# Embaralha a lista
random.shuffle(lista)

# Gera senha aleatório
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%*_-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))
print(senha)
