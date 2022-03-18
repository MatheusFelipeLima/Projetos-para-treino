Casa =float(input('digite o valor do imovelR$:'))
Salario=float(input('digite o valor do salario R$:'))
Tempo=int(input('digite o total de anos, que pretende parcelar R$'))
#Preciso converter o tempo de anos em meses
#verificar se o mensal nao excede o valor de 30% do salario
#dizer se aprova ou nao o financiamento
parcela = Casa / (Tempo*12 )
#SE salario for menor que 30%, NAO APROVA
if parcela>(Salario*30/100):
    print(f'seu financiamento nao foi aprovado devido que as parcelas são {parcela:.2f} e excedem 30% do seu salario' )
else:
 print(f'seu financiamento foi aprovado, as parcelas serão de {parcela:.2f}')
