from playwright.sync_api import Page
import pytest
import json
from Pages.BasePage import BasePage
from Config.ConfigReader import ConfigReader
from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage


@pytest.fixture(autouse=True)
def open_localhost(page: Page):
    page.goto("http://localhost:5000/")
    yield page


@pytest.fixture(autouse=True)
def home(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture(autouse=True)
def search(page: Page) -> SearchPage:
    return SearchPage(page)


@pytest.fixture(autouse=True)
def config1(page: Page) -> ConfigReader:
    return ConfigReader(page)
