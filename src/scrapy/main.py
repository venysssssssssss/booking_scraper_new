from init_service import init_service
from init_driver import init_driver
from construct_url import construct_url
from click_button import click_button
from close_popup import close_popup
from get_hotels import get_hotels
from extract_hotel_info import extract_hotel_info
from save_hotel_info import save_hotel_info

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
    hotels = get_hotels(driver)
    hotels_list = [extract_hotel_info(hotel) for hotel in hotels]
    driver.quit()
    save_hotel_info(hotels_list)

if __name__ == '__main__':
    checkin_date = '2024-01-20'
    checkout_date = '2024-01-24'
    destination = 'Paris'
    main(checkin_date, checkout_date, destination)
