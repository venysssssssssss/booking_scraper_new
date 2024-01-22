import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import numpy as np

# Carregar os dados
df = pd.read_excel('data/out/output_etl_data/all_hotels_pages_in_1_file.xlsx')

# Remover o símbolo do dólar e a vírgula, e converter a coluna 'price' para float
df['price'] = df['price'].str.replace('US$', '').str.replace(',', '').astype(float)

# Mapear as categorias de avaliação para números
review_mapping = {
    'Good': 1,
    'Very Good': 2,
    'Wonderful': 3,
    'Review score': 4,
    'Excellent': 5,
    'Exceptional': 6
}
df['avg review'] = df['avg review'].map(review_mapping)

# Remover a vírgula e converter a coluna 'reviews count' para float
df['reviews count'] = df['reviews count'].str.replace(',', '').astype(float)

# Criar uma lista de cores
colors = plt.cm.rainbow(np.linspace(0, 1, len(review_mapping)))

# Criar um dicionário para mapear cada avaliação a uma cor
color_dict = dict(zip(review_mapping.values(), colors))

# Plotar os hotéis
for review in review_mapping.values():
    review_data = df[df['avg review'] == review]
    plt.scatter(review_data['price'], review_data['reviews count'], c=[color_dict[review]], label=list(review_mapping.keys())[list(review_mapping.values()).index(review)])

plt.xlabel('Price')
plt.ylabel('Reviews Count')
plt.title('Hotels')
plt.legend()

# Adicionar interatividade ao gráfico
mplcursors.cursor(hover=True)

plt.show()
