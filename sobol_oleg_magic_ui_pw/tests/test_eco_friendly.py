def test_page_title(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_page_title("Eco Friendly")


def test_product_items_displayed(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_product_items_displayed()


def test_search_functionality(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.search_product_result("Bella")
