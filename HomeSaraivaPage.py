from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
##from selenium.webdriver.support import expected_conditions as ec
import csv

print (__doc__)

class Procura_Compra_Produto():

    def __init__(self, app):
        self.app = app
        # self.pagina('https://www.saraiva.com.br')

    def abrir_sitesaraiva(self):
        self.app.get('https://www.saraiva.com.br')

    def realiza_pesquisa(self):
        
        #### LENDO ARQUIVO COM NOME DO PRODUTO E XPATH CARRINHOO SELECIONANDO PARA COMPRA (produto,carrinho)
        f = csv.reader(open('produtos.csv'), delimiter=';')
        ##f = csv.reader(open('produtos.txt'), delimiter=';')
        for [produto,carrinho] in f:
            #if produto == ' ' :
      
      
            #  exit  
            print ('PRODUTO E CARRINHOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
            print (produto,carrinho)
            campo_pesquisa = self.app.find_element_by_id('q')
        ##campo_pesquisa.send_keys('Ansiedade 2')
            campo_pesquisa.clear()
            campo_pesquisa.send_keys(produto)
            botao_pesquisa = self.app.find_element_by_id('chaordic-search-button')
            sleep(2)
            botao_pesquisa.click()
        #self.app.click("chaordic-search-button","id")
        

    #def exibe_resultado(self):
        # assert self.app.title == "Gestão da emoção na Saraiva "
        # element = self.app.find_element_by_class_name('neemu-total-products-valor')
        # total = element.text
      
            element_2 = self.app.find_element_by_class_name('neemu-total-products-container')

        ##element_2 = self.app.find_element_by_class_name('neemu-total-products-container')
        
            resultado = element_2
            print(resultado.text)
        # print(total)
        #assert resultado.text == '7 produtos'
            sleep(3)
        #assert resultado.value == '7'
        #assert element.text == "Resultados para: Gestão da emoção"
        #assert self.app.title == 'Gestão da emoção na Saraiva'

    #def seleciono_produto(self):
        #clico no carrinho do produto selecionando ele para compra 
        #carrinho_produto = self.app.find_element_by_xpath('//*[@id="nm-product-9345571"]/div[3]/a')
        #carrinho_produto.click()
        #sleep(3)

######### ESPERA EXPLICITA #############################
            self.app.execute_script('window.scrollTo( 0, 500 );')
            wait = WebDriverWait(self.app, 120)

        ##carrinho_produto = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nm-product-9345571"]/div[3]/a')))
        
        ##    carrinho_produto = wait.until(EC.element_to_be_clickable((By.XPATH, carrinho)))
            
            #carrinho_produto = self.app.find_element_by_xpath(carrinho)     

            #caminho = '//*[@id="nm-product-9345571"]/div[3]/a'  
            #print(caminho)
            caminho = carrinho
            print('CARRINHOOOOOOOOOOOOOOOOO  ARQUIVOOOOOOOOOOOOOOOOOOOOOOOOOOO')
            print(caminho)
            #carrinho_produto = self.app.find_element_by_xpath('//*[@id="nm-product-9345571"]/div[3]/a')
            carrinho_produto = self.app.find_element_by_xpath(caminho)
        ##carrinho_produto = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="nm-product-9345571"]/div[3]/a')))
           
            carrinho_produto.click()
            sleep(10)
            self.app.execute_script('window.scrollTo( 500, 0 );')
            sleep(10)
        print (f.line_num, 'linhas lidasSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')

        #carrinho_produto = self.app.find_element_by_xpath('//*[@id="nm-product-9345571"]/div[3]/a')
        #wait.until(EC.element_to_be_clickable((carrinho_produto)))
        #carrinho_produto.click()
        
    def finalizar_compra(self):
        #clico no carrinho do lado direito da tela para finalizar compra  
        #self.app.execute_script('window.scrollTo( 1500, 0 );')
        #self.app.find_element_by_id('content-minicart').focus()
        #self.app.find_element_by_id('content-minicart').focus()
        carrinho_finaliza = self.app.find_element_by_id('content-minicart')
        carrinho_finaliza.click()
        sleep(5)
                
        #clico no botão continuar para finalizar compra /pagamento  == vai pagina login / PAG PAGAMENTO / vai pedir login
        botao_continuar = self.app.find_element_by_id('proceed-checkout')
        botao_continuar.click()