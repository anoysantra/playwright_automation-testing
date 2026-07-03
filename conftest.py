import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from fixtures.browser_fixtures import page_initialization
from fixtures.api_auth_fixtures import auth_using_api, user
from fixtures.api_auth_browser_fixtures_for_api import auth_browser_context