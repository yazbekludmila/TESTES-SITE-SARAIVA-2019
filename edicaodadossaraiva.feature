@Edicao_dados_saraiva

Feature: Ediçao de Informações do Usuário 

    Eu como usuario já cadastrado no site da Saraiva 
    Quero realizar a alteraçao de um  endereço já cadastrado , sobrenome, complemento e estado
    Quero realizar a inclusão de um  novo endereço  
    

    """Feature Description"""

   Background: Estar no site da Saraiva 
   Given eu esteja na Home Page do site da saraiva https://www.saraiva.com.br
   When fizer login com usuário já cadastrado 
   Then usuário estará logado 
   When selecionar no menu a opção : Meu Perfil / meus endereços 
   Then aparecerá tela com endereços cadastrados  

   @AlteraEnderecoClienteJaCadastrado
   Scenario: Alteraçao de Endereço com Usuário já Cadastrado 
        When selecionar Editar aparecerá página para editar endereço
        When digitar as informações desejadas e clicar em Salvar Endereço 
        Then aparecerá mensagem de O endereço foi salvo. 

   @IncluiEnderecoClienteJaCadastrado
   Scenario: Inclusão de novo de Endereço com Usuário já Cadastrado 
        When selecionar Adicionar Endereco aparecerá página para editar endereço
        When digitar as informações desejadas e clicar em Salvar Endereço  
        Then aparecerá mensagem de O endereço foi salvo. 