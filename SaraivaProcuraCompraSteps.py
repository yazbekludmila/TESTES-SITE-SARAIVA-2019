#from selenium import webdriver
from pages.pages.HomeSaraivaPage import Procura_Compra_Produto
#from pages.pages.LoginSaraivaPage import Fazer_Login_Saraiva
#from pages.pages.FreteSaraivaPage import Escolher_Frete
#from pages.pages.PagamentoPage import Fazer_Pagamento


@given(u'eu esteja na pagina inicial do site da saraiva {url}')
def step_impl(context, url):
    context.app.navigate(url)
    context.home.abrir_sitesaraiva()
 
@When (u'pesquisar produtos, os resultados das pesquisas são exibidos, os produtos são adicionados ao  carrinho') 
def step_impl(context):
   context.home.realiza_pesquisa()  
   #context.home.exibe_resultado()
   #context.home.seleciono_produto()

#@when(u'pesquisar produto')
#def step_impl(context):
#    context.home.realiza_pesquisa()


#@then(u'resultado da pesquisa é exibido')
#def step_impl(context):
#    context.home.exibe_resultado()

@then(u'carrinho lado direito para finalizar compra é clicado')
def step_impl(context):
#    context.home.seleciono_produto()
   context.home.finalizar_compra()

@then(u'efetuar login no site')
def step_impl(context):
   pass
     
@when(u'selecionar {tipo_usuario} usuário estará logado')
def step_impl(context,tipo_usuario):
    context.login.efetuar_login(tipo_usuario)
    ##### SE USUARIO NOVO == FAZER CADASTRO USUARIO 
    if tipo_usuario == "CADASTRE":
         print('ENTREIII IFFFFF VOU CADASTRAR USUARIO ')
         ## CLICAR BOTÃO CADASTRE-SE 
         context.cadastrousuario.cadastrar_usuario_novo()   

   #  context.app.navigate(context.pages['frete'])

@when(u'alterar o tipo de frete')
def step_impl(context):   
   context.frete.altera_frete()

@when(u'confirmar o tipo de frete')
def step_impl(context):   
   context.frete.confirmo_frete()

@when(u'digitar as informações de pagamento inválidas')
def step_impl(context):
    context.pagamento.preenche_informacoes_pagamento()

@then(u'aparecerá mensagem do site de dados de pagamento invalidos')
def step_impl(context):
    pass

# @then(u'aparecerá tela para fazer login')
# def step_impl(context):
#     context.login.efetuar_login()
# @then(u'aparecerá tela para confirmar o tipo de frete')
# def step_impl(context):
#     context.frete.confirmo_frete()





















