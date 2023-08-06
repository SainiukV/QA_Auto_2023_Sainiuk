from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage():
    PATH = r"c:/Users/38067/QA_Auto_2023_Sainiuk/"
    DRIVER_NAME = "chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service = Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()