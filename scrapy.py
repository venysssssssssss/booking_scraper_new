import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def init_service():
    return Service(r'C:\\Users\\truks\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\msedgedriver.exe')

def init_driver(service):
    return webdriver.Edge(service=service)

def construct_url(checkin_date, checkout_date, destination):
    return f'https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&selected_currency=USD&ss={destination}&ssne={destination}&ssne_untouched={destination}&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'

def click_button(driver):
    WebDriverWait(driver, 16).until(EC.presence_of_element_located((By.XPATH, '//*[@id="b2searchresultsPage"]/div[44]/div/div/div/div[1]/div[1]/div/button'))).click()

def close_popup(driver):
    WebDriverWait(driver, 16).until(EC.element_to_be_clickable(( By.XPATH, '//button[@aria-label="Close"]'))).click()

def get_hotels(driver):
    time.sleep(5)
    return driver.find_elements(By.XPATH, '//div[@data-testid="property-card"]')

def extract_hotel_info(hotel):
    hotel_dict = {}
    hotel_dict['hotel'] = hotel.find_element(By.XPATH, './/div[@data-testid="title"]').text
    hotel_dict['price'] = hotel.find_element(By.XPATH, './/span[@data-testid="price-and-discounted-price"]').text
    hotel_dict['score'] = hotel.find_element(By.XPATH, './/div[@data-testid="review-score"]/div[1]').text
    hotel_dict['avg review'] = hotel.find_element(By.XPATH, './/div[@data-testid="review-score"]/div[2]/div[1]').text
    hotel_dict['reviews count'] = hotel.find_element(By.XPATH, './/div[@data-testid="review-score"]/div[2]/div[2]').text.split()[0]
    return hotel_dict

def save_hotel_info(hotels_list):
    df = pd.DataFrame(hotels_list)
    out_dir = 'data/out'
    os.makedirs(out_dir, exist_ok=True)
    excel_file = os.path.join(out_dir, 'hotels_list.xlsx')
    csv_file = os.path.join(out_dir, 'hotels_list.csv')
    df.to_excel(excel_file, index=False)
    df.to_csv(csv_file, index=False)
    print(f'There are: {len(hotels_list)} hotels.')

def main(checkin_date, checkout_date, destination):
    service = init_service()
    driver = init_driver(service)
    page_url = construct_url(checkin_date, checkout_date, destination)
    driver.get(page_url)
    click_button(driver)
    close_popup(driver)
    hotels = get_hotels(driver)
    hotels_list = [extract_hotel_info(hotel) for hotel in hotels]
    driver.quit()
    save_hotel_info(hotels_list)

if __name__ == '__main__':
    checkin_date = '2024-01-20'
    checkout_date = '2024-01-24'
    destination = 'Paris'
    main(checkin_date, checkout_date, destination)
