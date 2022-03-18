import random
a= str(input('primeiro aluno:'))
b= str(input('segundo aluno:'))
c= str(input('terceiro aluno:'))
d= str(input('quarto aluno:'))
e= [a,b,c,d]
f= random.choice(e)
print(f' o aluno escolhido foi {f} ')
