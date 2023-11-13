from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="F://Official/LaxmanAutomantion/Pycharm Projects/drivers/chromedriver.exe")
    return driver
