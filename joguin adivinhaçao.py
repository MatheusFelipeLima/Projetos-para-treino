from time import sleep
from random import randint
computador = randint(0, 5)
print('====='*10)
player = int(input( 'olá caro jogador, tente adivinhar o numero que estou pensando de 0 até 5 :'))
print ('o numero que eu escolhi foi')
print('Processando...')
sleep(2)
print('trocando de numero...')
sleep(2)
if \
        computador == player :
    print( f' parabens eu escolhi {computador} e você acertou, PERDI ')
else:
    print(f'eu escolhi {computador} e voce errou! Ganhei')
