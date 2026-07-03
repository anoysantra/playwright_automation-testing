
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def page_initialization():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        #closing
        context.close()
        browser.close()
