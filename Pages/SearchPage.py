from playwright.sync_api import Locator
from Pages.BasePage import BasePage


class SearchPage(BasePage):
    pass

    @property
    def search_relevance_box(self) -> Locator:
        return self.page.get_by_test_id("filter-sort")

    # @property
    # def click_by_filter(self) -> Locator:
    #     return self.page.get_by_text()

    @property
    def click_button_apply(self) -> Locator:
        return self.page.get_by_test_id("apply-filters-button")
    @property
    def enum_filter(self):
        if self.page.locator('input[value="male"]'):


    def choose_filter(self, filter_type: str):
        self.search_relevance_box.click()
        self.page.get_by_text(filter_type).click()
        self.click_button_apply.click()



