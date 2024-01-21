import time
from selenium import webdriver
from init_service import init_service
from close_popup import close_popup
from construct_url import construct_url
from extract_hotel_info import extract_hotel_info
from get_hotels import get_hotels
from save_hotel_info import save_hotel_info
from select_pages import scrape_pages

def main(checkin_date, checkout_date, destination):
    # Initialize the WebDriver instance
    service = init_service()
    driver = webdriver.Edge(service=service)

    # Construct the URL for the search
    url = construct_url(checkin_date, checkout_date, destination)

    # Navigate to the URL
    driver.get(url)

    
    # Close the popup window
    close_popup(driver)

    # Scrape the pages
    scrape_pages(driver)

    # Close the WebDriver instance
    driver.quit()

if __name__ == "__main__":
    checkin_date = '2024-01-30'
    checkout_date = '2024-2-30'
    destination = 'Paris'
    main(checkin_date, checkout_date, destination)
