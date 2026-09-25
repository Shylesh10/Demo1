class InfoPage:
    def __init__(self,page):
        self.page = page
        self.firstname = page.get_by_placeholder("First Name")
        self.lastname = page.get_by_placeholder("Last Name")
        self.zipcode = page.get_by_placeholder("Zip/Postal Code")
        self.continuebutton = page.locator("#continue")

    def infopage(self):
        self.firstname.fill("Demo")
        self.lastname.fill("Test1")
        self.zipcode.fill("560001")
        self.continuebutton.click()
