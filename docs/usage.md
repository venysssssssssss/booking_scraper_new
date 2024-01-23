# Uso do Selenium

O Selenium é uma ferramenta de automação de navegador amplamente utilizada para testes e scraping da web. Nesta seção, vamos explorar como usar o Selenium em projetos Python.

## Instalação

Antes de começar, certifique-se de ter o Python e o pip instalados em seu sistema. Em seguida, siga as etapas abaixo para instalar o Selenium:

1. Instale o Pyenv para gerenciar suas versões do Python:
    ```bash
    $ pip install pyenv
    ```

2. Instale o Poetry para gerenciar as dependências do projeto:
    ```bash
    $ pip install poetry
    ```

3. Crie um ambiente virtual com a versão correta do Python usando o Pyenv:
    ```bash
    $ pyenv install 3.11.3
    $ pyenv virtualenv 3.11.3 myenv
    $ pyenv activate myenv
    ```

4. Instale os pacotes usando o Poetry:
    ```bash
    $ poetry install
    ```

## Exemplo de Uso

Aqui está um exemplo básico de como usar o Selenium para automatizar ações em um navegador:
```from selenium import webdriver```

# Inicializar o driver do Selenium
```driver = webdriver.Chrome()```

# Abrir uma página da web
```driver.get("https://www.example.com")```

# Localizar um elemento na página e interagir com ele
```element = driver.find_element_by_id("my-element")```
```element.click()```

# Fechar o navegador
```driver.quit()```
