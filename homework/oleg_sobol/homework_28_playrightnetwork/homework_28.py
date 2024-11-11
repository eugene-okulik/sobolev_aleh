from playwright.sync_api import Page, Route, expect
import re
import json


def test_change_iphone_name(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = "яблокофон 16 про"
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route(re.compile('/digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('button[data-trigger-id="digitalmat-1"]').click()
    popup_title = page.locator('h2[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(popup_title).to_have_text("яблокофон 16 про")
