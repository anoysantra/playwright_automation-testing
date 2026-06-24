from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)

class InvoicePage:
    def __init__(self, page: Page):
        self.page = page
        self.invoice_locator = page.locator('td.em-spacer-1')
        self.all_invoice_locator = self.invoice_locator.locator('label.ng-star-inserted')
        self.thank_you_text_locator = self.page.get_by_text('Thankyou for the order.')
        #view the invoices


    def get_order_ids(self):
        self.thank_you_text_locator.wait_for(state="visible", timeout=5000)
        thank_you_msg = self.thank_you_text_locator.text_content()
        logger.info(f"Thank you message: {thank_you_msg.strip()}")
        
        order_id_lists = []
        orders_ids = self.all_invoice_locator.all()

        for order in orders_ids:
            raw_text = order.text_content()
            clean_text = raw_text.replace("|", "").strip()
            order_id_lists.append(clean_text)
        
        logger.info(f"Order IDs extracted: {order_id_lists}")
        return thank_you_msg, order_id_lists

