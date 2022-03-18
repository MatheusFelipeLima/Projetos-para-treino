nome = str(input('diga seu nome')).strip()
Up = nome.upper()
low = nome.lower()
novonome = nome.split()
B= len(nome)
A= len(nome)-nome.count(' ')
C= nome.find(' ')
print  (F'Seu nome com letra maiuscula é {Up}')
print (F'Seu nome com letras minusculas é{low}')
print ('a quantidade de letras que tem em seu nome com espaço é {}'.format(len(nome)))
print (f'seu nome tem o total de letras {A}')
print(f'seu primeiro nome tem {C} letras ')
print((novonome[0]))

#Upper = deixa todas as letras em maiuscula
#lower = deixa todas as letras em minuscula
#len conta todos os espaços ocupados da cadeia de dados,incluindo espaço
#split vai ocorrer uma divisao entre os espaços da frase
#''.join() junta duas coisas
