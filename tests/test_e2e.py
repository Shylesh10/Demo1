from playwright.sync_api import Page,expect
from pages.cartpage import CartPage
from pages.infopage import InfoPage
from pages.loginpage import LoginPage
from pages.opencart import OpenCart
from pages.overviewpage import OverviewPage
import json
import pytest

with open("data/cred.json") as file:
    test_data = json.load(file)
    user_credentials = test_data['cred']

@pytest.mark.parametrize('user_cred',user_credentials)    
def test_e2e(page:Page,
             login_page:LoginPage,
             cart_page:CartPage,
             open_cart:OpenCart,
             info_page:InfoPage,
             overview_page:OverviewPage,
             user_cred):
    
    username = user_cred["userName"]
    password = user_cred["passWord"]
   
    #Login page
    login_page.login(username,password)
    #Add to cart page
    cart_page.cartpage()
    #Open cart
    open_cart.opencart()
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    open_cart.checkout()
    #Information page
    info_page.infopage()
    #Overview page
    overview_page.overviewpage()
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()

