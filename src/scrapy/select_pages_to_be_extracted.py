import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.scrapy.extract_hotel_info import extract_hotel_info
from src.scrapy.get_hotels import get_hotels
from src.scrapy.save_hotel_info import save_hotel_info

def scrape_pages(hotels_page):
    all_hotels_list = []
    
    try:
        # Get all elements with the XPath 'bodyconstraint-inner'
        bodyconstraint_inner_elements = hotels_page.find_elements(By.XPATH, '//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[4]/div[2]/nav/nav/div/div[2]/ol')
        
        for bodyconstraint_inner_element in bodyconstraint_inner_elements:
            # Get the ol element containing the page numbers
            WebDriverWait(bodyconstraint_inner_element, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[4]/div[2]/nav/nav/div/div[2]/ol/li[1]/button')
                )
            )
            # Get all the li elements within the ol element
            li_elements = bodyconstraint_inner_element.find_elements(By.NAME, '1')
            # Get the text of the last li element
            for element in range(len(li_elements)):
                print(li_elements[element].text)
            last_page_number_text = li_elements[-1].text
            if last_page_number_text:
                last_page_number = int(last_page_number_text)
            else:
                print('Last page number not found')
                return
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
