import os
import pandas as pd

def save_hotel_info(self, hotels_list):
        df = pd.DataFrame(hotels_list)
        out_dir = 'data/out'
        os.makedirs(out_dir, exist_ok=True)
        excel_file = os.path.join(out_dir, 'hotels_list.xlsx')
        csv_file = os.path.join(out_dir, 'hotels_list.csv')
        df.to_excel(excel_file, index=False)
        df.to_csv(csv_file, index=False)
        print(f'There are: {len(hotels_list)} hotels.')