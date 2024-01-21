from src.scrapy.click_button import click_button
from src.scrapy.close_popup import close_popup
from src.scrapy.construct_url import construct_url
from src.scrapy.extract_hotel_info import extract_hotel_info
from src.scrapy.get_hotels import get_hotels
from src.scrapy.init_driver import init_driver
from src.scrapy.init_service import init_service
from src.scrapy.save_hotel_info import save_hotel_info
from src.scrapy.select_pages import scrape_pages


def main(checkin_date, checkout_date, destination):
    """
    This function is the main entry point of the booking scraper program.

    Args:
        checkin_date (str): The check-in date in the format 'YYYY-MM-DD'.
        checkout_date (str): The check-out date in the format 'YYYY-MM-DD'.
        destination (str): The destination for the hotel search.
    """
    driver = init_driver()
    page_url = construct_url(checkin_date, checkout_date, destination)
    driver.get(page_url)
    click_button(driver)
    close_popup(driver)
    scrape_pages(driver)


if __name__ == '__main__':
    checkin_date = '2024-01-26'
    checkout_date = '2024-02-30'
    destination = 'Paris'
    main(checkin_date, checkout_date, destination)
