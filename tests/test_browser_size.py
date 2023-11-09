import pytest
from selene.support.shared import browser

@pytest.fixture()
def chrome():
    pass

@pytest.fixture()
def open_browser(chrome):
    pass

@pytest.fixture
def browser_size():
    browser.size.window_width = 1024
    browser.size.window_height = 768

def test_browser_size(open_browser, browser_size):
    pass
