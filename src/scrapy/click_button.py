from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def click_button(driver):
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="b2searchresultsPage"]/div[44]/div/div/div/div[1]/div[1]/div/button'))).click()
    except Exception as e:
        print(f"An error occurred while clicking the button: {str(e)}")
