import re
from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")

    def handle_dialog(alert: Dialog):
        alert.accept()

    page.on("dialog", handle_dialog)
    button_alert = page.get_by_role("link", name="Click")
    button_alert.click()
    result_text = page.locator("#result-text")
    expect(result_text).to_have_text("Ok")


def test_new_tab(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")

    button_tab = page.get_by_role("link", name="Click")
    with context.expect_page() as new_page_event:
        button_tab.click()
    new_page = new_page_event.value
    result = new_page.locator("#result-text")
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()
    expect(button_tab).to_be_enabled()


def test_wait_button_visible(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    button = page.locator("#colorChange")
    expect(button).to_have_class(re.compile("text-danger"))
    button.click()
