#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
#detalhe a formula de area do circulo é = area = pi.r², R= 1/2 diametro
#como o valor de pi e possui muitos numeros,irei utilizar 3,14

d = float (input ('digite o diametro de um circulo, :'))
r = d/2
area = r**2*3.14

print (f'a area do circulo corresponde a {area}m²')


