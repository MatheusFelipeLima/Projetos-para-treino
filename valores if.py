r1=int(input('digite um valor:'))
r2=int(input('digite outro:'))
r3=int(input('digite um terceiro valor:'))
menor = r1
if r2<r1 and r2<r3:
    menor= r2
if r3<r1 and r3<r2 :
    menor= r3
print(f'o menor valor foi {menor}')
maior= r2
if r1>r2 and r1>r3:
    maior = r1
if r3>r1 and r3>r2:
    maior= r3
print(f'o maior valor foi {maior}')
