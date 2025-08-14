from conftest import driver
from pages.residents_page import ResidentsPage

def test_resident_page(driver):
    resident_page = ResidentsPage(driver)
    resident_page.open()
    assert resident_page.page_is_successfully_open(resident_page.TITLE), 'The page is not opened correctly'