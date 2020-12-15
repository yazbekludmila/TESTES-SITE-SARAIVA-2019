from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Edicao_Home_Clicar_Fazer_Login():

    def __init__(self, app):
        self.app = app
        # self.pagina('https://www.saraiva.com.br')

    def abrir_sitesaraiva(self):
        self.app.get('https://www.saraiva.com.br')
        
    def fazer_login_edicao(self):
        #clicar NO link "entre ou cadastre-se"
        link_entrarsite = self.app.find_element_by_class_name('my-account')
        link_entrarsite.click()
       ## link_entrarsite = find_element_by_xpath('//*[@id="header"]/div/section[2]/ul/li[1]/a')
       #sleep(2)
        #link_entrarsite.submit() 
        #link_entrarsite.click()
    #    link_entrarsite = self.app.find('link_text',"Entre ou cadastre-se").click()
         
        

    