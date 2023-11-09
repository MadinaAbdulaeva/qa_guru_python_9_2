from selene.support.shared import browser
from selene import be, have

def test_browser_invalid_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('**&kfjejfwlkfn').press_enter()
    browser.element('[style="padding-top:.33em"]').should(have.text('По запросу **&kfjejfwlkfn ничего не найдено.'))