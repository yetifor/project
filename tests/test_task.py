from playwright.sync_api import expect, Page
from faker import Faker

fake = Faker()
ADRESS = 'http://localhost:7080'


def test_login_loader(page: Page):
    page.goto(ADRESS)
    page.get_by_role("link", name="Dynamic Loading").click()
    page.wait_for_url("**/dynamic_loading")
    page.get_by_role("link", name="Example 1: Element on page").click()
    page.wait_for_url("**/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    loader = page.locator("#loading")
    expect(loader).to_be_visible()
    page.wait_for_timeout(10000)
    expect(loader).to_be_hidden()
    page.goto(ADRESS)
    page.wait_for_timeout(5000)
    page.get_by_role('link', name='Form Authentication').click()
    page.wait_for_url('**/login')
    page.get_by_role('textbox', name='Username').fill(fake.user_name())
    page.get_by_role('textbox', name='Password').fill(fake.password())
    page.get_by_role('button', name=' Login').click()
    assert page.get_by_text('Your username is invalid!').is_visible(), \
        'Сообщение "Your username is invalid!" не отображетсяя'
