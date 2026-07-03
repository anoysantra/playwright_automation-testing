import json
from pathlib import Path


def _load_json(file_name: str) -> dict:
    file_path = Path(__file__).resolve().parent.parent / "test_data" / file_name
    with file_path.open(encoding="utf-8") as file_handle:
        return json.load(file_handle)


def json_helper_products() -> list[dict]:
    product_data = _load_json("order_shopping_data.json")
    return product_data["products"]


def json_helper_payments() -> dict:
    payment_info = _load_json("card_details.json")
    return payment_info["test_card"]


def json_helper_cart() -> list[dict]:
    cart_info = _load_json("cart_payload.json")
    return cart_info["cart_payloads"]


def json_helper_create_order() -> dict:
    order_info = _load_json("order_create_data.json")
    return order_info

#pytest --collect-only




