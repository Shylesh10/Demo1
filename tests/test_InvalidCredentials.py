from playwright.sync_api import Page,expect
from pages.loginpage import LoginPage
import json
import pytest


with open("data/cred.json") as file:
    test_data = json.load(file)
    user_credentials = test_data['invalidcred']

@pytest.mark.parametrize('user_cred',user_credentials)
def test_invalidcredentials(page:Page,login_page:LoginPage,user_cred):
    username = user_cred["userName"]
    password = user_cred["passWord"]
    #Login page
    login_page.login(username,password)
    