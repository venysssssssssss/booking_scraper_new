from selenium import webdriver
from init_service import init_service

def init_driver():
    service = init_service()
    return webdriver.Edge(service=service)
