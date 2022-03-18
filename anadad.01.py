from selenium import webdriver #controla o navegador
from selenium.webdriver.common.keys import Keys #controla teclado
from selenium.webdriver.common.by import By #localiza no navegador
#Criar Navegador
navegador = webdriver.Chrome()
#entrar no google
navegador.get('https://www.google.com.br/')
#pesquisar cotaçao dolar

#navegador.quit()
#inacabado
#pegaria a cotaçao do dolar
#pesquisaria a cotaçao euro
#pegaria a cotaçao do euro
#entraria em https://www.melhorcambio.com/ouro-hoje
#pegaria a cotaçao do ouro
#importar a base de dados
#atualizar as cotaçoes na base de dados
#atualizar o preço de compra e venda
#exportar a base de dados para ter um resultado atualizado
