import json
from playwright.sync_api import APIRequestContext, Page
import pytest
from utils.api_logger import get_api_logger
from utils.json_reader import *

LOGGER = get_api_logger(__name__)
orderIDs = []

# create_order-api
# fetch order api
# check for excel data


def log_response(action_name: str, response) -> dict:
    """Parse the API response payload and log the status details for debugging."""
    try:
        response_payload = response.json()
    except Exception:
        response_payload = {"text": response.text()}

    LOGGER.info("%s status=%s payload=%s", action_name, response.status, response_payload)
    return response_payload


def test_dashboard_page_is_reachable(auth_using_api: APIRequestContext):
    """Verify that the dashboard endpoint responds successfully for an authenticated user."""
    request_url = "https://rahulshettyacademy.com/client/"
    api_response = auth_using_api.get(request_url)
    log_response("Dashboard response", api_response)
    assert api_response.ok
    assert api_response.status == 200




products = json_helper_cart()
#print(f"Products loaded for parameterized test: {products} and type: {type(products)}")

@pytest.mark.parametrize("cart_payload", products, ids=[p["product"]["productName"] for p in products])
def test_add_to_cart_endpoint(auth_using_api: APIRequestContext, user , cart_payload):
    """Validate that adding a product to the cart via the API works as expected."""
    customer_user_id = user
    add_to_cart_url = "https://rahulshettyacademy.com/api/ecom/user/add-to-cart"
    #cart_payload = json_helper_cart()
    #cart_payload["_id"] = customer_user_id
    #print(f"Payload Cart : {cart_payload} and type: {type(cart_payload)}")

    cart_payload["_id"] = customer_user_id
    api_response = auth_using_api.post(
        add_to_cart_url,
        data=json.dumps(cart_payload),
        headers={"Content-Type": "application/json"},
    )
    response_payload = log_response("Add to cart response", api_response)
    assert api_response.status == 200
    assert response_payload.get("message", "").strip() == "Product Added To Cart"

def test_cart_endpoint_returns_success_status(auth_using_api: APIRequestContext, user):
    """Check that the cart API returns a successful response for the current user."""
    customer_user_id = user
    request_url = f"https://rahulshettyacademy.com/api/ecom/user/get-cart-products/{customer_user_id}"
    api_response = auth_using_api.get(request_url)
    print(f"Cart endpoint response: {api_response.json()}")
    log_response("Empty cart response", api_response)
    assert api_response.status == 200
    assert api_response.json().get("message", "").strip() == "Cart Data Found"
    assert api_response.json().get('count') == 3, "Expected 3 products in the cart for the user"   


def test_cart_count_endpoint_returns_expected_message(auth_using_api: APIRequestContext, user):
    """Validate the cart-count endpoint payload and success/error messaging."""
    customer_user_id = user
    request_url = f"https://rahulshettyacademy.com/api/ecom/user/get-cart-count/{customer_user_id}"
    api_response = auth_using_api.get(request_url)
    response_payload = log_response("Check cart count response", api_response)
    print("Cart count response:", response_payload)
    if api_response.status == 200:
        assert response_payload["message"].strip() == "Cart Data Found"
        assert response_payload["count"] == 3, "Expected 3 products in the cart for the user"
    else:
        assert api_response.status == 400
        assert response_payload["message"].strip() == "No Product in Cart"
        LOGGER.error("Error checking cart count: %s", response_payload)


def test_mocked_empty_cart_response_is_handled(page: Page, user):
    """Validate that a mocked empty-cart response is handled correctly in the browser context."""
    customer_user_id = user

    def handle_cart_route(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps({"message": "No Products Added to Cart. This is a mock response"}),
        )

    login_credentials = {"userEmail": "testuserleo13@gmail.com", "userPassword": "Sample@1234"}
    login_api_url = "https://rahulshettyacademy.com/api/ecom/auth/login"
    request_headers = {"Content-Type": "application/json"}
    login_response = page.request.post(login_api_url, data=login_credentials, headers=request_headers)
    login_payload = login_response.json()

    access_token = login_payload.get("token")

    page.route("**/get-cart-products/*", handle_cart_route)

    cart_products_url = f"https://rahulshettyacademy.com/api/ecom/user/get-cart-products/{customer_user_id}"
    api_response = page.evaluate(
        f"""() => fetch("{cart_products_url}", {{
            headers: {{ Authorization: "Bearer {access_token}" }}
        }}).then(res => res.json())"""
    )

    LOGGER.info("Mocked cart response: %s", api_response)


def test_get_all_products_endpoint_returns_expected_payload(auth_using_api: APIRequestContext):
    """Confirm the products listing API returns the expected payload and count."""
    products_api_url = "https://rahulshettyacademy.com/api/ecom/product/get-all-products"
    product_filter_payload = {
        "productName": "",
        "minPrice": None,
        "maxPrice": None,
        "productCategory": [],
        "productSubCategory": [],
        "productFor": [],
    }

    products_api_response = auth_using_api.post(
        products_api_url,
        data=json.dumps(product_filter_payload),
        headers={"Content-Type": "application/json"},
    )
    response_payload = log_response("Get all products response", products_api_response)
    product_count = response_payload.get("count")
    response_message = response_payload.get("message")

    assert product_count == 3, "Wrong Count of Items"
    assert (response_message or "").strip() == "All Products fetched Successfully"


def test_customer_order_history_endpoint_returns_success(auth_using_api: APIRequestContext, user):
    """Verify the customer order history API returns a successful response."""
    customer_user_id = user
    request_url = f"https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/{customer_user_id}"
    api_response = auth_using_api.get(request_url)
    response_payload = log_response("Get all order details response", api_response)
    assert api_response.status == 200
    assert response_payload["message"].strip() == "Orders fetched for customer Successfully"

# Example of a specific-order lookup test kept as a commented block for reference.
# def test_specific_order_details_endpoint_returns_expected_payload(auth_using_api: APIRequestContext):
#     """Retrieve a specific order and assert the expected response message."""
#     order_id = "6a3d51d2378febeacdcdfc"
#     request_url = f"https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id={order_id}"
#     api_response = auth_using_api.get(request_url)
#     response_payload = log_response("Get specific order response", api_response)
#     if api_response.status == 200:
#         assert response_payload["message"].strip() == "Orders fetched for customer Successfully"
#     else:
#         assert api_response.status_text.strip() == "Internal Server Error"
#         LOGGER.error("Error fetching specific order details: %s", response_payload)


# https://rahulshettyacademy.com/api/ecom/user/get-cart-count/6a38bf36378febeacdc1bb06 ---> get cart count check this api
# userID : 6a38bf36378febeacdc1bb06
# output msg if no item in cart : {"message":"No Product in Cart"}


def test_delete_order_endpoint_handles_success_and_failure(auth_using_api: APIRequestContext):
    """Check the delete-order endpoint behavior for both successful and failed cases."""
    order_id = "6a3bce1b378febeacdc9ebad"
    request_url = f"https://rahulshettyacademy.com/api/ecom/order/delete-order/{order_id}"
    api_response = auth_using_api.delete(request_url)
    response_payload = log_response("Delete order response", api_response)
    if api_response.status == 200:
        assert response_payload["message"].strip() == "Orders Deleted Successfully"
    else:
        assert api_response.status == 400
        assert response_payload["message"].strip() == "Order not found"
        LOGGER.error("Error deleting order: %s", response_payload)


def test_place_order_response(auth_using_api: APIRequestContext, user):
    """Validate the place-order endpoint returns a successful response for a valid order."""
    global orderIDs
    check_url = "https://rahulshettyacademy.com/api/ecom/order/create-order"

    payload = json_helper_create_order()
    print("DEBUG : ", payload)
    api_response = auth_using_api.post(check_url , data = payload)
    response_payload = log_response("Delete order response", api_response)
    print("The response is : ", response_payload)
    #collecting all the produced orderIds in a list
    for orderid in response_payload['orders']:
        orderIDs.append(orderid)

    assert api_response.status == 201
    assert response_payload['message'] == "Order Placed Successfully"


def test_specific_order(auth_using_api: APIRequestContext):
    """Retrieve a specific order and assert the expected response message."""
    orderIDs.append('6a476863cd73adf7e58ee31f') #a order where ID is deleted
    for orderid in orderIDs:
        print(f"----------------Testing for Order ID : {orderid}----------------")
        request_url = f"https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id={orderid}"
        api_response = auth_using_api.get(request_url)
        response_payload = log_response("Get specific order response", api_response)
        if api_response.status == 200:
            assert response_payload["message"].strip() == "Orders fetched for customer Successfully"
        else:
            assert api_response.status == 400
            assert response_payload["message"].strip() == "Order not found"
            



    


    




































