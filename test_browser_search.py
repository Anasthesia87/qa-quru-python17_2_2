from selene import browser, be, have


def test_search_correct_request():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_search_incorrect_request():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('y566/76554j===').press_enter()
    browser.element('#rcnt').should(have.text('По запросу y566/76554j=== ничего не найдено. '))
