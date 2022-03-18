from selenium import webdriver #controla o navegador
from selenium.webdriver.common.keys import Keys #controla teclado
from selenium.webdriver.common.by import By #localiza no navegador
import time
#Criar navegador
navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')
#pesquisar cotaçao dolar
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys\
    ('Cotação Dólar',Keys.ENTER)
cotaçao_dolar = navegador.find_element(
    By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(f'a cotaçao atual do Dolar é {cotaçao_dolar}')

#Euro.
navegador.get('https://www.google.com.br/')
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys\
    ('Cotação Euro',Keys.ENTER)
cotaçao_euro = navegador.find_element(
    By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(f'a cotaçao do euro atual é {cotaçao_euro}')

#Libra esterlina.
navegador.get('https://www.google.com.br/')
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys\
    ('Cotação Libra Esterlina ',Keys.ENTER)
cotaçao_libra = navegador.find_element(
     By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(f'a cotaçao do libra atual é {cotaçao_libra}')

#Iene.
navegador.get('https://www.google.com.br/')
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys\
    ('Cotação Iene ',Keys.ENTER)
cotaçao_iene = navegador.find_element(
     By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(f'a cotaçao do iene atual é {cotaçao_iene}')

#Dólar Australiano.
navegador.get('https://www.google.com.br/')
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys\
    ('Cotação Dolar Australiano ',Keys.ENTER)
cotaçao_dolaraustraliano = navegador.find_element(
     By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(f'a cotaçao do Dolar Australiano é {cotaçao_dolaraustraliano}')

#Franco Suíço.
navegador.get('https://www.google.com.br/')
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys\
    ('Cotação Franco Suíço ',Keys.ENTER)
cotaçao_FrancoSuíço = navegador.find_element(
     By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(f'a cotaçao do Franco Suíço atual é {cotaçao_FrancoSuíço}')

#Dólar Canadense.
navegador.get('https://www.google.com.br/')
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys\
    ('Cotação Dolar Canadense ',Keys.ENTER)
cotaçao_dolarCanadense = navegador.find_element(
     By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(f'a cotaçao do Dolar Canadense atual é {cotaçao_dolarCanadense}')
#Renminbi (Yuan)
navegador.get('https://www.google.com.br/')
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys\
    ('Cotação Renminbi (Yuan) ',Keys.ENTER)
cotaçao_RenminbiYuan = navegador.find_element(
     By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(f'a cotaçao do Renminbi (Yuan) atual é {cotaçao_RenminbiYuan}')
navegador.quit()

