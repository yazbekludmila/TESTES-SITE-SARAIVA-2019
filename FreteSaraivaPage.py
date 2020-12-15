from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Escolher_Frete():

    def __init__(self, app):
        self.app = app
          
    def altera_frete(self):
        #botao_continua_pagto = self.app.find(('xpath', '//*[@id="shiping-meths"]/button'), timeout=5, wait_displayed=True)
        #botao_continua_pagto = self.app.find(xpath='//*[@id="shiping-meths"]/button',timeout=5,wait_displayed=True)
        #id, name, link_text, partial_link_text,
        #css, xpath, tag_name.
        #botao_continua_pagto = self.app.find(('partial_link_text', 'Continuar'))
        ##self.app.execute_script('window.scrollTo( 0, 11000 );')
        #sleep(6)
        self.app.execute_script('window.scrollTo( 0, 190000 );')
        sleep(6)
        
        ##### PATH TEXTO ECONOMICA == FRETE 
        #botao_altera_frete = self.app.find_element_by_xpath('//*[@id="shiping-meths"]/ul/li/ul[2]/li[2]/p[1]')
        #self.app.execute_script('window.scrollTo( 0, 10000 );')
        
        ## PATH FRETE ECONOMICA == RADIO BUTTON 
        
        botao_altera_frete = self.app.find_element_by_xpath('//*[@id="shiping-meths"]/ul/li/ul[2]/li[2]/input')
      
        botao_altera_frete.click()
        
        #assert botao_altera_frete.text == 'Econômica' 

        #selecao_ok = 'N' 

        if botao_altera_frete.is_selected(): 
          selecao_ok = 'S'
        else:
           selecao_ok = 'N'

        print('ludmila taissssssssssssssss==' ,selecao_ok)
        assert selecao_ok == 'S'    



        ### #assert botao_altera_frete.text == 'Econômica' 
        #if botao_altera_frete.is_selected(): 
        #  selecao_ok = 'S'
        #else:
        #   selecao_ok = 'N'

        #assert botao_altera_frete.Enabled 
        #self.app.assert_element_selected(('xpath', '//*[@id="shiping-meths"]/ul/li/ul[2]/li[2]/p[1]'))
        #self.app.assert_element_checked(('xpath', '//*[@id="shiping-meths"]/ul/li/ul[2]/li[2]/p[1]'))
        #self.app.assert_second_selected_option(('xpath', '//*[@id="shiping-meths"]/ul/li/ul[2]/li[2]/p[1]'))
        #assert.assertTrue((botao_altera_frete).isSelected())
        ##assert botao_altera_frete == 0    
        sleep(7)

    def confirmo_frete(self):
        #botao_continua_pagto = self.app.find(('xpath', '//*[@id="shiping-meths"]/button'), timeout=5, wait_displayed=True)
        #botao_continua_pagto = self.app.find(xpath='//*[@id="shiping-meths"]/button',timeout=5,wait_displayed=True)
        #id, name, link_text, partial_link_text,
        #css, xpath, tag_name.
        #botao_continua_pagto = self.app.find(('partial_link_text', 'Continuar'))
        #self.app.execute_script('window.scrollTo( 0, 11000 );')
        botao_continua_pagto = self.app.find_element_by_xpath('//*[@id="shiping-meths"]/button')
        #self.app.execute_script('window.scrollTo( 0, 10000 );')
        botao_continua_pagto.click()
        # self.app.execute_script("document.querySelector('.co_bt_continue').click();")
        sleep(10)