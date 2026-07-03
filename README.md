# Playwright Ecommerce Test Automation Suite

A focused Playwright + Pytest automation project for an ecommerce demo application.

## What is covered
- Login and logout flow
- Empty cart and empty order validation
- Add products to cart and verify count
- Checkout, payment, and coupon application
- Invoice capture and order history validation

## Why this is useful
- Uses Page Object Model for maintainable page interactions
- External JSON test data stored in `test_data/`
- Pytest fixtures for browser setup and auth reuse
- Combines UI and API automation examples
- Ready for portfolio and interview discussion

## Structure
- `pages/` — page objects
- `tests/` — UI and API tests
- `fixtures/` — setup and authentication fixtures
- `utils/` — test data helpers
- `test_data/` — external JSON inputs
- `logs/` — execution logs
- `reports/` — HTML results

## Quick setup
```bash
git clone https://github.com/anoysantra/playwright_automation-testing.git
cd playwright_ecommerce_project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Run tests
```bash
pytest tests/test_ui_workflow.py -v
pytest tests/test_ui_workflow.py::test_login_operation -v
pytest tests/test_ui_workflow.py -v -s
```

## API test commands
```bash
pytest tests/test_api_workflow.py -v
pytest tests/test_api_login_ui_workflow.py -v
```

## Test flow
1. Login to the app
2. Validate empty cart and empty orders states
3. Add items to cart and verify count
4. Checkout, apply coupon, and place order
5. Capture invoice order IDs and verify order history
6. Validate order details and sign out

## Key pages
- `LoginPage`: login and sign-out
- `CartPage`: product selection, cart count, checkout
- `OrderPaymentsPage`: payment form, coupon, place order
- `OrdersPage`: order list and details
- `InvoicePage`: extract order IDs after payment

## Project value
A clean ecommerce test automation suite demonstrating end-to-end workflow coverage, modular design, and data-driven validation.
