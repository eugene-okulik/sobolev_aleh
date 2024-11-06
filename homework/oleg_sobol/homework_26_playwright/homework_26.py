from playwright.sync_api import Page


def test_form_authentication(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    form_authentication_link = page.get_by_role("link", name="Form Authentication")
    form_authentication_link.click()

    username_field = page.get_by_role("textbox", name="Username")
    username_field.fill("alex")
    password_field = page.get_by_role("textbox", name="Password")
    password_field.fill("password321")

    login_button = page.get_by_role("button", name="Login")
    login_button.click()


def test_automation_form_fill(page: Page):
    first_name = "Alex"
    last_name = "Flex"
    user_email = "alexflex@example.com"
    phone_number = "1234567890"
    date_of_birth = "20 Nov 1995"
    subjects = "Maths"
    address = "Minsk, street"
    state = "NCR"
    city = "Delhi"

    page.goto("https://demoqa.com/automation-practice-form", timeout=60000)

    first_name_field = page.get_by_placeholder("First Name")
    first_name_field.fill(first_name)

    last_name_field = page.get_by_placeholder("Last Name")
    last_name_field.fill(last_name)

    email_field = page.get_by_placeholder("name@example.com")
    email_field.fill(user_email)

    gender_radio = page.locator("//label[text()='Male']")
    gender_radio.click()

    phone_field = page.get_by_placeholder("Mobile Number")
    phone_field.fill(phone_number)

    date_field = page.locator("//*[@id='dateOfBirthInput']")
    date_field.click()
    date_field.press("Meta+a")
    date_field.fill(date_of_birth)
    date_field.press("Enter")

    subjects_field = page.locator("//*[@id='subjectsInput']")
    subjects_field.press_sequentially(subjects, delay=200)
    subjects_field.press("Enter")

    sports_checkbox = page.locator("//label[text()='Sports']")
    sports_checkbox.click()

    music_checkbox = page.locator("//label[text()='Music']")
    music_checkbox.click()

    address_field = page.get_by_placeholder("Current Address")
    address_field.fill(address)

    state_and_field = page.locator("//*[@id='state']")
    state_and_field.click()
    state_and_field.press_sequentially(state, delay=200)
    state_and_field.press("Enter")
    state_and_field.press("Tab")
    state_and_field.press_sequentially(city, delay=200)
    state_and_field.press("Enter")

    submit_button = page.get_by_role("button", name="Submit")
    submit_button.click()
