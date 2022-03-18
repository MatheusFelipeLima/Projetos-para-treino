s1=float(input('Primeiro segmento'))
s2=float(input('Segundo segmento'))
s3=float(input('Terceiro segmento'))
#regra o segmento tem q ser menor q a soma dos outros dois ou seja s1< s2+s3
if s1<s2+s3 and s2<s1+s3 and s3<s2+s1:
    print('os segmentos informados conseguem formar um triangulo')
else:
    print('os segmentos informados nao conseguem formar um triangulo')
