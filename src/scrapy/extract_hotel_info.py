from selenium.webdriver.common.by import By

def extract_hotel_info(hotel):
    hotel_dict = {}
    title_element = hotel.find_element(By.XPATH, './/div[@data-testid="title"]')
    hotel_dict['hotel'] = title_element.get_attribute('innerText') if title_element else None
    price_element = hotel.find_element(By.XPATH, './/span[@data-testid="price-and-discounted-price"]')
    hotel_dict['price'] = price_element.get_attribute('innerText') if price_element else None
    score_element = hotel.find_element(By.XPATH, './/div[@data-testid="review-score"]/div[1]')
    hotel_dict['score'] = score_element.get_attribute('innerText') if score_element else None
    avg_review_element = hotel.find_element(By.XPATH, './/div[@data-testid="review-score"]/div[2]/div[1]')
    hotel_dict['avg review'] = avg_review_element.get_attribute('innerText') if avg_review_element else None
    reviews_count_element = hotel.find_element(By.XPATH, './/div[@data-testid="review-score"]/div[2]/div[2]')
    hotel_dict['reviews count'] = reviews_count_element.get_attribute('innerText').split()[0] if reviews_count_element else None
    return hotel_dict
