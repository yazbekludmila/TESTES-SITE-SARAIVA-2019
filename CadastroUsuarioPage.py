from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from selenium import WebElement

from time import sleep

class Cadastrar_Usuario():

    def __init__(self, app):
        self.app = app
        
    def cadastrar_usuario_novo(self):

        sleep(8)
        campo_nome = self.app.find_element_by_id('firstname_pf')
        campo_nome.clear()
        campo_nome.send_keys('FABIO')
        sleep(8)

         ## ALTERAR COMPLEMeNTO ENDERECO 
        campo_sobrenome = self.app.find_element_by_id('lastname')
        campo_sobrenome.clear()
        campo_sobrenome.send_keys('GOMIEIRO')
        sleep(5)

       
       





        ###############################CAMPOS  
        #NOME 
#id="firstname_pf" 

#SOBRENOME = id = lastname 
#email =  id email_address_pf
#senha = id password
#senha confirmaçao = id confirmation 

#cpf = id = cpf-number 

#sexo id = gender === listbox 

#DATA NASCIMENTO = fulldob

#CELULAR = celular_pf 

#PAIS = country_id  == list box 

#cep id = zip 

#endereco 
#id street_1 == rua 

#NUMERO RUA id="address:numero_endereco" 

#COMPLEMENTO =  id=address:complemento_endereco

#BAIRRO =  id=address:bairro

#ESTADO = id = region_id

#cidade = id = city 

#telefone = id = telephonme_pf 

#BAIRRO =  id=address:ponto_referencia 

#BOTAO FINALZIAR CADASTRO = xpath 
#//*[@id="form-validate-register"]/div[4]/button



       
        ##############################  FORMA MAIS DIDATICA 
               
        #element=self.app.find_element_by_id('region_id')
        #buscaEstado = Select(element)  
        #teste = buscaEstado.select_by_visible_text("São Paulo")

        
        #sleep(5) 
                       
        #print(buscaEstado.first_selected_option.text)
        #assert buscaEstado.first_selected_option.text == "São Paulo"
                  
        # clicar botao para salvar alteracoes 
        #botao_conf_alteracoes = self.app.find_element_by_xpath('//*[@id="form-validate"]/div[3]/button')
        #botao_conf_alteracoes.click()
        #sleep(5) 

        
    #def validar_alteracoes(self):
       
    #    validacao_endereco = self.app.find_element_by_xpath('//*[@id="core_messages"]/ul/li/ul/li/span')
    #    print(validacao_endereco.text)
    #    assert  validacao_endereco.text == 'O endereço foi salvo.'   

        #self.app.find(link_text='O endereço foi salvo.', timeout=4)
        #self.app.assert_element_displayed(('link_text', 'O endereço foi salvo.'))
        # alteracoes_ok = self.app.find_element_by_xpath('//*[@id="core_messages"]/ul/li/ul/li/span')
        #assert alteracoes_ok.text == 'O endereço foi salvo.'          
