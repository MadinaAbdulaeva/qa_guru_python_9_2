
from selene.support.shared import browser
from selene import be, have
@pytest.fixture(scope='session', autouse=True) #фикстура на применение ко всем тестам

def test_browser_valid_search(): #успешный поиск
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_browser_invalid_search(): #поиск без результата
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('**&kfjejfwlkfn').press_enter()
    browser.element('[style="padding-top:.33em"]').should(have.text('По запросу **&kfjejfwlkfn ничего не найдено.'))
