from selenium import webdriver
from init_service import init_service

def init_driver():
    """
    Initializes and returns a WebDriver instance for the Edge browser.

    Returns:
        WebDriver: An instance of the Edge WebDriver.
    """
    service = init_service()
    return webdriver.Edge(service=service)
