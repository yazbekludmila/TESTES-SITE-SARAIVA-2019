from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from selenium import WebElement
from time import sleep
#import logging
#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
########### gravando log ARQUIVO 
import logging
logging.basicConfig(filename='LOGSARAIVA.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


class Alterar_Endereco():

    def __init__(self, app):
        self.app = app      
        
    def editar_endereco(self):

        #alterar informaçoes do usuário : sobrenome / telefone /estado 
        ## ALTERAR SOBRENOME 
        ##sleep(8)
        
        logging.debug('Start of programMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')

        #print ("entreiiiiiiiiiiiiiiiiiiiiiii edicao endereco")
        campo_sobrenome = self.app.find_element_by_id('lastname')
        campo_sobrenome.clear()
        campo_sobrenome.send_keys('Gomieiro')
        sleep(8)

         ## ALTERAR COMPLEMeNTO ENDERECO 
        campo_complem_end = self.app.find_element_by_id('complemento_endereco')
        campo_complem_end.clear()
        campo_complem_end.send_keys('estacionamento')
        sleep(5)

        ##self.app.execute_script('window.scrollTo( 0, 12000 );')
        #select = Select(self.app.find_element_by_id('region_id'))
        #select.select_option_by_visible_text('Piauí')
        #teste = select.select_option_by_visible_text('Piauí')
        #assert select.first_selected_option.text == "Piauí"
       
        ##############################  FORMA MAIS DIDATICA 
               
        element=self.app.find_element_by_id('region_id')
        buscaEstado = Select(element)  
        teste = buscaEstado.select_by_visible_text("Minas Gerais")
        print('SELECIONADO', buscaEstado.first_selected_option.text)
        logging.debug('SELECIONADO', buscaEstado.first_selected_option.text)
    
        #print("Ludmilaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa   ESTADO ") 
        #print("DISPONIVEIS")
        disponiveis = []
        itemlista = ' ' 
        #elements=self.app.find_elements_by_id('region_id')
        #selecionadas =  Select(elements)  
        #selecionadas =  buscaEstado.all_selected_options
        
        disponiveis =  buscaEstado.options
        ##for contador in range(1, 11):
        for ind in range(len(disponiveis)):     
          if disponiveis[ind] != ' ' : 
             itemlista = disponiveis[ind] 
             logging.debug('DISPONIVEISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
             logging.debug(str(ind))
             logging.debug(itemlista.text)
             print('disponiveis',ind, itemlista.text)
              
        #print("Ludmilaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa   ESTADO ") 
        #print("SELECIONADAS")
        
        selecionadas = []
        itemlista = ' ' 
                
        selecionadas =  buscaEstado.all_selected_options
        for ind in range(len(selecionadas)): 
          if selecionadas[ind] != ' ' : 
             itemlista = selecionadas[ind] 
             print('selecionadas',ind, itemlista.text)
             ##logging.debug('selecionadas',ind, itemlista.text)
             logging.debug('SELECIOANDASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
             logging.debug(str(ind))
             logging.debug(itemlista.text)


        ##selecionadas =  buscaEstado.all_selected_options
        #print (selecionadas)
        ##print ('deu certo') 
        ##print(buscaEstado.all_selected_options) 
        #print(selecionadas) 

        assert buscaEstado.first_selected_option.text == "Minas Gerais"
             
        sleep(3) 
         
        logging.debug('End of programMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM') 
        #print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPÇOES DISPONIVEIS")
        #disponiveis = [] 
        #disponiveis = buscaEstado.options
        #print(disponiveis[0-20].text)
        #print(buscaEstado.options)

        ### PARA VER TODAS OPÇOES SELECIONADAS 
        #opcoes_selecionadas = buscaEstado.all_selected_options
        #print("SELECIONADASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
        #print(buscaEstado.all_selected_options)
        #print(opcoes_selecionadas)
        
        #print(opcoes_selecionadas)

        ####  PARA VER TODAS OPÇOES DISPONIVEIS 
        #opcoes_disponiveis = buscaEstado.options
        #print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPÇOES DISPONIVEIS")
        #print(buscaEstado.options)


                    
        # clicar botao para salvar alteracoes 
        botao_conf_alteracoes = self.app.find_element_by_xpath('//*[@id="form-validate"]/div[3]/button')
        botao_conf_alteracoes.click()
        sleep(5) 

        
    def validar_alteracoes(self):
       
        validacao_endereco = self.app.find_element_by_xpath('//*[@id="core_messages"]/ul/li/ul/li/span')
        print(validacao_endereco.text)
        assert  validacao_endereco.text == 'O endereço foi salvo.'   

        #self.app.find(link_text='O endereço foi salvo.', timeout=4)
        #self.app.assert_element_displayed(('link_text', 'O endereço foi salvo.'))
        # alteracoes_ok = self.app.find_element_by_xpath('//*[@id="core_messages"]/ul/li/ul/li/span')
        #assert alteracoes_ok.text == 'O endereço foi salvo.'    
        # 
        # 
        # #### PARA VER TODAS OPÇOES SELECIONADAS 
        #opcoes_selecionadas = buscaEstado.all_selected_options
        ##print('SELECIONADASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
        ##print(buscaEstado.all_selected_options[0-10].text)
        
        #print(opcoes_selecionadas)

        ####  PARA VER TODAS OPÇOES DISPONIVEIS 
        ##opcoes_disponiveis = buscaEstado.options
        #print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPÇOES DISPONIVEIS')
        #print(buscaEstado.options[0-10].text)      
