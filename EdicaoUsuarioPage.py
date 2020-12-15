from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Selecionar_Informacao_Alterar():


    def __init__(self, app):
        self.app = app
        
    def selecionar_opcao_menu(self):

        #SELECIONAR OPCAO NO MENU "MEUS ENDERECOS" E SELECIONAR ENDERECOO DESEJADO A ALTERAR 
        seleciona_menu = self.app.find_element_by_link_text('Olá, Ludmila')
        seleciona_menu.click()
        opcao_menu = self.app.find_element_by_link_text('Meus dados').click()
        opcao2_menu = self.app.find_element_by_link_text('Meus endereços').click()
        
    def selecionar_endereco_alterar(self,tipo_endereco):
        
        print("LUDMILAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(tipo_endereco) 
        if tipo_endereco == "Editar":
            print("ENTREIIIIIIIIIIIIIIIIIIIIIIIII IFFFFFFFF ENDERCO EXISTENTE")
            enderecos_cadastrados = []
            enderecos_cadastrados = self.app.find_elements_by_link_text('Editar')
            endereco_selecionado = enderecos_cadastrados[0] 
            endereco_selecionado.click()
        elif tipo_endereco == "Adicionar Endereco":
            print("ENTREIII ELSEEEEEEEEEEEEEEEEEEEEEEEEE  ADICAO ENDERECO")
            sleep(8)
            self.app.execute_script('window.scrollTo( 0, 190 );')
            sleep(8)
            endereco_selecionado = self.app.find_element_by_class_name('linkNewAddress')
            endereco_selecionado.click()    
    
    #def validar_pagina_endereco(self):
        #valido_login = self.app.find('link_text',"Olá, Ludmila")
        ##self.app.assert_element_displayed("link_text", "Meus endereços")               
    #    complemento_editar = self.app.find_element_by_id('complemento_endereco')
    #    print(complemento_editar.text)
        #assert complemento_editar.text == 'largo treze'
        #resultado = element_2
        #print(resultado.text)
        # print(total)
        
       