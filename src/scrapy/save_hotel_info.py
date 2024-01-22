import os

import pandas as pd


def save_hotel_info(hotels_list, filename, save_per_page):
    """
    Save the hotel information to Excel and CSV files.

    Args:
        hotels_list (list): A list of dictionaries containing hotel information.
        filename (str): The base filename to use for the output files.
        save_per_page (bool): Whether to save each page in a separate file.

    Returns:
        None
    """
    try:
        df = pd.DataFrame(hotels_list)
        out_dir_all_hotels = 'data\out\all_hotels_files'
        out_dir_all_hotels_splitted = 'data\out\all_hotels_splitted_files'  
        os.makedirs(out_dir_all_hotels, exist_ok=True)
        if save_per_page:
            excel_file = os.path.join(out_dir_all_hotels_splitted, f'{filename}.xlsx')
        else:
            excel_file = os.path.join(out_dir_all_hotels, 'all_hotels.xlsx')
            csv_file = os.path.join(out_dir_all_hotels, 'all_hotels.csv')
        df.to_excel(excel_file, index=False)
        df.to_csv(csv_file, index=False)
        print(f'There are: {len(hotels_list)} hotels.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
