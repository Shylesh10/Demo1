
class OpenCart:
    def __init__(self,page):
        self.page = page
        self.cartlink = page.locator(".shopping_cart_link")
        self.checkoutbutton = page.get_by_role("button",name="Checkout")

    def opencart(self):
        self.cartlink.click()

    def checkout(self):
        self.checkoutbutton.click()