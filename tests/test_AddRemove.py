from playwright.sync_api import Page,expect
from pages.cartpage import CartPage
from pages.loginpage import LoginPage
import json
import pytest

with open("data/cred.json") as file:
    test_data = json.load(file)
    user_credentials = test_data['cred']

@pytest.mark.parametrize('user_cred',user_credentials)    
def test_addremove(page:Page,
                   login_page:LoginPage,
                   cart_page:CartPage,
                   user_cred):
    
    username = user_cred["userName"]
    password = user_cred["passWord"]
   
    #Login page
    login_page.login(username,password)
    #YOUR CART PAGE
    #Add ,Open Cart& Verify 2 products
    cart_page.add_to_cart_items()
    expect(page.locator(".inventory_item_name").filter(has_text="Sauce Labs Backpack")).to_be_visible()
    expect(page.locator(".inventory_item_name").filter(has_text="Sauce Labs Bike Light")).to_be_visible()
    #Remove Sauce Labs Backpack,Verify only Bike Light remains & Verify cart badge = 1
    cart_page.remove_cart_items()
    expect(page.locator(".inventory_item_name").filter(has_text="Sauce Labs Backpack")).not_to_be_visible()
    expect(page.locator(".inventory_item_name").filter(has_text="Sauce Labs Bike Light")).to_be_visible()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

