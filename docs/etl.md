   - [ `extract`](#extract)
   - [ `load`](#load)
   - [ `transform`](#transform)
   - [ `main_etl`](#main_etl)


# Documentação da Função `extract_from_excel` <a name="extract"></a>

## Descrição

A função `extract_from_excel` lê os arquivos Excel de uma pasta específica e retorna uma lista de DataFrames do Pandas.

## Parâmetros

- `path` (str): O caminho para a pasta contendo os arquivos Excel a serem lidos.

## Retorno

- Uma lista de DataFrames do Pandas, cada um representando o conteúdo de um arquivo Excel na pasta especificada.

## Funcionamento

1. **Listagem de Arquivos**: Utiliza a biblioteca `glob` para listar todos os arquivos Excel (`*.xlsx`) no diretório especificado pelo caminho.

2. **Leitura dos Arquivos**: Itera sobre a lista de arquivos e utiliza a biblioteca `pandas` para ler cada arquivo Excel como um DataFrame.

3. **Construção da Lista de DataFrames**: Adiciona cada DataFrame à lista `data_frame_list`.

4. **Retorno**: Retorna a lista completa de DataFrames, cada um representando o conteúdo de um arquivo Excel na pasta especificada.

## Uso

- A função pode ser chamada diretamente a partir do script, lendo os arquivos Excel da pasta especificada e exibindo a lista de DataFrames resultante.

```if __name__ == '__main__':
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)


# Documentação da Função `load_to_excel` <a name="load"></a>

## Descrição

A função `load_to_excel` recebe um DataFrame do Pandas e o salva como um arquivo Excel (.xlsx) em um caminho especificado.

## Parâmetros

- `data_frame` (pd.DataFrame): O DataFrame a ser salvo como um arquivo Excel.
- `output_path` (str): O caminho onde o arquivo Excel será salvo.
- `output_file_name` (str): O nome do arquivo a ser salvo.

## Retorno

- Uma string indicando que o arquivo foi salvo com sucesso.

## Funcionamento

1. **Verificação do Diretório de Saída**: Verifica se o diretório de saída especificado (`output_path`) existe. Se não existir, o cria.

2. **Salvamento como Excel**: Utiliza o método `to_excel` do Pandas para salvar o DataFrame como um arquivo Excel (.xlsx) no caminho especificado.

3. **Retorno de Sucesso**: Retorna a mensagem "Arquivo salvo com sucesso".

## Uso

- A função pode ser chamada com um DataFrame, um caminho de saída e um nome de arquivo para salvar o DataFrame como um arquivo Excel.

```python
data_frame = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']})
output_path = 'output_folder'
output_file_name = 'output_file'
result = load_to_excel(data_frame, output_path, output_file_name)
print(result)


# Documentação da Função `contact_dataframes`

## Descrição

A função `contact_dataframes` recebe uma lista de DataFrames do Pandas e os concatena em um único DataFrame.

## Parâmetros

- `data_frame_list` (List[pd.DataFrame]): A lista de DataFrames a serem concatenados.

## Retorno

- Um único DataFrame resultante da concatenação dos DataFrames da lista.

## Funcionamento

1. **Concatenação dos DataFrames**: Utiliza o método `pd.concat` do Pandas para concatenar os DataFrames da lista em um único DataFrame.

2. **Ignorar Índices Antigos**: O parâmetro `ignore_index=True` é utilizado para redefinir os índices do DataFrame resultante.

3. **Retorno do DataFrame Concatenado**: Retorna o DataFrame resultante da concatenação.

## Uso

- A função pode ser chamada com uma lista de DataFrames para obter um único DataFrame concatenado.

```python
data_frame_list = [df1, df2, df3]  # Substitua df1, df2, df3 pelos seus DataFrames
result_dataframe = contact_dataframes(data_frame_list)
print(result_dataframe)


# Script ETL - Extração, Transformação e Carregamento <a name="main_etl"></a>

Este script realiza as etapas de Extração (Extract), Transformação (Transform) e Carregamento (Load) de dados usando pandas.

## Importação de Módulos

```python
from src.pipeline.extract import extract_from_excel
from src.pipeline.load import load_to_excel
from src.pipeline.transform import contact_dataframes





