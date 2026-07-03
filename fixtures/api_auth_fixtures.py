import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext

try:
    from utils.api_logger import get_api_logger
except ModuleNotFoundError:  # pragma: no cover - fallback for package-style imports
    from ..utils.api_logger import get_api_logger

LOGGER = get_api_logger(__name__)

USER_CREDENTIALS = {"userEmail": "testuserleo13@gmail.com", "userPassword": "Sample@1234"}
AUTH_API_URL = "https://rahulshettyacademy.com/api/ecom/auth/login"
AUTH_HEADERS = {"Content-Type": "application/json"}

authenticated_user_id = ""


@pytest.fixture(scope="session")
def auth_using_api(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    """Create an authenticated API request context for the duration of the test session."""
    global authenticated_user_id
    api_request_context: APIRequestContext = playwright.request.new_context()
    api_response = api_request_context.post(AUTH_API_URL, data=USER_CREDENTIALS, headers=AUTH_HEADERS)
    response_payload = api_response.json()
    LOGGER.info("Authentication response payload: %s", response_payload)

    access_token = response_payload.get("token")
    authenticated_user_id = response_payload.get("userId")

    if not access_token:
        raise RuntimeError("❌ No token found in login response")
    if not authenticated_user_id:
        raise RuntimeError("❌ No userId found in login response")

    authenticated_request_context = playwright.request.new_context(
        extra_http_headers={"Authorization": f"{access_token}"}
    )

    yield authenticated_request_context
    authenticated_request_context.dispose()


@pytest.fixture(scope="session")
def user(auth_using_api: APIRequestContext):
    """Expose the authenticated user's ID to tests that need it."""
    yield authenticated_user_id
