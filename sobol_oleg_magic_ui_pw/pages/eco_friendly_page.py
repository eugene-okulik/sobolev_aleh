from playwright.sync_api import expect

from sobol_oleg_magic_ui_pw.pages.base_page import BasePage
from sobol_oleg_magic_ui_pw.pages.locators.page_locators import EcoFriendlyLoc as loc


class EcoFriendly(BasePage):
    page_url = "/collections/eco-friendly.html"

    def check_page_title(self, expected_title):
        expect(self.find(loc.page_title_loc)).to_have_text(expected_title)

    def check_product_items_displayed(self):
        expect(self.find(loc.product_items_loc)).not_to_have_count(0)

    def search_product_result(self, search_term):
        search_field = self.find(loc.search_field_loc)
        search_field.fill(search_term)
        search_field.press("Enter")
        product_items = self.find(loc.product_items_loc)
        expect(product_items).not_to_have_count(0)
