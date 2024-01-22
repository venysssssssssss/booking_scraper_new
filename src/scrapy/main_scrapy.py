import time

from close_popup import close_popup
from construct_url import construct_url
from extract_hotel_info import extract_hotel_info
from get_hotels import get_hotels
from init_service import init_service
from save_hotel_info import save_hotel_info
from select_pages import scrape_pages
from selenium import webdriver


def main(checkin_date, checkout_date, destination):
    """
    Main function to scrape hotel information.

    Args:
        checkin_date (str): The check-in date in the format 'YYYY-MM-DD'.
        checkout_date (str): The check-out date in the format 'YYYY-MM-DD'.
        destination (str): The destination city.

    Returns:
        None
    """
    service = init_service()
    driver = webdriver.Edge(service=service)

    url = construct_url(
        checkin_date,
        checkout_date,
        destination,
        adults,
        rooms,
        children,
        currency,
    )

    driver.get(url)

    close_popup(driver)

    scrape_pages(driver)

    driver.quit()


if __name__ == '__main__':
    checkin_date = '2024-02-15'
    checkout_date = '2024-2-30'
    destination = 'Rio de Janeiro'
    adults = 1
    rooms = 1
    children = 0
    currency = 'USD'
    main(checkin_date, checkout_date, destination)
