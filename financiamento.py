casa=float(input('digite o valor do imovelR$:'))
Salario=float(input('digite o valor do salario R$:))
Tempo=int(input('digite o total de anos, que pretende parcelar R$'))
#Preciso converter o tempo de anos em meses
#verificar se o mensal nao excede o valor de 30% do salario 
#dizer se aprova ou nao o financiamento
parcela= casa/(tempo*12)
#SE salario for menor que 30%, NAO APROVA
if parcela>(salario*30/100):
    print('seu financiamento nao foi aprovado devido que as parcelas excedem 30% do seu salario )
elif :
 print('seu financiamento foi aprovado')
