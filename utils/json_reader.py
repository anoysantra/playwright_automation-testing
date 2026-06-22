import json

global products

def json_helper_products():
    with open('test_data/order_shopping_data.json') as f:
        product_data = json.load(f)
        products = product_data['products']
        return products

def json_helper_payments():
    with open('test_data/card_details.json') as f:
        payment_info = json.load(f)
        card = payment_info['test_card']
        return card





