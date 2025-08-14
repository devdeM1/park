from conftest import driver
from pages.residents_page import ResidentsPage

def test_basic_auth(driver):
    auth_page = ResidentsPage(driver)
    auth_page.open()
    assert auth_page.page_is_successfully_open(auth_page.TITLE), 'The page is not opened correctly'