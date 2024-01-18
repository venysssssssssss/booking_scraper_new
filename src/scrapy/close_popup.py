from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def close_popup(driver):
    """
    Close the popup window by clicking on the close button.

    Args:
        driver: The WebDriver instance.

    Raises:
        Exception: If an error occurs while closing the popup.

    """
    try:
        WebDriverWait(driver, 18).until(EC.element_to_be_clickable(( By.XPATH, '//button[@aria-label="Close"]'))).click()
    except Exception as e:
        print(f"An error occurred while closing the popup: {str(e)}")
