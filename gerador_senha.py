import random
quantidade = int(input('\tDigite quantas senhas você quer gerar '))
print('')
comprimento = int(input('\tDigite o comprimento de sua  senhas  '))
caracteres = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVYXZ0123456789'

for c in range(quantidade):
    senha = ''
    print('')
    for i in range(comprimento):
        senha += random.choice(caracteres)
    print('\t',senha)
print('')