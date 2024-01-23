# Documentação de Web Scraping

Esta documentação fornece uma visão geral de um script modularizado de web scraping para extrair informações de hotéis do Booking.com. O script está dividido em vários arquivos, cada um com um propósito específico. Os módulos incluem funções para inicializar o WebDriver, construir URLs, clicar em botões, extrair informações de hotéis, salvar dados em arquivos e fazer scraping de várias páginas.

## Tabela de Conteúdos

   - [Introdução](#introdução)
   - [Configuração](#configuração)
   - [Pré-requisitos](#pré-requisitos)
   - [Instalação](#instalação)
   - [Detalhes dos Módulos](#detalhes-dos-módulos)
   - [ `click_button`](#click_button)
   - [ `close_popup`](#close_popup)
   - [ `construct_url`](#construct_url)
   - [ `extract_hotel_info`](#extract_hotel_info)
   - [ `get_hotels`](#get_hotels)
   - [ `init_driver` e `init_service`](#init_driver-e-init_service)
   - [ `main`](#main)
   - [ `save_hotel_info`](#save_hotel_info)
   - [ `scrape_pages`](#scrape_pages)

## 1. Introdução <a name="introdução"></a>

Este script de web scraping foi projetado para extrair informações de hotéis do Booking.com, oferecendo uma estrutura modular e fácil de manter. Ele utiliza o Selenium WebDriver para navegar pelo site, interagir com elementos e extrair dados.


### 2. Pré-requisitos <a name="pré-requisitos"></a>

- Python 3.11.3
- Selenium
- pandas

### 3. Instalação <a name="instalação"></a>

Instale os pacotes necessários usando os seguintes comandos:

```poetry install ```

# Documentação da Função `click_button` <a name="click_button"></a>

## Descrição

A função `click_button` é utilizada para clicar em um botão em uma página da web, fazendo uso do driver fornecido.

## Parâmetros

- `driver`: A instância do WebDriver utilizada para interagir com a página da web.

## Exceções

A função pode gerar uma exceção do tipo `Exception` caso ocorra um erro durante o processo de clicar no botão.

## Código

Aqui está o código-fonte da função `click_button`:

```python
def click_button(driver):
    """
    Clica em um botão em uma página da web.

    :param driver: A instância do WebDriver utilizada para interagir com a página da web.
    :type driver: WebDriver

    :raises Exception: Se ocorrer um erro ao clicar no botão.
    """
    try:
        # Substitua esta linha pelo código específico para localizar e clicar no botão
    except Exception as e:
        raise Exception("Erro ao clicar no botão: {}".format(str(e)))

# Documentação da Função `close_popup` <a name="close_popup"></a>

## Descrição

A função `close_popup` é utilizada para fechar uma janela de pop-up clicando na tela.

## Parâmetros

- `driver`: A instância do WebDriver utilizada para interagir com a página da web.

## Exceções

A função pode gerar uma exceção do tipo `Exception` caso ocorra um erro durante o processo de fechamento do pop-up.

## Código

Aqui está o código-fonte da função `close_popup`:

```python
def close_popup(driver):
    """
    Fecha a janela de pop-up clicando na tela.

    :param driver: A instância do WebDriver utilizada para interagir com a página da web.
    :type driver: WebDriver

    :raises Exception: Se ocorrer um erro ao fechar o pop-up.
    """
    try:
        wait = WebDriverWait(driver, 15)
        element_present = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="b2searchresultsPage"]/div[49]/div/div/div',
                )
            )
        )
        click_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="b2searchresultsPage"]/div[48]/div/div/div/div[1]/div[1]/div/button',
                )
            )
        )
        if element_present and click_button:
            time.sleep(2)  # Aguarda por 2 segundos antes de clicar
            click_button.click()
            wait.until_not(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="b2searchresultsPage"]/div[49]/div/div/div',
                    )
                )
            )
    except Exception as e:
        print(f'Um erro ocorreu ao fechar o pop-up: {str(e)}')


# Documentação da Função `construct_url` <a name="construct_url"></a>

## Descrição

A função `construct_url` constrói uma URL para os resultados de busca do Booking.com com base nas informações fornecidas.

## Parâmetros

- `checkin_date` (str): A data de check-in no formato 'AAAA-MM-DD'.
- `checkout_date` (str): A data de check-out no formato 'AAAA-MM-DD'.
- `destination` (str): A cidade de destino para a pesquisa.
- `adults` (int): O número de adultos.
- `rooms` (int): O número de quartos.
- `children` (int): O número de crianças.
- `currency` (str): A moeda desejada.

## Retorno

- `str`: A URL construída.

## Exceções

A função pode gerar uma exceção do tipo `Exception` se ocorrer um erro durante a construção da URL.

## Código

Aqui está o código-fonte da função `construct_url`:

```python
def construct_url(
    checkin_date, checkout_date, destination, adults, rooms, children, currency
):
    """
    Constrói uma URL para os resultados de busca do Booking.com com base nas informações fornecidas.

    :param checkin_date: A data de check-in no formato 'AAAA-MM-DD'.
    :type checkin_date: str
    :param checkout_date: A data de check-out no formato 'AAAA-MM-DD'.
    :type checkout_date: str
    :param destination: A cidade de destino para a pesquisa.
    :type destination: str
    :param adults: O número de adultos.
    :type adults: int
    :param rooms: O número de quartos.
    :type rooms: int
    :param children: O número de crianças.
    :type children: int
    :param currency: A moeda desejada.
    :type currency: str

    :return: A URL construída.
    :rtype: str

    :raises Exception: Se ocorrer um erro durante a construção da URL.
    """
    try:
        url = f'https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&selected_currency={currency}&ss={destination}&ssne={destination}&ssne_untouched={destination}&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults={adults}&no_rooms={rooms}&group_children={children}&sb_travel_purpose=leisure'
        return url
    except Exception as e:
        print(f'Um erro ocorreu: {e}')


# Documentação da Função `extract_hotel_info` <a name="extract_hotel_info"></a>

## Descrição

A função `extract_hotel_info` extrai informações de um elemento de hotel e retorna um dicionário.

## Parâmetros

- `hotel`: O elemento do hotel a partir do qual extrair informações.

## Retorno

- `dict`: Um dicionário contendo as informações extraídas. As chaves são 'hotel', 'price', 'score', 'avg review' e 'reviews count'. Os valores são os valores correspondentes extraídos do elemento do hotel.

## Código

Aqui está o código-fonte da função `extract_hotel_info`:

```python
def extract_hotel_info(hotel):
    """
    Extrai informações de um elemento de hotel e retorna um dicionário.

    :param hotel: O elemento do hotel a partir do qual extrair informações.

    :return: Um dicionário contendo as informações extraídas. As chaves são 'hotel', 'price', 'score', 'avg review' e 'reviews count'. Os valores são os valores correspondentes extraídos do elemento do hotel.
    :rtype: dict
    """
    hotel_dict = {}
    try:
        title_element = hotel.find_element(
            By.XPATH, './/div[@data-testid="title"]'
        )
        hotel_dict['hotel'] = (
            title_element.get_attribute('innerText') if title_element else None
        )
    except:
        hotel_dict['hotel'] = None
    try:
        price_element = hotel.find_element(
            By.XPATH, './/span[@data-testid="price-and-discounted-price"]'
        )
        hotel_dict['price'] = (
            price_element.get_attribute('innerText') if price_element else None
        )
    except:
        hotel_dict['price'] = None
    try:
        score_element = hotel.find_element(
            By.XPATH, './/div[@data-testid="review-score"]/div[1]'
        )
        hotel_dict['score'] = (
            score_element.get_attribute('innerText') if score_element else None
        )
    except:
        hotel_dict['score'] = None
    try:
        avg_review_element = hotel.find_element(
            By.XPATH, './/div[@data-testid="review-score"]/div[2]/div[1]'
        )
        hotel_dict['avg review'] = (
            avg_review_element.get_attribute('innerText')
            if avg_review_element
            else None
        )
    except:
        hotel_dict['avg review'] = None
    try:
        reviews_count_element = hotel.find_element(
            By.XPATH, './/div[@data-testid="review-score"]/div[2]/div[2]'
        )
        hotel_dict['reviews count'] = (
            reviews_count_element.get_attribute('innerText').split()[0]
            if reviews_count_element
            else None
        )
    except:
        hotel_dict['reviews count'] = None
    return hotel_dict


# Documentação da Função `get_hotels` <a name="get_hotels"></a>

## Descrição

A função `get_hotels` obtém uma lista de hotéis do driver fornecido.

## Parâmetros

- `driver`: A instância do WebDriver.

## Retorno

- `list`: Uma lista de objetos WebElement representando os hotéis.

## Código

Aqui está o código-fonte da função `get_hotels`:

```python
def get_hotels(driver):
    """
    Obtém uma lista de hotéis do driver fornecido.

    :param driver: A instância do WebDriver.

    :return: Uma lista de objetos WebElement representando os hotéis.
    :rtype: list
    """
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, './/div[@data-testid="property-card"]')
        )
    )
    return driver.find_elements(
        By.XPATH, './/div[@data-testid="property-card"]'
    )


# Documentação da Função `init_driver` <a name="init_driver"></a>

## Descrição

A função `init_driver` inicializa e retorna uma instância do WebDriver para o navegador Edge.

## Retorno

- `WebDriver`: Uma instância do WebDriver para o navegador Edge.

## Código

Aqui está o código-fonte da função `init_driver`:

```python
def init_driver():
    """
    Inicializa e retorna uma instância do WebDriver para o navegador Edge.

    :return: Uma instância do WebDriver para o navegador Edge.
    :rtype: WebDriver
    """
    service = init_service()
    return webdriver.Edge(service=service)

# Documentação da Função `init_service` <a name="init_service"></a>

## Descrição

A função `init_service` inicializa e retorna um objeto Service para o WebDriver do Microsoft Edge.

## Retorno

- `Service`: Um objeto Service para o WebDriver do Microsoft Edge.

## Código

Aqui está o código-fonte da função `init_service`:

```python
def init_service():
    """
    Inicializa e retorna um objeto Service para o WebDriver do Microsoft Edge.

    :return: Um objeto Service para o WebDriver do Microsoft Edge.
    :rtype: Service
    """
    return Service(
        r'C:\\Users\\truks\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\msedgedriver.exe'
    )

# Documentação da Função `main` <a name="main"></a>

## Descrição

A função `main` é a função principal para extrair informações de hotéis.

## Parâmetros

- `checkin_date` (str): A data de check-in no formato 'AAAA-MM-DD'.
- `checkout_date` (str): A data de check-out no formato 'AAAA-MM-DD'.
- `destination` (str): A cidade de destino.
- `adults` (int): O número de adultos.
- `rooms` (int): O número de quartos.
- `children` (int): O número de crianças.
- `currency` (str): A moeda desejada.

## Código

Aqui está o código-fonte da função `main`:

```python
def main(checkin_date, checkout_date, destination):
    """
    Função principal para extrair informações de hotéis.

    :param checkin_date: A data de check-in no formato 'AAAA-MM-DD'.
    :type checkin_date: str
    :param checkout_date: A data de check-out no formato 'AAAA-MM-DD'.
    :type checkout_date: str
    :param destination: A cidade de destino.
    :type destination: str

    :return: None
    """
    service = init_service()
    driver = webdriver.Edge(service=service)

    url = construct_url(
        checkin_date,
        checkout_date,
        destination,
        adults,
        rooms,
        children,
        currency,
    )

    driver.get(url)

    close_popup(driver)

    scrape_pages(driver)

    driver.quit()


if __name__ == '__main__':
    checkin_date = '2024-02-15'
    checkout_date = '2024-2-30'
    destination = 'Rio de Janeiro'
    adults = 1
    rooms = 1
    children = 0
    currency = 'USD'
    main(checkin_date, checkout_date, destination)


# Documentação da Função `save_hotel_info` <a name="save_hotel_info"></a>

## Descrição

A função `save_hotel_info` salva as informações do hotel em arquivos Excel e CSV.

## Parâmetros

- `hotels_list` (list): Uma lista de dicionários contendo informações do hotel.
- `filename` (str): O nome base do arquivo a ser usado para os arquivos de saída.
- `save_per_page` (bool): Se salvar cada página em um arquivo separado.

## Código

Aqui está o código-fonte da função `save_hotel_info`:

```python
def save_hotel_info(hotels_list, filename, save_per_page):
    """
    Salva as informações do hotel em arquivos Excel e CSV.

    :param hotels_list: Uma lista de dicionários contendo informações do hotel.
    :type hotels_list: list
    :param filename: O nome base do arquivo a ser usado para os arquivos de saída.
    :type filename: str
    :param save_per_page: Se salvar cada página em um arquivo separado.
    :type save_per_page: bool

    :return: None
    """
    try:
        df = pd.DataFrame(hotels_list)
        out_dir = 'data/out'
        os.makedirs(out_dir, exist_ok=True)
        if save_per_page:
            excel_file = os.path.join(
                out_dir, 'all_hotels_splitted_files', f'{filename}.xlsx'
            )
        else:
            excel_file = os.path.join(
                out_dir, 'all_hotels_files', 'all_hotels.xlsx'
            )
            csv_file = os.path.join(
                out_dir, 'all_hotels_files', 'all_hotels.csv'
            )
        df.to_excel(excel_file, index=False)
        if not save_per_page:
            df.to_csv(csv_file, index=False)
        print(f'There are: {len(hotels_list)} hotels.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Documentação da Função `scrape_pages`

## Descrição

A função `scrape_pages` é responsável por extrair informações de múltiplas páginas de hotéis em um site usando Selenium WebDriver.

## Parâmetros

- `driver`: Uma instância do Selenium WebDriver utilizada para interagir com a página da web.

## Retorno

A função não possui um retorno explícito. Ela realiza a extração de informações de hotéis e, opcionalmente, salva os resultados em arquivos.

## Funcionamento

1. **Inicialização**: A função inicializa uma lista vazia chamada `all_hotels_list` para armazenar as informações dos hotéis.

2. **Obtenção do Número de Páginas**: Utilizando Selenium, a função identifica o número total de páginas disponíveis para extração, com base nos elementos da barra de navegação.

3. **Input do Usuário**: Solicita ao usuário que informe o número desejado de páginas a serem extraídas e se deseja salvar cada página em um arquivo separado ou todas as páginas em um único arquivo.

4. **Loop de Extração por Página**: Itera sobre o número de páginas fornecido pelo usuário.

    a. **Extração de Hotéis**: Utiliza a função `get_hotels` para obter a lista de hotéis da página atual.
    
    b. **Extração de Informações**: Utiliza a função `extract_hotel_info` para obter as informações de cada hotel na página.
    
    c. **Acumulação de Dados**: Adiciona as informações dos hotéis à lista `all_hotels_list`.
    
    d. **Salvamento Opcional por Página**: Se o usuário optou por salvar cada página separadamente, utiliza a função `save_hotel_info` para salvar as informações dos hotéis da página atual em um arquivo.

    e. **Navegação para a Próxima Página**: Se ainda houver páginas a serem extraídas, clica no botão da próxima página e aguarda uma mudança na URL para garantir que a página foi carregada completamente.

5. **Salvamento Final**: Se o usuário optou por salvar todas as páginas em um único arquivo, utiliza a função `save_hotel_info` para salvar todas as informações dos hotéis em um arquivo.

## Exceções

- Em caso de erro durante o processo de extração de informações de uma página, a exceção é capturada e uma mensagem é exibida indicando a ocorrência do erro.
