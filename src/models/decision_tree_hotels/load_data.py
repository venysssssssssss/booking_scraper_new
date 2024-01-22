import pandas as pd

def load_data(file_path):
    """
    Load data from an Excel file and return a DataFrame.
    """
    df = pd.read_excel(file_path)
    return df