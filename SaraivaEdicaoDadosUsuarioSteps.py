#from selenium import webdriver
from pages.pages.EdicaoHomeSaraivaPage import Edicao_Home_Clicar_Fazer_Login
#from pages.pages.EdicaoLoginSaraivaPage import Fazer_Login_Saraiva
#from pages.pages.EdicaoEnderecoSaraivaPage import Edicao_Endereco
#from pages.pages.EdicaoUsuarioPage import Fazer_Pagamento

@given(u'eu esteja na Home Page do site da saraiva {url}')
def step_impl(context, url):
    context.app.navigate(url)
    context.edicaohome.abrir_sitesaraiva()
        
@when(u'fizer login com usuário já cadastrado')
def step_impl(context):
   context.edicaohome.fazer_login_edicao()
   context.edicaologin.efetuar_login()

@then(u'usuário estará logado')
def step_impl(context):
    context.edicaologin.validar_login_efetuado()

@when(u'selecionar no menu a opção : Meu Perfil / meus endereços')
def step_impl(context):
    context.edicaousuario.selecionar_opcao_menu()

@then(u'aparecerá tela com endereços cadastrados')
def step_impl(context):
    pass
 
@when(u'selecionar {tipo_endereco} aparecerá página para editar endereço')
def step_impl(context,tipo_endereco):
    context.edicaousuario.selecionar_endereco_alterar(tipo_endereco)

@when(u'digitar as informações desejadas e clicar em Salvar Endereço' )
def step_impl(context):
    context.edicaoendereco.editar_endereco()

@then(u'aparecerá mensagem de O endereço foi salvo.')
def step_impl(context):
    context.edicaoendereco.validar_alteracoes()

