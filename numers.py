#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
C= int(input('me de um numero :'))
C2= int(input('mede um segundo numero:'))
C3= float(input('me de um terceiro numero:'))
h= (C*2)+(C2/2)
h2= (C*3)+C3
h3= C3**3

print (f'a={h},b={h2},c={h3}')


