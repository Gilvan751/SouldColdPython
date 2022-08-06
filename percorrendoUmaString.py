nome = 'python'
# primeir maneira for
for i in nome:
    print(i)

print('-'*30)
#segunda maneira comando while
i = 0
while i < len(nome):
    print(nome[i])
    i+=1
print('-='*30)
#terceira percorrer com for / enumerate
for k,v in enumerate(nome):
    print(k,v)
