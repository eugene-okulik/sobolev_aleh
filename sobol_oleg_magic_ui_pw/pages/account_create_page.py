import re

from playwright.sync_api import expect

from sobol_oleg_magic_ui_pw.pages.base_page import BasePage
from sobol_oleg_magic_ui_pw.pages.locators.page_locators import AccountCreateLoc as loc


class AccountCreate(BasePage):
    page_url = "/customer/account/create/"

    def required_fields_present_account_form(self):
        expect(self.find(loc.firstname_field_loc)).to_be_visible()
        expect(self.find(loc.lastname_field_loc)).to_be_visible()
        expect(self.find(loc.email_field_loc)).to_be_visible()
        expect(self.find(loc.password_loc)).to_be_visible()
        expect(self.find(loc.confirm_password_field_loc)).to_be_visible()

    def send_invalid_password(self, password):
        self.find(loc.password_loc).fill(password)
        self.find(loc.create_button_loc).click()

    def check_error_message(self, message):
        error_message = self.find(loc.error_message_validation_loc)
        expect(error_message).to_have_text(message)

    def click_create_button(self):
        self.find(loc.create_button_loc).click()

    def check_validation_messages(self):
        expect(self.find(loc.firstname_error_message_loc)).to_be_visible()
        expect(self.find(loc.lastname_error_message_loc)).to_be_visible()
        expect(self.find(loc.email_error_message_loc)).to_be_visible()
        expect(self.find(loc.password_error_message_loc)).to_be_visible()
        expect(self.find(loc.confirm_password_error_message_loc)).to_be_visible()

    def check_fields_highlighted_red(self):
        expect(self.find(loc.firstname_field_loc)).to_have_class(re.compile(".*mage-error.*"))
        expect(self.find(loc.lastname_field_loc)).to_have_class(re.compile(".*mage-error.*"))
        expect(self.find(loc.email_field_loc)).to_have_class(re.compile(".*mage-error.*"))
        expect(self.find(loc.password_loc)).to_have_class(re.compile(".*mage-error.*"))
        expect(self.find(loc.confirm_password_field_loc)).to_have_class(re.compile(".*mage-error.*"))
