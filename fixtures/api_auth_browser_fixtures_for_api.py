import pytest
import json
from typing import Generator
from playwright.sync_api import Playwright, BrowserContext


@pytest.fixture(scope="session")
def auth_browser_context(playwright: Playwright) -> Generator[BrowserContext, None, None]:
    new_request_context: BrowserContext = playwright.request.new_context()
    user_cred = {'userEmail': "testuserleo13@gmail.com", 'userPassword': "Sample@1234"}
    auth_api_url = "https://rahulshettyacademy.com/api/ecom/auth/login"

    login_response = new_request_context.post(auth_api_url, data=user_cred)
    data = login_response.json()
    token = data.get('token')

    if not token:
        raise RuntimeError("❌ No token found in login response")

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client")
    page.evaluate(f"window.localStorage.setItem('token','{token}')")

    yield context

    context.close()
    browser.close()
