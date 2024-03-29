from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_hotels(driver):
    """
    Get a list of hotels from the given driver.

    Args:
        driver: The WebDriver instance.

    Returns:
        A list of WebElement objects representing the hotels.
    """
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, './/div[@data-testid="property-card"]')
        )
    )
    return driver.find_elements(
        By.XPATH, './/div[@data-testid="property-card"]'
    )
