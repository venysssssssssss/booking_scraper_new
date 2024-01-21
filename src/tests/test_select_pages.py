import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from unittest.mock import patch
from src.scrapy.extract_hotel_info import extract_hotel_info
from src.scrapy.get_hotels import get_hotels
from src.scrapy.save_hotel_info import save_hotel_info
from src.scrapy.select_pages import scrape_pages

class TestScrapePages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.quit()

    @patch('builtins.input', side_effect=['2', '2'])
    def test_scrape_pages_save_all_in_one_file(self, mock_input):
        # Set up
        driver = self.driver
        driver.get('https://example.com')
        
        # Execute
        scrape_pages(driver)
        
        # Assert
        # Add your assertions here
    
    @patch('builtins.input', side_effect=['2', '1'])
    def test_scrape_pages_save_each_page_in_file(self, mock_input):
        # Set up
        driver = self.driver
        driver.get('https://example.com')
        
        # Execute
        scrape_pages(driver)
        
        # Assert
        # Add your assertions here
    
    @patch('builtins.input', side_effect=['0', '2'])
    def test_scrape_pages_invalid_num_pages(self, mock_input):
        # Set up
        driver = self.driver
        driver.get('https://example.com')
        
        # Execute
        scrape_pages(driver)
        
        # Assert
        # Add your assertions here
    
    @patch('builtins.input', side_effect=['2', '3'])
    def test_scrape_pages_invalid_save_option(self, mock_input):
        # Set up
        driver = self.driver
        driver.get('https://example.com')
        
        # Execute
        scrape_pages(driver)
        
        # Assert
        # Add your assertions here

if __name__ == '__main__':
    unittest.main()
