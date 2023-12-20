from selene.support.shared import browser

import pytest

@pytest.fixture()

def browser_open_with_selene():
    browser.config.window_width = 1900
    browser.config.window_height = 950
    browser.open("https://github.com")

    yield "Google Chrome"
    browser.quit()
