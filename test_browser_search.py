
from selene.support.shared import browser
from selene import be, have

def test_browser_valid_search(browser_size): #успешный поиск с применением фикстуры browser_size
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_browser_invalid_search(browser_size): #поиск без результата с применением фикстуры browser_size
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('**&kfjejfwlkfn').press_enter()
    browser.element('[style="padding-top:.33em"]').should(have.text('По запросу **&kfjejfwlkfn ничего не найдено.'))
