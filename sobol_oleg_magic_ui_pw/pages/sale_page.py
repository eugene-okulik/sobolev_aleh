from playwright.sync_api import expect
from sobol_oleg_magic_ui_pw.pages.base_page import BasePage
from sobol_oleg_magic_ui_pw.pages.locators.page_locators import SaleLoc as loc


class Sale(BasePage):
    page_url = "/sale.html"

    def check_page_title(self, expected_title):
        expect(self.find(loc.page_title_loc)).to_have_text(expected_title)

    def check_logo_displayed_on_page(self):
        expect(self.find(loc.logo_loc)).to_be_visible()

    def check_menu_displayed(self):
        expect(self.find(loc.menu_loc)).to_be_visible()
