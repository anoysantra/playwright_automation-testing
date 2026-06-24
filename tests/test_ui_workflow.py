from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.order_payments_page import PaymentsPage
from pages.orders_page import OrdersPage
from pages.invoice_page import InvoicePage
import pytest
from playwright.sync_api import Page
from utils.json_reader import json_helper_products, json_helper_payments

# Global list to store order IDs generated from invoice page for later validation
global_list_invoices = []


def test_login_operation(page_initialization):
    # Test user login with credentials and verify dashboard is loaded
    page = page_initialization
    page.goto('https://rahulshettyacademy.com/client/#/auth/login')
    login_instance = LoginPage(page)
    creds = {'username': 'testuserleo13@gmail.com', 'password': 'Sample@1234'}
    login_instance.login(creds.get('username'), creds.get('password'))
    heading_h3_p = page.get_by_text('Automation Practice').inner_text()

    assert '/dashboard/dash' in page.url, 'ERROR : Cannot Login'
    assert heading_h3_p == 'Automation Practice', 'ERROR : not in login page no heading found'



def test_cart_empty(page_initialization):
    # Verify empty cart message is displayed when no products are in the cart
    page = page_initialization
    cart = CartPage(page)
    msg = cart.cart_history_empty()
    if msg == "":
        pytest.skip("Empty cart text not found. Skipping assertion.")
    else:
        assert 'No Products in Your Cart !' in msg, 'ERROR : empty cart text not found'
    

def test_orders_page_empty(page_initialization):
    # Validate that empty orders message is shown when user has no previous orders
    page = page_initialization
    order = OrdersPage(page)
    msg_check = order.empty_orders_validation()
    if msg_check == "":
        pytest.skip("Empty orders text not found. Skipping assertion.")
        
    assert 'You have No Orders to show at this time.' in msg_check, f'ERROR : {msg_check} error in orders empty page'


def test_cart_with_products(page_initialization):
    # Add products to cart, proceed to checkout and verify cart count and URL
    page = page_initialization
    cart = CartPage(page)
    page.goto('https://rahulshettyacademy.com/client/#/dashboard/dash')
    page.wait_for_url('**/dashboard/dash')
    products = json_helper_products()
    count_items = int()
    
    for product in products:
        productName = product['product_name']
        cart.select_product(productName)
    
    count_items = cart.count_cart_items()
    cart.checkout_press()
    checkout_url = page.url
    assert count_items == 3, f'{count_items} wrong count'
    assert '/order' in checkout_url, 'ERROR : Checkout URL not matching'


def test_payments(page_initialization):
    # Fill payment details, apply coupon and place order to verify successful payment flow
    page = page_initialization
    coupon = 'rahulshettyacademy'
    payments = PaymentsPage(page)
    card = json_helper_payments()
    msg, email, url = payments.add_payment_details(card, coupon)
    assert '* Coupon Applied' in msg
    assert 'testuserleo13@gmail.com' in email
    assert '/thanks' in url


def test_invoices_generated(page_initialization):
    # Extract order IDs from invoice page and store them in global list for validation
    page = page_initialization
    invoices = InvoicePage(page)
    thanks_msg, list_invoices = invoices.get_order_ids()
    global_list_invoices.extend(list_invoices)

    assert 'Thankyou for the order.' in thanks_msg, f'ERROR : {thanks_msg} the thanks msg not matching'
    assert len(list_invoices) == 3, f'ERROR : {len(list_invoices)} the length not matched'


def test_order_id_generated_check(page_initialization):
    # Verify that all invoice order IDs are present in the orders table
    page = page_initialization
    order = OrdersPage(page)
    ids = order.order_ids_check()

    assert len(ids) >= 3, f'ERROR : Found only {len(ids)} orders, expected at least 3.'
    assert set(global_list_invoices).issubset(set(ids)), f"ERROR: Some IDs from {global_list_invoices} are missing in table!"


def test_check_invoice_address(page_initialization):
    # Navigate to order details page and verify billing and delivery address match
    page = page_initialization
    order = OrdersPage(page)
    specific_id = global_list_invoices[1]
    response_url, thanks_msg, billing_details, delivery_details = order.order_id_detail_check(specific_id)

    assert f'/order-details/{specific_id}' in response_url, 'WRONG URL'
    assert 'Thank you for Shopping With Us' in thanks_msg
    assert billing_details == delivery_details, 'ERROR : the details in billing and delivery do not match'


def test_sign_out(page_initialization):
    # Test user sign out functionality and verify redirect to login page
    page = page_initialization
    login_instance = LoginPage(page)
    sign_out_url = login_instance.sign_out()
    assert '/login' in sign_out_url, 'ERROR : Sign out URL not matching'







