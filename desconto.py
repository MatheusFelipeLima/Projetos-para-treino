#enunciado : fazer um bang de desconto de 5%

preco  = float (input('digite o valor do produto desejado,para saber o preço com desconto de 5%:  '))
b = float ( preco -(preco*5/100) )
print (f'o valor do produto é :{b:.2f}')