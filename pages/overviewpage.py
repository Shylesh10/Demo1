class  OverviewPage:
    def __init__(self,page):
        self.page = page
        self.finishbutton = page.get_by_role("button",name="Finish")

    def overviewpage(self):
        self.finishbutton.click()