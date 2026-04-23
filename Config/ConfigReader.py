import json
import os
from Config import *

class ConfigReader:
    def __init__(self, page):
        self.page = page


    @staticmethod
    def read_config()->list:
        module_dir = os.path.dirname(os.path.abspath(__file__))
        # Формируем путь к config.json в той же директории
        config_path = os.path.join(module_dir, 'config.json')
        with open('config.json') as json_file:
            gata = json.load(json_file)

        return [tuple(item.values()) for item in gata]
    # @classmethod
    # def _load_config(self) -> None:
    #     """Загружает конфигурацию из JSON‑файла."""
    #     # Корень проекта — директория с conftest.py
    #     root_dir = os.path.dirname(os.path.abspath('conftest.py'))
    #     config_path = os.path.join(root_dir, '../config.json')
    #
    #     if not os.path.exists(config_path):
    #         raise FileNotFoundError(f"Конфигурационный файл не найден: {config_path}")
    #
    #     with open(config_path, 'r', encoding='utf-8') as f:
    #         self._config_data = json.load(f)




