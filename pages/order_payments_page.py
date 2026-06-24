from playwright.sync_api import sync_playwright, expect , Page
import logging

logger = logging.getLogger(__name__)

class PaymentsPage:
    def __init__(self, page: Page):
        self.page = page
        self.day_select_locator = page.locator('select').nth(0)
        self.month_select_locator = page.locator('select').nth(1)
        self.card_number_locator = page.locator("div.field:has-text('Credit Card Number') input")
        self.cvv_number_locator = page.locator("div.field:has-text('CVV Code') input")
        self.name_on_card_locator = page.locator("div.field:has-text('Name on Card') input")
        self.country_select_locator = page.locator('input[placeholder="Select Country"]')
        self.email_locator = page.locator('div.user__name.mt-5')
        self.coupon_code_locator = page.locator('input[name = "coupon"]')
        self.apply_coupon_btn = page.get_by_role("button", name="Apply Coupon")
        self.dropdown_results = page.locator("section.ta-results button.ta-item")
        # Targets the success message layout container that appears afterward
        self.coupon_success_msg = page.get_by_text("* Coupon Applied")
        self.place_order_btn_locator = page.locator('a.btnn.action__submit:has-text("Place Order")')


    def add_payment_details(self, card_data : dict, coupon_code : str):
        # 1. Fill Credit Card Information Fields
        self.card_number_locator.wait_for(state="visible", timeout=5000)
        self.card_number_locator.clear()
        self.card_number_locator.fill(card_data.get("card_number"))
        self.cvv_number_locator.fill(card_data.get("cvv"))
        self.name_on_card_locator.fill(card_data.get("card_name"))
        
        # 2. Interact with Expiry Date Dropdowns
        self.day_select_locator.select_option(value=card_data.get("expiry_day"))
        self.month_select_locator.select_option(value=card_data.get("expiry_month"))
        
        # 3. Handle Dynamic Angular Country Suggestion Field
        country = card_data.get("country").strip()
        #self.country_select_locator.fill(country)
        self.country_select_locator.press_sequentially(country, delay=100)
        self.dropdown_results.first.wait_for()
       
        country_option = self.page.locator("button.ta-item").get_by_text(country, exact=True)
        logger.info(f"Country selected: {country}")
        country_option.first.click()


        # 4. Handle Coupon Submission
        self.coupon_code_locator.fill(coupon_code)
        self.apply_coupon_btn.click()

        email = self.email_locator.text_content()
        coupon_msg = self.coupon_success_msg.text_content()
        self.place_order_btn_locator.click()
        
        self.page.wait_for_url("**/dashboard/thanks*")
        after_payment_url = self.page.url
        logger.info(f"After payment URL: {after_payment_url}")
        
        return coupon_msg, email, after_payment_url