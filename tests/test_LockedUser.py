from playwright.sync_api import Page,expect
from pages.loginpage import LoginPage

import json
import pytest

with open("data/cred.json") as file:
    test_data = json.load(file)
    user_credentials = test_data['lockeduser']

@pytest.mark.parametrize('user_cred',user_credentials)
def test_lockeduser(page:Page,login_page : LoginPage,user_cred):
    username = user_cred["userName"]
    password = user_cred["passWord"]
    #Login page
    login_page.login(username,password)
    expect(page.get_by_role("alert")).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    expect(page).to_have_url("https://www.saucedemo.com/")