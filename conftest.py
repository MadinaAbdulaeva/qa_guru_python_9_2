import pytest
from selenium import browser

@pytest.fixture
def browser_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    browser.config.browser_name = 'Chrome'

    yield
    browser.quit()