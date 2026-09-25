class LoginPage:

    def __init__(self,page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.locator("#login-button")


    def login(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
