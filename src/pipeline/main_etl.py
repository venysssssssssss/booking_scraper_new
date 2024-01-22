from src.etl.extract import extract_from_excel
from src.etl.load import load_to_excel
from src.etl.transform import contact_dataframes

if __name__ == '__main__':
    # Extract
    data_frame_list = extract_from_excel(
        'data\\out\\all_hotels_splitted_files'
    )

    print('Extracted DataFrames:')
    print(data_frame_list)

    if not data_frame_list:
        print('No DataFrames to process. Exiting.')
        exit()

    # Transform
    data_frame = contact_dataframes(data_frame_list)

    print('Concatenated DataFrame:')
    print(data_frame)

    # Load
    load_to_excel(data_frame, 'data\\out\\output_etl_data', 'all_hotels_pages_in_1_file')
    
    # Substring
    substring = 'all_hotels_pages_in_1_file'[4:9]
    print('Substring:', substring)
