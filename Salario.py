#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês..
# Calcule e mostre o total do seu salário no referido mês
salario = float(input('Quanto voce ganha por hora trabalhada R$:' ))
horas = float(input('Quantas horas voce trabalha no dia ?'))
d = int(input('Quantos dias voce trabalha na semana ?'))
h = salario*horas
c = (h*d)*4
print(f'o seu salario é R${c:.2f},por mês')
