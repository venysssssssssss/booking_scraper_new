from src.models.decision_tree_hotels import preprocess_data
from src.models.decision_tree_hotels import load_data
from src.models.decision_tree_hotels import plot_hotels


def main():
    # Load the data
    df = load_data('data\out\output_etl_data\all_hotels_pages_in_1_file.xlsx')

    # Preprocess the data
    df = preprocess_data(df)

    # Plot the hotels
    plot_hotels(df)

if __name__ == "__main__":
    main()
