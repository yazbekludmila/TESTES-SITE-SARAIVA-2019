@Pesquisa_Compra_Saraiva 

Feature: Procura e compra Produtos  
#Acessar site Saraiva , Pesquisar por Produto, Selecionar Produto para compra, efetuar login , fazer pagamento"
       
    Eu como usuario já cadastrado no site da Saraiva 
    Quero realizar a pesquisa de um Produto no Site da Saraiva
    Entao realizar a compra desse produto pelo site  

    """Feature Description"""

   Background: Estar no site da Sariava 
        Given eu esteja na pagina inicial do site da Saraiva https://www.saraiva.com.br
        When pesquisar produtos, os resultados das pesquisas são exibidos, os produtos são adicionados ao  carrinho 
        Then carrinho lado direito para finalizar compra é clicado
        Then efetuar login no site 


   @ProcuraCompraProdutoClienteJaCadastrado
   Scenario: Compra de Produto com usuário já cadastrado
        When selecionar CONTINUAR usuário estará logado 
        When alterar o tipo de frete 
        When confirmar o tipo de frete 
        When digitar as informações de pagamento inválidas  
        Then aparecerá mensagem do site de dados de pagamento invalidos  
   
   @ProcuraCompraProdutoClienteNaoCadastrado
   Scenario: Alteraçao de Endereço com Usuário já Cadastrado 
        When selecionar CADASTRE usuário estará logado 
        When alterar o tipo de frete 
        When confirmar o tipo de frete 
        When digitar as informações de pagamento inválidas  
        Then aparecerá mensagem do site de dados de pagamento invalidos  
