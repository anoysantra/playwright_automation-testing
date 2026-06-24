# Playwright Ecommerce Test Automation Suite

A comprehensive **end-to-end test automation framework** for ecommerce applications using **Playwright** and **Pytest**. This project demonstrates industry best practices in test automation including the **Page Object Model (POM)** design pattern, organized test structure, data externalization, and integrated logging.

---

## 📋 Table of Contents

- [Quick Overview](#quick-overview)
- [Key Features](#key-features)
- [Project Architecture](#project-architecture)
- [Technologies & Dependencies](#technologies--dependencies)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Running Tests](#running-tests)
- [Test Workflow](#test-workflow)
- [Page Objects Explained](#page-objects-explained)
- [Test Data Management](#test-data-management)
- [Logging & Reports](#logging--reports)
- [Project Highlights for Recruiters](#project-highlights-for-recruiters)

---

## 🎯 Quick Overview

This project automates a complete **ecommerce user journey** on the Rahul Shetty Academy practice website:

```
LOGIN → VERIFY EMPTY STATES → ADD PRODUCTS TO CART → 
CHECKOUT → PAYMENT PROCESSING → ORDER VERIFICATION → SIGN OUT
```

**What it tests:**
- ✅ User authentication (login/logout)
- ✅ Cart management (add items, verify count)
- ✅ Checkout process (product selection, pricing)
- ✅ Payment processing (card details, coupon application)
- ✅ Order history & details verification
- ✅ Invoice generation and validation
- ✅ Cross-page data consistency

---

## ⚡ Key Features

| Feature | Benefit |
|---------|---------|
| **Page Object Model (POM)** | Centralized locators, easy maintenance, scalable |
| **Pytest Framework** | Industry standard, fixtures, plugins support |
| **Playwright** | Fast, cross-browser, modern automation API |
| **External Test Data** | JSON-based, easily updateable without code changes |
| **Integrated Logging** | File and console logs for debugging |
| **HTML Reports** | Beautiful test execution reports |
| **Graceful Error Handling** | Tests skip non-critical steps instead of failing |
| **Session & Function Fixtures** | Flexible browser initialization strategies |

---

## 🏗️ Project Architecture

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│           TEST LAYER (tests/)                           │
│   - test_ui_workflow.py: 9 sequential test cases       │
│   - Orchestrates page objects to execute workflows     │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│           PAGE OBJECT LAYER (pages/)                    │
│   ┌──────────────┬──────────────┬──────────────────┐  │
│   │ LoginPage    │ CartPage     │ OrderPaymentsPage│  │
│   │ OrdersPage   │ InvoicePage  │ DashboardPage    │  │
│   └──────────────┴──────────────┴──────────────────┘  │
│   - Encapsulate page interactions                      │
│   - Define locators & business logic                   │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│         SUPPORT LAYERS                                  │
│   ┌──────────────────┬──────────────────┐             │
│   │ Fixtures (fixtures/) │ Utils (utils/)   │             │
│   │ - Browser init    │ - JSON reader    │             │
│   │ - Page setup      │ - Helper methods │             │
│   └──────────────────┴──────────────────┘             │
│   ┌─────────────────────────────────────┐             │
│   │ Test Data (test_data/)              │             │
│   │ - Products, cards, credentials      │             │
│   └─────────────────────────────────────┘             │
└─────────────────────────────────────────────────────────┘
```

### Design Pattern: Page Object Model (POM)

Each page of the ecommerce application has a corresponding Python class:

```python
# Example: LoginPage encapsulates all login-related interactions
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = "#userEmail"          # Locator
        self.password_input = "#userPassword"    # Locator
    
    def login(self, username, password):
        # Interact with page elements
        # Wait for navigation
        # Return results
```

**Benefits:**
1. **Maintainability**: When a locator changes, update only one place
2. **Readability**: Tests read like business scenarios, not technical code
3. **Reusability**: Page methods are used across multiple test cases
4. **Scalability**: Add new pages without affecting existing tests

---

## 💻 Technologies & Dependencies

```
Playwright          - Modern web automation framework
Pytest              - Python testing framework
Python 3.8+         - Programming language
Logging             - Built-in Python logging module
JSON                - Test data storage format
```

### Key Playwright Concepts Used

| Concept | Purpose |
|---------|---------|
| `page.locator()` | Find elements using CSS/XPath |
| `page.wait_for_url()` | Assert URL changes (navigation) |
| `page.click()` | Click buttons/links |
| `page.fill()` | Enter text in input fields |
| `page.text_content()` | Extract text from elements |
| `page.select_option()` | Select from dropdowns |
| `is_visible()` | Check element visibility |

---

## 📁 Project Structure

```
playwright_ecommerce_project/
│
├── 📂 pages/                          # Page Object Classes
│   ├── login_page.py                  # Login & sign-out operations
│   ├── cart_page.py                   # Shopping cart interactions
│   ├── order_payments_page.py         # Payment & checkout
│   ├── orders_page.py                 # Order history & details
│   ├── invoice_page.py                # Order confirmation & invoice
│   └── dashboard_page.py              # Dashboard operations
│
├── 📂 tests/                          # Test Suites
│   ├── test_ui_workflow.py            # ⭐ Main test suite (9 test cases)
│   └── test_api_workflow.py           # Placeholder for API tests
│
├── 📂 fixtures/                       # Pytest Fixtures (Setup/Teardown)
│   ├── browser_fixtures.py            # Session-scoped browser setup
│   ├── auth_fixtures.py               # Function-scoped browser setup
│   └── api_fixtures.py                # Placeholder for API fixtures
│
├── 📂 utils/                          # Utility Functions
│   ├── json_reader.py                 # Read test data from JSON files
│   └── helper_functions.py            # Placeholder for helpers
│
├── 📂 test_data/                      # External Test Data (JSON)
│   ├── order_shopping_data.json       # Product names to test
│   ├── card_details.json              # Payment card info
│   └── creds_data.json                # Placeholder for credentials
│
├── 📂 config/                         # Configuration Files
│   └── project_data.py                # Placeholder for project config
│
├── 📂 logs/                           # Test Execution Logs
│   └── automation_run.log             # Generated during test runs
│
├── 📂 reports/                        # HTML Test Reports
│   └── report.html                    # Generated after test execution
│
├── conftest.py                        # Pytest configuration
├── pytest.ini                         # Pytest settings
└── README.md                          # This file

```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/anoysantra/playwright_automation-testing.git
cd playwright_ecommerce_project
```

### Step 2: Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**or manually install:**

```bash
pip install playwright pytest
playwright install chromium
```

### Step 4: Verify Installation

```bash
pytest --version
python -c "import playwright; print('Playwright installed successfully')"
```

---

## 🧪 Running Tests

### Run All Tests

```bash
pytest tests/test_ui_workflow.py -v
```

### Run with HTML Report

```bash
pytest tests/test_ui_workflow.py -v \
  --html=reports/report.html --self-contained-html
```

### Run Specific Test

```bash
pytest tests/test_ui_workflow.py::test_login_operation -v
```

### Run with Console Logging

```bash
pytest tests/test_ui_workflow.py -v -s
```

### Run in Debug Mode

```bash
pytest tests/test_ui_workflow.py -v -s --tb=long
```

### View Logs

```bash
cat logs/automation_run.log
```

---

## 🔄 Test Workflow

### Complete User Journey (9 Test Cases)

```
1️⃣  TEST_LOGIN_OPERATION
   └─ Navigate to login page → Enter credentials → Verify dashboard

2️⃣  TEST_CART_EMPTY
   └─ Verify cart shows "No Products" message on empty state

3️⃣  TEST_ORDERS_PAGE_EMPTY
   └─ Verify orders page shows "No Orders" message initially

4️⃣  TEST_CART_WITH_PRODUCTS
   └─ Add 3 products to cart → Verify cart count = 3

5️⃣  TEST_PAYMENTS
   └─ Fill payment details → Apply coupon → Place order

6️⃣  TEST_INVOICES_GENERATED
   └─ Extract order IDs from invoice page → Store globally

7️⃣  TEST_ORDER_ID_GENERATED_CHECK
   └─ Validate invoice order IDs appear in order history table

8️⃣  TEST_CHECK_INVOICE_ADDRESS
   └─ Fetch order details → Verify billing = delivery address

9️⃣  TEST_SIGN_OUT
   └─ Sign out → Verify redirect to login page
```

### Global State Management

Tests share state through a global variable:

```python
global_list_invoices = []  # Stores order IDs from invoice page
```

This allows **Test 6** to capture order IDs and **Test 7** to validate them in the orders table.

---

## 📄 Page Objects Explained

### 1. **LoginPage** (`login_page.py`)

**Handles:** User authentication

**Methods:**
- `login(username, password)` - Authenticate user
- `sign_out()` - Logout user

**Locators:**
- Email input: `#userEmail`
- Password input: `#userPassword`
- Login button: `#login`
- Sign-out button: `button[name="Sign Out"]`

**Example Usage:**
```python
from pages.login_page import LoginPage

login = LoginPage(page)
login.login("test@example.com", "password123")
# User is now logged in and on dashboard
```

---

### 2. **CartPage** (`cart_page.py`)

**Handles:** Shopping cart operations

**Methods:**
- `select_product(product_name)` - Add product to cart
- `count_cart_items()` - Get total items in cart
- `cart_history_empty()` - Check if cart is empty
- `checkout()` - Get subtotal and total amounts
- `checkout_press()` - Click checkout button

**Locators:**
- Product cards: `div.card`
- Cart button: `button[routerlink="/dashboard/cart"]`
- Empty message: `get_by_text("No Products in Your Cart !")`
- Checkout button: `button[name="Checkout"]`

**Example Usage:**
```python
cart = CartPage(page)
cart.select_product("ADIDAS ORIGINAL")  # Add product
count = cart.count_cart_items()         # Get count
amounts = cart.checkout()               # {'subtotal': 50, 'total': 50}
```

---

### 3. **OrderPaymentsPage** (`order_payments_page.py`)

**Handles:** Payment processing and order placement

**Methods:**
- `add_payment_details(card_data, coupon_code)` - Fill payment form and place order

**Locators:**
- Card dropdowns: `select[nth=0]`, `select[nth=1]`
- Country field: `input[placeholder="Select Country"]`
- Coupon field: `input[name="coupon"]`
- Place order button: `a.btnn.action__submit`

**Example Usage:**
```python
payment = OrderPaymentsPage(page)
coupon_msg, email, success_url = payment.add_payment_details(
    card_data={
        "card_number": "4542 9931 9292 2293",
        "cvv": "123",
        "card_name": "John Doe",
        "expiry_day": "05",
        "expiry_month": "11",
        "country": "India"
    },
    coupon_code="rahulshettyacademy"
)
```

---

### 4. **OrdersPage** (`orders_page.py`)

**Handles:** Order history and order details

**Methods:**
- `empty_orders_validation()` - Check empty orders message
- `order_ids_check()` - Get list of all order IDs
- `order_id_detail_check(orderID)` - Get specific order details

**Locators:**
- Orders button: `button[routerlink="/dashboard/myorders"]`
- Orders table: `table.table.table-bordered`
- Empty message: `get_by_text("You have No Orders...")`

**Example Usage:**
```python
orders = OrdersPage(page)
order_ids = orders.order_ids_check()  # ['ORD123', 'ORD124']
url, msg, billing, delivery = orders.order_id_detail_check('ORD123')
```

---

### 5. **InvoicePage** (`invoice_page.py`)

**Handles:** Invoice/order confirmation page

**Methods:**
- `get_order_ids()` - Extract order IDs from thank you page

**Locators:**
- Invoice container: `td.em-spacer-1`
- Order labels: `label.ng-star-inserted`
- Thank you message: `get_by_text("Thankyou for the order.")`

**Example Usage:**
```python
invoice = InvoicePage(page)
thank_you_msg, order_ids = invoice.get_order_ids()
# thank_you_msg: "Thankyou for the order."
# order_ids: ['ORD123']
```

---

## 📊 Test Data Management

### External Data Approach

Test data is stored in **JSON files** instead of being hardcoded:

#### `test_data/order_shopping_data.json`
```json
{
  "products": [
    { "product_name": "ADIDAS ORIGINAL" },
    { "product_name": "ZARA COAT 3" },
    { "product_name": "iphone 13 pro" }
  ]
}
```

#### `test_data/card_details.json`
```json
{
  "test_card": {
    "card_number": "4542 9931 9292 2293",
    "cvv": "123",
    "card_name": "John Doe",
    "expiry_day": "05",
    "expiry_month": "11",
    "country": "India"
  }
}
```

### Reading Test Data

```python
from utils.json_reader import json_helper_products, json_helper_payments

# Get product list
products = json_helper_products()  # Returns list of products

# Get payment card
card_data = json_helper_payments()  # Returns card details dict
```

**Advantages:**
- ✅ Easy to update without code changes
- ✅ Supports multiple test data sets
- ✅ Version control friendly
- ✅ Can swap data per environment

---

## 📋 Logging & Reports

### Logging Configuration (`pytest.ini`)

```ini
[pytest]
log_file = logs/automation_run.log
log_file_level = INFO
log_cli = true
log_cli_level = INFO
```

### Log Levels

- **INFO**: General test execution information
- **WARNING**: Non-critical issues (missing elements, timeouts)
- **ERROR**: Test failures

### Log Files Generated

```
logs/automation_run.log      # Complete test execution log

Example log output:
INFO - test_ui_workflow.py - Navigating to login page
INFO - login_page.py - Logging in with username: test@example.com
INFO - cart_page.py - Adding product: ADIDAS ORIGINAL to cart
WARNING - orders_page.py - Empty orders message not visible, skipping...
```

### HTML Reports

Generate HTML reports for test results:

```bash
pytest tests/test_ui_workflow.py -v \
  --html=reports/report.html --self-contained-html
```

Reports include:
- Test duration
- Pass/fail status
- Error messages and screenshots
- Execution timeline

---

## 🎓 Project Highlights for Recruiters

### Industry Best Practices Demonstrated

| Practice | Implementation |
|----------|-----------------|
| **Page Object Model** | Separate page classes for each UI page |
| **Test Organization** | Clear test directory structure |
| **Data Externalization** | JSON-based test data management |
| **Logging & Debugging** | Integrated file & console logging |
| **Fixture Management** | Session and function-scoped fixtures |
| **Error Handling** | Graceful skips vs hard failures |
| **Code Documentation** | Comments, logger statements throughout |
| **Scalability** | Easy to add new tests and pages |

### Technical Skills Showcased

✅ **Automation Framework Design** - POM architecture  
✅ **Test Automation Tools** - Playwright, Pytest  
✅ **Python Programming** - Classes, functions, data handling  
✅ **Web Element Interaction** - Locators, waits, actions  
✅ **Data-Driven Testing** - External data management  
✅ **Logging & Monitoring** - Integration with logging module  
✅ **Git Version Control** - Structured project organization  
✅ **End-to-End Testing** - Complete workflow automation  

### Real-World Application Scenarios

- **E-commerce automation** for regression testing
- **Payment processing validation** across different payment methods
- **Order management workflows** verification
- **Cross-page data consistency** checks
- **UI element state validation** (empty states, populated states)

---

## 🔧 Troubleshooting

### Tests Fail with "Element Not Found"

**Solution:** Check if selectors have changed in the website. Update locators in the respective page class.

```python
# Update in pages/login_page.py
self.email_input = "#userEmail"  # Change this if selector changed
```

### Tests Timeout

**Solution:** Increase wait timeout in Playwright calls:

```python
page.wait_for_url("**/dashboard/dash", timeout=10000)  # 10 seconds
```

### Logs Not Appearing

**Solution:** Ensure logger is initialized in your page class:

```python
import logging
logger = logging.getLogger(__name__)
logger.info("Action performed")
```

### HTML Report Not Generated

**Solution:** Install pytest-html plugin:

```bash
pip install pytest-html
```

---

## 📚 Learning Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Best Practices](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [Python Logging Module](https://docs.python.org/3/library/logging.html)

---

## 📞 Contact & Support

For questions or collaboration:
- **GitHub**: [anoysantra](https://github.com/anoysantra)
- **Project**: [Playwright Automation Testing](https://github.com/anoysantra/playwright_automation-testing)

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🎉 Key Takeaways

1. **Well-Structured**: Clear separation of concerns (pages, tests, fixtures, utils)
2. **Maintainable**: Changes to locators/logic are isolated to page classes
3. **Scalable**: Easy to add new test cases and page objects
4. **Professional**: Follows industry best practices and standards
5. **Production-Ready**: Logging, error handling, and reporting included

This project demonstrates the skills and knowledge required for **QA Automation Engineer** roles in modern software testing environments.

---

**Happy Testing! 🚀**
