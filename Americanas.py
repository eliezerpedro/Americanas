import os
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Americanas:
    def __init__(self):
        self.dirpath = os.getcwd()+'\\chromedriver.exe' #define o path do driver
        self.chrome_options = Options()
        self.chrome_options.add_argument('--start-maximized') #ativa o modo full screen do navegador
        self.chrome_options.add_argument("--enable-javascript") #habilita o javascript
        self.browser = webdriver.Chrome(executable_path=self.dirpath, options=self.chrome_options) #instancia o driver
        
    def consulta(self):
        self.browser.get('https://www.americanas.com.br/') #Abre a página da americanas
        self.browser.find_element_by_id('h_search-input').send_keys('console ps4') #digita por console ps4
        self.browser.find_element_by_id('h_search-btn').click() #clica em pesquisar
        self.browser.find_element_by_id('lgpd-accept').click() #aceita os cookies
        self.browser.find_elements_by_xpath('*//h3[contains(text(), "Console")]')[0].click() #clica na primeira opção que tiver o nome console
        self.browser.find_element_by_xpath('*//input[@name="cep"]').send_keys('54745150') #digita o cep
        self.browser.find_element_by_xpath('*//button[contains(text(), "ok")]').click() #Clica em ok
        sleep(1)
        self.browser.find_element_by_xpath('*//span[contains(text(), "mais formas de entrega")]').click() #clica em mais formas de entrega
        sleep(1)
        precos = self.browser.find_elements_by_xpath('*//div[contains(@class, "price__PriceWrapper")]') #cria uma lista com os elementos dos fretes

        print('Valores de frete disponíveis:')
        for x in precos: #itera na lista de elementos e printa o valor dos fretes
            print(x.text) 

        self.browser.refresh() #atualiza a página para fechar a lista de fretes

        self.browser.find_element_by_xpath('*//span[contains(text(), "comprar")]').click() #clica em comprar
        sleep(1)
        self.browser.find_element_by_xpath('*//button[contains(text(), "Continuar")]').click() #clica em continuar

        self.browser.get('https://sacola.americanas.com.br/carrinho/#/basket') #abre a página do carrinho

        try:
            self.browser.find_element_by_xpath('*//h3[contains(text(), "Console")]') #checa se o produto está no carrinho
            print('Produto na sacola')
        except:
            print('Produto não está na sacola')

        self.browser.quit() #fecha a instancia do browser.
        
americanas = Americanas()

americanas.consulta()