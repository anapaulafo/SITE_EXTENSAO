# Projeto: Site do Abrigo de Animais

Este é um site desenvolvido para um abrigo de animais, com o objetivo de facilitar a adoção de animais e fornecer informações importantes sobre o abrigo. Ele permite que usuários interessados visualizem animais disponíveis para adoção, conheçam a história do abrigo, entrem em contato expressando o interesse em adotar, e oferece uma página administrativa para gerenciar os animais cadastrados.

## Funcionalidades

### Para os Usuários
- **Visualizar Animais Disponíveis**: Uma galeria com fotos e descrições dos animais disponíveis para adoção.
- **História do Abrigo**: Uma seção que conta a história e missão do abrigo.
- **Formulário de Contato**: Um formulário onde o usuário pode enviar uma mensagem com seus dados e o nome do animal que deseja adotar. As informações são enviadas para o e-mail cadastrado pelo abrigo.
- **Informações de Contato**: Seção com detalhes de localização, telefone, e Instagram do abrigo.

### Para o Administrador
- **Página de Login**: Uma página protegida por senha (senha padrão que pode ser redefinida) para acessar as funcionalidades administrativas.
- **Gerenciamento de Animais**: O administrador pode:
  - **Adicionar novos animais**: Inserir fotos, nomes, e descrições dos animais.
  - **Remover animais adotados**: Excluir registros de animais que foram adotados.
  
## Tecnologias Utilizadas

- **Front-end**: HTML, CSS
- **Back-end**: Flask (framework Python)
- **Banco de Dados**: SQLite (armazenamento de informações dos animais)

## Como Usar

### Pré-requisitos
- Python 3 instalado
- Flask instalado

### Instalação

1. Clone o repositório:
2. Navegue até o diretório do projeto:
3. No console, rode o arquivo app.py:
```python app.py```
4. Abra o navegador e acesse http://127.0.0.1:5000.

### Uso da Página Administrativa
1. Acesse http://127.0.0.1:5000/admin.
2. Insira a senha 1234 para acessar o painel de administração.
3. Adicione ou remova animais conforme necessário.

## Estrutura do Projeto
- app.py: Arquivo principal que inicia o servidor Flask.
- templates/: Contém os arquivos HTML do projeto.
- static/: Contém os arquivos estáticos, como CSS, imagens e uploads.

## Customização
Alterar a senha de administrador: Modifique a variável PASSWORD no arquivo app.py.
Alterar o e-mail de contato: Atualize o e-mail abrigo@abrigo.com no arquivo app.py. (Essa funcionalidade depende de associação com API que não faz parte do projeto.)
Adicionar um logo personalizado: Substitua o arquivo de imagem no diretório static com seu logo.

Desenvolvido com ❤️ para ajudar nossos amigos de quatro patas a encontrar um lar amoroso!