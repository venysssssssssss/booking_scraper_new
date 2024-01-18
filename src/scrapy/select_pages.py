from selenium.webdriver.common.by import By
from src.scrapy.extract_hotel_info import extract_hotel_info
from src.scrapy.get_hotels import get_hotels
from src.scrapy.save_hotel_info import save_hotel_info

def scrape_pages(driver):
    all_hotels_list = []
    
    # Get the total number of available pages
    total_pages = len(driver.find_elements(By.XPATH, '//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[4]/div[2]/nav/nav/div/div[2]/ol/li'))
    print(f"The available pages are {total_pages}")

    # Ask the user for the number of pages to scrape
    while True:
        try:
            num_pages = int(input("Enter the number of pages to scrape: "))
            if 1 <= num_pages <= total_pages:
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    # Ask the user whether to save each page in a file or all pages in a single file
    while True:
        try:
            save_per_page = int(input("Do you want to save each page in a file or all pages in a single file? Enter 1 for each page, 2 for all in one: "))
            if save_per_page in [1, 2]:
                save_per_page = save_per_page == 1
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    
    for i in range(num_pages):
        print(f"Scraping page {i+1}...")
        hotels = get_hotels(driver)  # Get the hotels on the current page here
        hotels_list = [extract_hotel_info(hotel) for hotel in hotels]
        all_hotels_list.extend(hotels_list)

        if save_per_page:
            save_hotel_info(hotels_list, f'hotels_page_{i+1}', save_per_page)

        next_page_button = driver.find_element(By.XPATH, '//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[4]/div[2]/nav/nav/div/div[2]/ol/li[1]/button')
        next_page_button.click()

    if not save_per_page:
        save_hotel_info(all_hotels_list, 'hotels_all_pages', save_per_page)
