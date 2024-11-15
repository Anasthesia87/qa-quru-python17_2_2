import pytest
from selene import browser


@pytest.fixture(autouse=True)
def settings_browser():
    browser.config.window_height = 768
    browser.config.window_width = 1024

    yield

    browser.quit()
