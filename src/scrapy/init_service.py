from selenium.webdriver.edge.service import Service


def init_service():
    """
    Initializes and returns a Service object for the Microsoft Edge WebDriver.

    Returns:
        Service: A Service object for the Microsoft Edge WebDriver.
    """
    return Service(
        r'C:\\Users\\truks\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\msedgedriver.exe'
    )
