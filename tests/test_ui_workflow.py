from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.order_payments_page import PaymentsPage
import re
from playwright.sync_api import Page, expect
from utils.json_reader import json_helper_products , json_helper_payments


def test_login_operation(page_initialization):
    page = page_initialization
    page.goto('https://rahulshettyacademy.com/client/#/auth/login')
    login_instance = LoginPage(page)
    creds = {'username' : 'testuserleo13@gmail.com' , 'password' : 'Sample@1234'}  # will later stage read from json files
    login_instance.login(creds.get('username') , creds.get('password'))
    #print('The URL : ', page.url)

    page.wait_for_url('**/dashboard/dash')
    heading_h3_p = page.get_by_text('Automation Practice').inner_text()
    #print('Header Text : ', heading_h3_p)
    #expect(page).to_have_url(re.compile(r"/dashboard/dash"))    #test-try 1
    assert '/dashboard/dash' in page.url , 'ERROR : Cannot Login'  #test-try 2
    assert heading_h3_p == 'Automation Practice' , 'ERROR : not in login page no heading found'  #test-try 3
   


def test_cart_empty(page_initialization):
    page = page_initialization
    cart = CartPage(page)
    msg = cart.cart_history_empty()
    print(msg)
    assert 'No Products in Your Cart !' in msg , 'ERROR : not found'

def test_orders_page_empty(page_initialization):
    pass


def test_cart_with_products(page_initialization):
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
    print('After checkout btn press : ',checkout_url)
    print('Final Product Count :', count_items)
    assert count_items == 3, f'{count_items} wrong count'
    assert '/order' in checkout_url, 'ERROR : Checkout URL not matching'

def test_payments(page_initialization):
    page = page_initialization
    coupon = 'rahulshettyacademy'
    payments = PaymentsPage(page)
    card = json_helper_payments()
    msg , email , url = payments.add_payment_details(card, coupon)
    print("payment : ", url)
    # expect(coupon_locator).to_contain_text("* Coupon Applied", timeout=5000)
    assert '* Coupon Applied' in msg
    assert 'testuserleo13@gmail.com' in email
    assert '/thanks' in url 























        
    
    










