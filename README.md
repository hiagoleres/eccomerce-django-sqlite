# MercadoShops - Plataforma de E-commerce

O MercadoShops é uma plataforma de e-commerce especializada em produtos de tecnologia. Este projeto foi concebido para a avaliação P2 da disciplina de Tópicos Especiais de Informática, sendo desenvolvido no framework Django.

## Funcionalidades Principais

- **Autenticação**: Autenticação de usuários atravez do Django Autenticate

- **Gestão de Produtos**: Adição de arquivos e relatórios

- **Carrinho de Compras e checkout**: Carrinho de compras salvo no banco de dados e tela de checkout

## Requisitos para Execução

Certifique-se de atender aos seguintes requisitos antes de iniciar o projeto:

1. **Python**: Django é um framework Python. Certifique-se de ter o Python instalado (versão 3.6 ou superior). Baixe [aqui](https://www.python.org/downloads/).

2. **Ambiente Virtual (Opcional, mas recomendado)**: Crie um ambiente virtual para isolar as dependências do projeto. Execute:

    ```bash
    python -m venv venv
    ```

    Ative o ambiente virtual:

    - No Windows:

    ```bash
    venv\Scripts\activate
    ```

    - No macOS e Linux:

    ```bash
    source venv/bin/activate
    ```

3. **Instalação do Django**: Instale o Django usando o pip:

    ```bash
    pip install django
    ```

4. **Configuração do Projeto Django**: No diretório do projeto, execute:

    ```bash
    python manage.py migrate
    ```

5. **Criar um Superusuário (Opcional, mas muitas vezes útil)**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Executar o Servidor de Desenvolvimento**:

    ```bash
    python manage.py runserver
    ```

    Acesse o projeto em `http://localhost:8000` no navegador.
