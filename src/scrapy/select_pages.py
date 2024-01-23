import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.scrapy.extract_hotel_info import extract_hotel_info
from src.scrapy.get_hotels import get_hotels
from src.scrapy.save_hotel_info import save_hotel_info


def scrape_pages(driver):
    """
    Scrape multiple pages of hotels.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        None
    """
    all_hotels_list = []

    wait = WebDriverWait(driver, 10)
    total_pages_elements = wait.until(
        EC.presence_of_all_elements_located(
            (
                By.XPATH,
                '//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[4]/div[2]/nav/nav/div/div[2]/ol/li',
            )
        )
    )
    last_page_element = total_pages_elements[-1]

    button_element = (
        last_page_element.get_attribute('innerText')
        if last_page_element
        else None
    )

    button_text = button_element
    total_pages = (
        int(button_text)
        if button_text.isdigit()
        else len(total_pages_elements)
    )

    print(f'The value of available pages for scrapy are:  {button_text}')

    while True:
        try:
            num_pages = int(input('Enter the number of pages to scrape: '))
            if 1 <= num_pages <= total_pages:
                break
            else:
                print('Please enter a valid number.')
        except ValueError:
            print('Please enter a valid number.')

    while True:
        try:
            save_per_page = int(
                input(
                    'Do you want to save each page in a file or all pages in a single file? Enter 1 for each page, 2 for all in one: '
                )
            )
            if save_per_page in [1, 2]:
                save_per_page = save_per_page == 1
                break
            else:
                print('Please enter a valid number.')
        except ValueError:
            print('Please enter a valid number.')

    current_url = None

    for i in range(num_pages):
        print(f'Scraping page {i+1}...')
        try:
            hotels = get_hotels(driver)
            hotels_list = [extract_hotel_info(hotel) for hotel in hotels]
            all_hotels_list.extend(hotels_list)

            if save_per_page:
                save_hotel_info(
                    hotels_list, f'hotels_page_{i+1}', save_per_page
                )

            if i < num_pages - 1:
                next_page_button = driver.find_element(
                    By.XPATH,
                    '//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[4]/div[2]/nav/nav/div/div[3]/button',
                )
                next_page_button.click()

                # Add an explicit wait to ensure that the URL of the next page is different
                WebDriverWait(driver, 20).until(
                    lambda driver: driver.current_url != current_url
                )
                current_url = (
                    driver.current_url
                )  # Update the current URL for the next check

        except Exception as e:
            print(f'An error occurred while scraping page {i+1}: {str(e)}')

    if not save_per_page:
        save_hotel_info(all_hotels_list, 'hotels_all_pages', save_per_page)


