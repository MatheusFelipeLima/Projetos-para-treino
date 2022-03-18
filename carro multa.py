radar = float(input('qual a velocidade do carro :'))
if radar <= 80:
    print (f'voce estava a {radar}km/h dirija com segurança, tenha um bom dia !')
else:
    radar >= 80
    Soma = (radar-80)*7
    print(f'voce estava em {radar}km/h e sera multa em R$:{Soma}')