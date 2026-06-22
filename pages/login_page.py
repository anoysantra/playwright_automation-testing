from playwright.sync_api import sync_playwright

class LoginPage:
    def __init__(self , page):
        self.page = page
        self.email_locator = page.locator("#userEmail")
        self.password_locator = page.locator("#userPassword")
        self.login_btn_locator = page.locator("#login")  

    def login(self,username ,password):
       self.email_locator.fill(username)
       self.password_locator.fill(password)
       self.login_btn_locator.click()


        
