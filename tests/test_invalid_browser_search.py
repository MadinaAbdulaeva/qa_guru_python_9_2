from selene.support.shared import browser
from selene import be, have

def test_google_should_not_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('**&kfjejfwlkfn').press_enter()
    browser.element('#botstuff').should(have.text('По запросу **&kfjejfwlkfn ничего не найдено.'))