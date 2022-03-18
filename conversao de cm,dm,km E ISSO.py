#Faça um Programa que converta metros para centímetros.
m = float (input ('digite uma distacia em metros :'))
km = float (m /1000)
hm = float (m /100)
dam = float (m/10)
metros = float (m)
dm = float (m*10)
cm = float (m*100)
mm = float (m*1000)

print (f'{km}km\n{hm}hm\n{dam}dam\n{metros}m\n{dm}dm\n{cm}cm\n{mm}mm\n')
