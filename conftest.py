import pytest
from selene import browser

@pytest.fixture #фикстура на размер браузерного окна
def browser_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    yield
    browser.quit()