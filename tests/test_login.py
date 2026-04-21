from playwright.sync_api import expect, Page
from faker import Faker

fake = Faker()
ADRESS = 'http://localhost:5000/'


def test_login_loader(page: Page):
    page.goto(ADRESS)
    page.get_by_test_id("nav-login").click()
    page.get_by_test_id("login-username").fill(fake.user_name())
    page.get_by_test_id("login-password").fill(fake.password())
    page.get_by_test_id("login-submit").click()
    loader = page.get_by_test_id("login-submit-spinner")
    expect(loader).to_be_visible()
    expect(loader).to_be_hidden()
    locator = page.get_by_test_id("login-error-inline")
    text = locator.inner_text()
    assert text == 'Invalid login or password.', \
        ('Сообщение "Invalid login or password." не отображетсяя.'
         'actual result:', text)