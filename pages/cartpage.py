class CartPage:
    def __init__(self,page):
        self.page = page
        self.addtocart = page.locator("#add-to-cart-sauce-labs-backpack")

    def cartpage(self):
        self.addtocart.click()