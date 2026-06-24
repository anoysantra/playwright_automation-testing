import logging

from playwright.sync_api import sync_playwright , Page

logger = logging.getLogger(__name__)

class LoginPage:
    def __init__(self , page : Page):
        self.page = page
        self.email_locator = page.locator("#userEmail")
        self.password_locator = page.locator("#userPassword")
        self.login_btn_locator = page.locator("#login") 
        self.sign_out_btn_locator = page.get_by_role("button", name="Sign Out")

    def login(self,username ,password):
       self.email_locator.fill(username)
       self.password_locator.fill(password)
       logger.info(f"Attempting to log in with username: {username}")
       self.login_btn_locator.click()
       logger.info("Login button clicked. Waiting for navigation to dashboard...")
       self.page.wait_for_url("**/dashboard/dash")
       logger.info(f"Successfully logged in. Current URL: {self.page.url}")     


    def sign_out(self):
        self.sign_out_btn_locator.click()
        self.page.wait_for_url("**/login")
        logger.info(f"Successfully signed out. Current URL: {self.page.url}")
        return self.page.url


        
