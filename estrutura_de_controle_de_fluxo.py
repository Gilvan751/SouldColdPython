#while == enquanto i=0 e um contador

""" from time import sleep


i = 0
while(i<=10):
    i +=1
    print("O loop esta rodando")
    sleep(1)
 """

""" i = 0
for i in 'PYTHON':
    print(f'index.{i}')

num = [1,5,7,9,13,15]
for j in num:
    print(j) """
""" for i in range(10):
    i+=1
    print(i)

print('=-='*30)
for j in range(-10,0,2):
    print(j) """

#Exercicio imprimir os multiplos de 3 no intervalo de 0 a 15
""" for i in range(0,18,3):
    print(i) """
""" 
from time import sleep


print('Entrando no laço....')
for i in range(10):
    if(i==5):
        break
    
print('Saindo no laço....') """

print('Entrando no laço...')
i = 0
while(i<10):
    i+=1
    if(i%2):
        continue
    print(i)
print('Saindo do laço...')