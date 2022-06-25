from random import randint

jogador = input('Pedra(p), Papel(a), Tesoura(t)? ')
print(jogador, 'vs', end=' ')
escolhido = randint(1, 3)

if escolhido == 1:
    computador = 'p'
elif escolhido == 2:
    computador = 'a'
else:
    computador = 't'
print(computador)

if jogador == computador:
    print('EMPATOU!')
elif jogador == 'p' and computador == 't':
    print('O jogador ganhou!')
elif jogador == 'p' and computador == 'a':
    print('O computador ganhou!')

elif jogador == 't' and computador == 'a':
    print('O jogador ganhou !')
elif jogador == 't' and computador == 'p':
    print('O computador ganhou!')
elif jogador == 'a' and computador == 'p':
    print('O jogador ganhou !')
elif jogador == 'a' and computador == 't':
    print('O computador ganhou!')





