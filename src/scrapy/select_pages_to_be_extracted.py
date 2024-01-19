import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.scrapy.extract_hotel_info import extract_hotel_info
from src.scrapy.get_hotels import get_hotels
from src.scrapy.save_hotel_info import save_hotel_info

def scrape_pages(li_elements):
    all_hotels_list = []
    
    try:
        # Extract the numbers from the li elements
        last_page_numbers = [int(element.text) for element in li_elements]
        last_page_number = max(last_page_numbers)
    except Exception as e:
        print(f'An error occurred: {e}')
        return

    while True:
        try:
            num_pages = int(input(f'Enter the number of pages to scrape (1-{last_page_number}): '))
            if 1 <= num_pages <= last_page_number:
                break
            else:
                print('Please enter a valid number.')
        except ValueError:
            print('Please enter a valid number.')

    save_option = int(input('Enter 1 to save each page separately, or 2 to save all in one file: '))

    for i in range(1, num_pages + 1):
        print(f'Scraping page {i}...')
        hotels = get_hotels(hotels)
        hotels_list = [extract_hotel_info(hotel) for hotel in hotels]
        all_hotels_list.extend(hotels_list)

        if save_option == 1:
            save_hotel_info(hotels_list, f'hotels_page_{i}', False)
        elif save_option == 2 and i == num_pages:
            save_hotel_info(all_hotels_list, 'all_hotels', True)

        if i < num_pages:
            next_page_button = hotels.find_element(
                By.XPATH,
                '//*[@id="pagination"]/ul/li[@class="bui-pagination__next-arrow"]/a',
            )
            next_page_button.click()
            WebDriverWait.until(EC.staleness_of(next_page_button))
