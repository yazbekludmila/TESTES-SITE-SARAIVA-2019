from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Fazer_Pagamento():

    def __init__(self, app):
        self.app = app
          
    def preenche_informacoes_pagamento(self):
        #DIGITAR numero cartão e numero seguranca cartao 
        campo_cartao = self.app.find_element_by_id('cc_number_new')
        campo_cartao.send_keys('1111222233334444')
        
        campo_segurancacartao = self.app.find_element_by_id('cc_cvv_new')
        campo_segurancacartao.send_keys('123')
        
        # CLICAR NO BOTÃO CONTINUAR PARA EFETUAR LOGIN 
        #botao_continuar_login = self.app.find_element_by_id('send2').click()
        #sleep(2)
        # botao_pesquisa.submit()
