import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def close_popup(driver):
    """
    Close the popup window by clicking on the screen.

    Args:
        driver: The WebDriver instance.

    Raises:
        Exception: If an error occurs while closing the popup.

    """
    try:
        wait = WebDriverWait(driver, 15)
        element_present = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="b2searchresultsPage"]/div[49]/div/div/div',
                )
            )
        )
        click_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="b2searchresultsPage"]/div[48]/div/div/div/div[1]/div[1]/div/button',
                )
            )
        )
        if element_present and click_button:
            time.sleep(2)  # Aguarda por 2 segundos antes de clicar
            click_button.click()
            wait.until_not(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="b2searchresultsPage"]/div[49]/div/div/div',
                    )
                )
            )
    except Exception as e:
        print(f'An error occurred while closing the popup: {str(e)}')
