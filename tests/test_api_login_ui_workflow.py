
from playwright.sync_api import Page , BrowserContext

def test_dashboard_check(auth_browser_context: BrowserContext , page : Page):
    page = auth_browser_context.new_page()
    page.goto('https://rahulshettyacademy.com/client/#/dashboard/dash')
    print('Dashboard URL : ', page.url)
    text = page.get_by_text('Showing 3 results').text_content()
    assert '3 results' in text

def test_orders_page(auth_browser_context: BrowserContext , page : Page):
    page = auth_browser_context.new_page()
    page.goto('https://rahulshettyacademy.com/client/#/dashboard/dash')
    orders_navbar_btn = page.locator('button[routerlink ="/dashboard/myorders"]')
    orders_navbar_btn.click()
    text = page.get_by_text('Your Orders').text_content()
    url = page.url
    assert 'myorders' in url
    assert 'Your Orders' in text





