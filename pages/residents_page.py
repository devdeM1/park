from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ResidentsPage(BasePage):
    TITLE = (By.XPATH, "//a[text() = 'Расширенный поиск']")
    URL = "https://www.park.by/residents/"

    def open(self):
        self.driver.get(self.URL)