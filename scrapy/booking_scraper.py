import os
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BookingScraper:
    def __init__(self, checkin_date, checkout_date, destination):
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.destination = destination

    def extract_hotel_info(self):
        service = Service(r'C:\\Users\\truks\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\msedgedriver.exe')
        driver = webdriver.Edge(service=service)

        page_url = f'https://www.booking.com/searchresults.en-us.html?checkin={self.checkin_date}&checkout={self.checkout_date}&selected_currency=USD&ss={self.destination}&ssne={self.destination}&ssne_untouched={self.destination}&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'

        driver.get(page_url)

        WebDriverWait(driver, 16).until(EC.presence_of_element_located((By.XPATH, '//*[@id="b2searchresultsPage"]/div[44]/div/div/div/div[1]/div[1]/div/button'))).click()

        WebDriverWait(driver, 16).until(EC.element_to_be_clickable(( By.XPATH, '//button[@aria-label="Close"]'))).click()
        

        time.sleep(5)
        hotels = driver.find_elements(By.XPATH, '//div[@data-testid="property-card"]')

        hotels_list = []
        for hotel in hotels:
            hotel_dict = {}
            hotel_dict['hotel'] = hotel.find_element(By.XPATH, './/div[@data-testid="title"]').text
            hotel_dict['price'] = hotel.find_element(By.XPATH, './/span[@data-testid="price-and-discounted-price"]').text
            hotel_dict['score'] = hotel.find_element(By.XPATH, './/div[@data-testid="review-score"]/div[1]').text
            hotel_dict['avg review'] = hotel.find_element(By.XPATH, './/div[@data-testid="review-score"]/div[2]/div[1]').text
            hotel_dict['reviews count'] = hotel.find_element(By.XPATH, './/div[@data-testid="review-score"]/div[2]/div[2]').text.split()[0]

            hotels_list.append(hotel_dict)

        driver.quit()

        return hotels_list

    def save_hotel_info(self, hotels_list):
        df = pd.DataFrame(hotels_list)
        out_dir = 'data/out'
        os.makedirs(out_dir, exist_ok=True)
        excel_file = os.path.join(out_dir, 'hotels_list.xlsx')
        csv_file = os.path.join(out_dir, 'hotels_list.csv')
        df.to_excel(excel_file, index=False)
        df.to_csv(csv_file, index=False)
        print(f'There are: {len(hotels_list)} hotels.')

    def main(self):
        hotels_list = self.extract_hotel_info()
        self.save_hotel_info(hotels_list)


if __name__ == '__main__':
    checkin_date = '2024-01-20'
    checkout_date = '2024-01-24'
    destination = 'Paris'

    scraper = BookingScraper(checkin_date, checkout_date, destination)
    scraper.main()
