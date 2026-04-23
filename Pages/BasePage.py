from playwright.sync_api import Page

class BasePage(Page):
    def __init__(self, page):
        self.page = page

