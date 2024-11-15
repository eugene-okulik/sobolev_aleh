def test_required_fields_present(account_create_page):
    account_create_page.open_page()
    account_create_page.required_fields_present_account_form()


def test_password_confirmation_error(account_create_page):
    account_create_page.open_page()
    account_create_page.send_invalid_password(password="password")
    account_create_page.check_error_message(message="Minimum of different classes of characters in password is 3. "
                                                    "Classes of characters: Lower Case, Upper Case, Digits, "
                                                    "Special Characters.")


def test_text_validation_all_field(account_create_page):
    account_create_page.open_page()
    account_create_page.click_create_button()
    account_create_page.check_validation_messages()
    account_create_page.check_fields_highlighted_red()
