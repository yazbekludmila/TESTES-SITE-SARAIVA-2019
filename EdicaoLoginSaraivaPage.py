from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Edicao_Fazer_Login():

    def __init__(self, app):
        self.app = app
        
    def efetuar_login(self):

        #DIGITAR EMAIL E SENHA 
        campo_email = self.app.find_element_by_id('email')
        campo_email.send_keys('ludmilayazbek@gmail.com')
        
        campo_senha = self.app.find_element_by_id('pass')
        campo_senha.send_keys('paimaect')
        
        # CLICAR NO BOTÃO CONTINUAR PARA EFETUAR LOGIN === vai para pagina usuario 
        botao_continuar_login = self.app.find_element_by_id('send2').click()
        sleep(2)
        # botao_pesquisa.submit()   
        #  
    def validar_login_efetuado(self):   
        #valido_login = self.app.find('link_text',"Olá, Ludmila")
        #element_2 = self.app.find_element_by_class_name('nm-searched-term')
        login_valido = self.app.find_element_by_class_name('ellipsis-text')
        #print(login_valido.text)
        assert  login_valido.text == 'Olá, Ludmila'    
        #resultado = element_2
        # print(resultado.text)
        # print(total)
        #assert resultado.text == 'Resultados para: Gestão da Emoção'