from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Fazer_Login_Saraiva():

    def __init__(self, app):
        self.app = app
        
    def efetuar_login(self,tipo_usuario):

        if tipo_usuario == "CONTINUAR":
            print('ENTREIIIIIIIIIIIIIIIIIIIIIIIII IFFFFFFFF')
            #DIGITAR EMAIL E SENHA
            campo_email = self.app.find_element_by_id('login-email')
            campo_email.send_keys('ludmilayazbek@gmail.com')
        
            campo_senha = self.app.find_element_by_id('login-password')
            campo_senha.send_keys('paimaect')

            # CLICAR NO BOTÃO CONTINUAR PARA EFETUAR LOGIN === vai para opçoes frete 
            botao_continuar_login = self.app.find_element_by_id('send2').click()
            sleep(2)         
           
        elif tipo_usuario == "CADASTRE":
            print('ENTREIII ELSEEEEEEEEEEEEEEEEEEEEEEEEE opçao CADASTRAR USUARIOOOOOOOO ')
            ## CLICAR BOTÃO CADASTRE-SE 
            botao_cadastro = self.app.find_element_by_id('onepage-guest-register-button').click()
            # cadastra usuario novo 
            ##context.cadastrousuario.cadastrar_usuario_novo()    
            
            