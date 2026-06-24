from playwright.sync_api import sync_playwright, Page
import re
import logging

logger = logging.getLogger(__name__)

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.card_container = page.locator('div.card')
        self.cart_navbar_btn = page.locator('button[routerlink ="/dashboard/cart"]')
        self.empty_cart_text = page.get_by_text("No Products in Your Cart !")
        self.cart_items_locator = page.locator('ul.cartWrap')
        self.total_locator = page.get_by_text("Total", exact=True)
        self.subtotal_locator = page.get_by_text('Subtotal')
        self.checkout_btn_locator = page.get_by_role('button', name='Checkout')
        self.subtotal_amount_locator = page.get_by_role('//div[contains(@class ,"subtotal")]//ul[1]//li[1]/span[@class="value"]')
        self.total_amount_locator = page.get_by_role('//div[contains(@class ,"subtotal")]//ul[2]//li[2]/span[@class="value"]')

    def cart_history_empty(self):
        self.cart_navbar_btn.click()
        self.page.wait_for_url('**/cart')

        if not self.empty_cart_text.is_visible(timeout=5000):
            logger.warning("Empty cart text not visible. Cart may contain items or page structure has changed.")
            return ""

        msg_text = self.empty_cart_text.text_content()
        logger.info(f"Msg displayed when cart is empty: {msg_text.strip()}")
        return msg_text

    def select_product(self, product_name):
        specific_product_card = self.card_container.filter(has_text=product_name)
        add_to_cart_btn = specific_product_card.get_by_role('button', name='Add To Cart')
        add_to_cart_btn.click()

    def count_cart_items(self):
        self.cart_navbar_btn.click()
        self.page.wait_for_url('**/cart')
        logger.info(f"Current URL: {self.page.url}")
        self.total_locator.wait_for(state="visible", timeout=10000)
        number_of_items = self.cart_items_locator.count()
        return number_of_items

    def checkout(self):
        subtotal_amount = self.subtotal_amount_locator.text_content()
        total_amount = self.total_amount_locator.text_content()
        prices = {'subtotal': subtotal_amount, 'total': total_amount}
        return prices

    def checkout_press(self):
        self.checkout_btn_locator.click()
