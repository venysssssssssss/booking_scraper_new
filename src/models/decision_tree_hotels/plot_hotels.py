import matplotlib.pyplot as plt
import mplcursors
import numpy as np
import pandas as pd
from src.models.decision_tree_hotels.load_data import load_data

def plot_hotels(df):
    """
    Plot hotels based on price and reviews count, with different colors for each review category.
    """
    # Create a color map for each unique review category
    colors = plt.cm.rainbow(np.linspace(0, 1, len(df['avg review'].unique())))
    color_dict = dict(zip(df['avg review'].unique(), colors))

    # Plot each review category with a different color
    for review in df['avg review'].unique():
        review_data = df[df['avg review'] == review]
        plt.scatter(
            review_data['price'],
            review_data['reviews count'],
            c=[color_dict[review]],
            label=review,
        )

    plt.xlabel('Price')
    plt.ylabel('Reviews Count')
    plt.title('Hotels')
    plt.legend()

    mplcursors.cursor(hover=True)

    plt.show()

# Adicione a linha abaixo antes de chamar a função plot_hotels(df)
# Define the "df" variable here or read it from a file

# Define the "df" variable here or read it from a file
df = pd.read_excel('data\out\output_etl_data\all_hotels_pages_in_1_file.xlsx') # Define or read the "df" variable here

df['avg review'] = df['avg review'].fillna(df['avg review'].mean())
plot_hotels(df)
