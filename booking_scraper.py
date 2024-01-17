import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main():
    
    service = Service(r'C:\\Users\\truks\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\msedgedriver.exe')
    driver = webdriver.Edge(service=service)
    
    # IMPORTANT: Change dates to future dates, otherwise it won't work
    checkin_date = '2024-01-20'
    checkout_date = '2024-01-24'
    
    page_url = f'https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&selected_currency=USD&ss=Paris&ssne=Paris&ssne_untouched=Paris&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'

    driver.get(page_url)

    WebDriverWait(driver, 16).until(EC.presence_of_element_located((By.XPATH, '//*[@id="b2searchresultsPage"]/div[44]/div/div/div/div[1]/div[1]/div/button'))).click()

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

    df = pd.DataFrame(hotels_list)
    df.to_excel('hotels_list.xlsx', index=False) 
    df.to_csv('hotels_list.csv', index=False) 
    print(f'There are: {len(hotels)} hotels.')

if __name__ == '__main__':
    main()
