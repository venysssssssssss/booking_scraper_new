# Documentação do Script de Análise de Hotéis

O script `hotel_analysis.py` realiza a análise visual de hotéis com base em dados carregados de um arquivo Excel gerado pelo processo ETL. O script utiliza a biblioteca Matplotlib para criar um gráfico de dispersão, onde os hotéis são representados de acordo com o preço (diária) e o número de avaliações, com diferentes cores indicando diferentes categorias de avaliação.

## Função `load_data`

### Descrição

A função `load_data(file_path)` carrega dados de um arquivo Excel e retorna um DataFrame do Pandas.

### Parâmetros

- `file_path` (str): Caminho do arquivo Excel a ser carregado.

### Retorno

- DataFrame do Pandas contendo os dados do arquivo Excel.

## Função `preprocess_data`

### Descrição

A função `preprocess_data(df)` realiza o pré-processamento dos dados, removendo símbolos, convertendo colunas para tipos de dados apropriados e mapeando categorias para números.

### Parâmetros

- `df` (pd.DataFrame): DataFrame do Pandas contendo os dados a serem pré-processados.

### Retorno

- Tupla contendo o DataFrame pré-processado e um dicionário de mapeamento para as categorias de avaliação.

## Função `plot_hotels`

### Descrição

A função `plot_hotels(df, review_mapping)` gera um gráfico de dispersão para os hotéis com base no preço e no número de avaliações, usando cores diferentes para cada categoria de avaliação.

### Parâmetros

- `df` (pd.DataFrame): DataFrame do Pandas contendo os dados dos hotéis.
- `review_mapping` (dict): Dicionário de mapeamento para as categorias de avaliação.

### Retorno

- Nenhum (o gráfico é exibido).

## Função `main`

### Descrição

A função `main()` é a função principal que orquestra o carregamento dos dados, o pré-processamento e a geração do gráfico de dispersão.

### Parâmetros

- Nenhum.

### Retorno

- Nenhum (o gráfico é exibido).

## Uso

- Execute o script para visualizar o gráfico de dispersão dos hotéis.

```bash
python hotel_analysis.py
