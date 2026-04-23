from playwright.sync_api import Locator
from Pages.BasePage import BasePage

class HomePage(BasePage):



    #Locators

    @property
    def search_input(self)->Locator:
        return self.page.get_by_test_id("search-input")

    @property
    def search_button(self)->Locator:
        return self.page.get_by_test_id("search-button")

    #Actions
    def search(self, *args):
        self.search_input.fill(*args)
        self.search_button.click()




