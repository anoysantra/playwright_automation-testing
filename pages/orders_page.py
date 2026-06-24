from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)


class OrdersPage:
    def __init__(self, page: Page):
        self.page = page
        self.text_heading_locator = page.get_by_text('Your Orders')
        self.no_orders_text_locator = page.get_by_text("You have No Orders to show at this time.")
        self.orders_navbar_btn = page.locator('button[routerlink ="/dashboard/myorders"]')
        self.table = page.locator('table.table.table-bordered.table-hover.ng-star-inserted')
        self.orderId_rows_id = self.table.locator('tbody tr th')
        self.orderId_rows = self.table.locator('tbody tr')
        self.msg_thanks = page.get_by_text('Thank you for Shopping With Us')
        self.address_locator_billing = page.locator('div.address', has_text='Billing Address')
        self.address_locator_delivery = page.locator('div.address', has_text='Delivery Address')
        

    def empty_orders_validation(self):
        logger.info("Navigated to orders page. Checking for empty state message...")
        self.orders_navbar_btn.click()
        self.page.wait_for_url('**/myorders')
        logger.info(f"Page URL: {self.page.url}")

        # If the empty orders text is not visible, return an empty message rather than timing out
        if not self.no_orders_text_locator.is_visible(timeout=5000):
            logger.warning("Empty orders message not found. Orders may exist or page layout changed.")
            return ""

        msg = self.no_orders_text_locator.text_content()
        logger.info(f"Empty orders message: {msg.strip()}")
        return msg

    def order_ids_check(self):
        logger.info("Fetching order IDs from orders page...")
        self.orders_navbar_btn.click()
        self.page.wait_for_url('**/myorders')
        self.text_heading_locator.wait_for(state="visible")
        order_ids = self.orderId_rows_id.all()
        ids = []
        
        for orderId in order_ids:
            order_id = orderId.text_content()
            ids.append(order_id)
        
        logger.info(f"Order IDs found: {ids}")
        return ids

    def order_id_detail_check(self, orderID: str):
        logger.info(f"Checking details for order ID: {orderID}")
        matching_row = self.orderId_rows.filter(has_text=orderID)
        matching_row.get_by_role("button", name='View').click()
        thanks_msg = self.msg_thanks.text_content()
        self.page.wait_for_url('**/dashboard/order-details/*')
        
        billing_details = self.address_locator_billing.locator('p').all_text_contents()
        delivery_details = self.address_locator_delivery.locator('p').all_text_contents()
        
        logger.info(f"Order details page URL: {self.page.url}")
        return self.page.url, thanks_msg, billing_details, delivery_details
        
            




            








        
            








