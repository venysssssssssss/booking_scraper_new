import matplotlib.pyplot as plt
import mplcursors
import numpy as np
import pandas as pd
from src.models.decision_tree_hotels.view_best_hotels import review_mapping

def load_data(file_path):
    """
    Load data from an Excel file and return a DataFrame.
    """
    df = pd.read_excel(file_path)
    return df

def preprocess_data(df):
    """
    Preprocess the data by removing symbols, converting columns to appropriate data types,
    and mapping categories to numbers.
    """
    df['price'] = df['price'].str.replace('US$', '').str.replace(',', '').astype(float)
    
    review_mapping = {
        'Good': 1,
        'Very Good': 2,
        'Wonderful': 3,
        'Review score': 4,
        'Excellent': 5,
        'Exceptional': 6,
    }
    df['avg review'] = df['avg review'].map(review_mapping)
    
    df['reviews count'] = df['reviews count'].str.replace(',', '').astype(float)
    
    return df

def plot_hotels(df):
    """
    Plot hotels based on price and reviews count, with different colors for each review category.
    """
    colors = plt.cm.rainbow(np.linspace(0, 1, len(df['avg review'].unique())))
    color_dict = dict(zip(df['avg review'].unique(), colors))

    for review in df['avg review'].unique():
        review_data = df[df['avg review'] == review]
        plt.scatter(
            review_data['price'],
            review_data['reviews count'],
            c=[color_dict[review]],
            label=list(review_mapping.keys())[
                list(review_mapping.values()).index(review)
            ],
        )

    plt.xlabel('Price')
    plt.ylabel('Reviews Count')
    plt.title('Hotels')
    plt.legend()
    
    mplcursors.cursor(hover=True)
    
    plt.show()

def main():
    # Load the data
    df = load_data('data/out/output_etl_data/all_hotels_pages_in_1_file.xlsx')

    # Preprocess the data
    df = preprocess_data(df)

    # Plot the hotels
    plot_hotels(df)

if __name__ == "__main__":
    main()
