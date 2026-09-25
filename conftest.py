import pytest
from playwright.sync_api import Page
from pages.cartpage import CartPage
from pages.infopage import InfoPage
from pages.loginpage import LoginPage
from pages.opencart import OpenCart
from pages.overviewpage import OverviewPage

@pytest.fixture(autouse=True)
def setup_teardown(page: Page):
    page.goto("https://www.saucedemo.com/")
    yield
    
@pytest.fixture
def login_page(page:Page):
    return LoginPage(page)

@pytest.fixture
def cart_page(page:Page):
    return CartPage(page)

@pytest.fixture
def open_cart(page:Page):
    return OpenCart(page)

@pytest.fixture
def info_page(page:Page):
    return InfoPage(page)

@pytest.fixture
def overview_page(page:Page):
    return OverviewPage(page)

