from playwright.sync_api import expect, Page
from faker import Faker

fake = Faker()
ADRESS = 'http://localhost:5000/'


def test_login_loader(page: Page):
    page.goto(ADRESS)
    page.get_by_test_id("nav-login").click()
    page.wait_for_url("**/login")
    page.get_by_test_id("login-username").fill(fake.user_name())
    page.get_by_test_id("login-password").fill(fake.password())
    page.get_by_test_id("login-submit").click()
    loader = page.get_by_test_id("login-submit-spinner")
    expect(loader).to_be_visible()
    page.wait_for_timeout(10000)
    expect(loader).to_be_hidden()
    page.wait_for_timeout(5000)
    assert page.get_by_text('Invalid login or password.').is_visible(), \
        'Сообщение "Invalid login or password." не отображетсяя'