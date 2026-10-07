class CartPage:
    def __init__(self,page):
        self.page = page
        self.addbackpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.addbikelight = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.cartbutton = page.locator("#shopping_cart_container") 
        self.removebackpack = page.locator("#remove-sauce-labs-backpack")

    def cartpage(self):
        self.addbackpack.click()

    def add_to_cart_items(self):
        self.addbackpack.click()
        self.addbikelight.click()
        self.cartbutton.click()

    def remove_cart_items(self):
        self.removebackpack.click()
