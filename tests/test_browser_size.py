import pytest
from selenium import webdriver

@pytest.fixture()
def chrome():
    pass

@pytest.fixture()
def open_browser(chrome):
    pass

@pytest.fixture
def browser_size():
    webdriver.set_window_size(1024, 768)

def test_browser_size(open_browser, browser_size):
    pass
