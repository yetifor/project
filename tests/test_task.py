from playwright.sync_api import expect,Page

def test_loader(page: Page):
    page.goto('http://localhost:7080')
    expect(page).to_have_title('The Internet')
    page.get_by_role("link", name="Dynamic Loading").click()
    page.wait_for_url("**/dynamic_loading")
    page.get_by_role("link", name="Example 1: Element on page").click()
    page.wait_for_url("**/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    loader = page.locator("#loading")
    expect(loader).to_be_visible()

def test_autorisation(page: Page):
    page.goto('http://localhost:7080')
    expect(page).to_have_title('The Internet')
    page.locator('//*[@id="content"]/ul/li[21]/a').click()
    page.wait_for_url('**/login')
    page.get_by_role('textbox', name='Username').fill('username')
    page.get_by_role('textbox', name='Password').fill('password')
    page.get_by_role('button', name=' Login').click()
    expect(page.get_by_text('Your username is invalid!')).to_be_visible()