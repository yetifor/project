from playwright.sync_api import Page,expect
from Config.ConfigReader import ConfigReader
from Pages.HomePage import HomePage
from Pages.BasePage import BasePage
from Pages.SearchPage import SearchPage
import pytest


from Config.ConfigReader import ConfigReader

import os

from conftest import config1

print(f"Текущая рабочая директория: {os.getcwd()}")
print(f"Файл config.json существует: {os.path.exists('config.json')}")

@pytest.mark.parametrize('name, n, filter_type', ConfigReader.read_config())
def test_main(page,home,search, name,n, filter_type):
    home.search(name)

    search.choose_filter(filter_type)

