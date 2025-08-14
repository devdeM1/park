from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver


class WebDriverUtils:
    DEFAULT_TIMEOUT = 5

    @staticmethod
    def get_present_element(driver, locator, timeout=DEFAULT_TIMEOUT):
        return wait(driver, timeout).until(EC.presence_of_element_located(locator))
