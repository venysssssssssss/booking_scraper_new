from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def get_hotels(driver):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="property-card"]')))
    return driver.find_elements(By.XPATH, '//div[@data-testid="property-card"]')
