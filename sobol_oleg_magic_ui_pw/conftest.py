from sobol_oleg_magic_ui_pw.pages.account_create_page import AccountCreate
from sobol_oleg_magic_ui_pw.pages.eco_friendly_page import EcoFriendly
from sobol_oleg_magic_ui_pw.pages.sale_page import Sale
import pytest


@pytest.fixture()
def account_create_page(page):
    return AccountCreate(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendly(page)


@pytest.fixture()
def sale_page(page):
    return Sale(page)
