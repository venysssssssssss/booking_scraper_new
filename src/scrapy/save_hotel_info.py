import os
import pandas as pd

def save_hotel_info(hotels_list):
    """
    Save the hotel information to Excel and CSV files.

    Args:
        hotels_list (list): A list of dictionaries containing hotel information.

    Returns:
        None
    """
    try:
        df = pd.DataFrame(hotels_list)
        out_dir = 'data/out'
        os.makedirs(out_dir, exist_ok=True)
        excel_file = os.path.join(out_dir, 'hotels_list.xlsx')
        csv_file = os.path.join(out_dir, 'hotels_list.csv')
        df.to_excel(excel_file, index=False)
        df.to_csv(csv_file, index=False)
        print(f'There are: {len(hotels_list)} hotels.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
