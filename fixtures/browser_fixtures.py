"""
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
"""

import pytest
from playwright.sync_api import Browser

# 1. We use Playwright's built-in 'browser' fixture instead of sync_playwright()
@pytest.fixture(scope="session")
def page_initialization(browser: Browser):
    # Launch context and page natively inside the existing event loop
    context = browser.new_context()
    page = context.new_page()
    
    yield page
    
    # Teardown / Cleanup
    context.close()
