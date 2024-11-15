def test_page_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_title("Sale")


def test_logo_displayed(sale_page):
    sale_page.open_page()
    sale_page.check_logo_displayed_on_page()


def test_menu_sale_tab_selected(sale_page):
    sale_page.open_page()
    sale_page.check_menu_displayed()
