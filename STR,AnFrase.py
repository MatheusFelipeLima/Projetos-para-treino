
frase= str(input('Digite uma frase: ')).strip().upper().split()
junt = ''.join(frase)
b= str(input('Digite qualquer letra:')).upper()
contar= junt.count(f'{b}')
pos= junt.find(f'{b}')
lastpos=junt.rfind(f'{b}')

print(f'a letra {b} aparece {contar} vez(es)')
print(f'a letra {b} aparece a primeira vez em posiçao {pos+1}')
print(f'a ultima vez que a letra {b} aparece é em posiçao {lastpos+1}')