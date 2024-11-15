class AccountCreateLoc:
    firstname_field_loc = "#firstname"
    lastname_field_loc = "#lastname"
    email_field_loc = "#email_address"
    password_loc = "#password"
    confirm_password_field_loc = "#password-confirmation"
    create_button_loc = "button.action.submit.primary"

    error_message_validation_loc = "//*[@id='password-error']"

    firstname_error_message_loc = "#firstname-error"
    lastname_error_message_loc = "#lastname-error"
    email_error_message_loc = "#email_address-error"
    password_error_message_loc = "#password-error"
    confirm_password_error_message_loc = "#password-confirmation-error"


class EcoFriendlyLoc:
    page_title_loc = "h1"
    product_items_loc = ".product-item"
    search_field_loc = "#search"


class SaleLoc:
    page_title_loc = "h1"
    logo_loc = "a.logo img"
    menu_loc = "nav.navigation"
