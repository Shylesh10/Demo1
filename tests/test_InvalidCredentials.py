from playwright.sync_api import Page,expect
from pages.loginpage import LoginPage
import json
import pytest


with open("data/invalidcred.json") as file:
    test_data = json.load(file)
    user_credentials = test_data['invalidcred']

@pytest.mark.parametrize('user_cred',user_credentials)
def test_invalidcredentials(page:Page,login_page:LoginPage,user_cred):
    username = user_cred["userName"]
    password = user_cred["passWord"]
    #Login page
    login_page.login(username,password)
    expect(page.get_by_role("alert")).to_have_text("Epic sadface: Username and password do not match any user in this service")
    