import pytest
import os
import json
from func.utils import load_file  # замените на имя вашего модуля

def test_load_file_valid_json():
    # Подготовка
    valid_json_file = "test_valid.json"
    with open(valid_json_file, "w") as file:
        json.dump({"key": "value"}, file)

    # Вызов функции и проверка результата
    data = load_file(valid_json_file)
    assert data == {"key": "value"}

    # Уборка
    os.remove(valid_json_file)


def test_load_file_invalid_json():
    # Подготовка
    invalid_json_file = "test_invalid.json"
    with open(invalid_json_file, "w") as file:
        file.write("not a json")

    # Проверка, что вызов функции поднимает исключение
    with pytest.raises(json.JSONDecodeError):
        load_file(invalid_json_file)

    # Уборка
    os.remove(invalid_json_file)


def test_load_file_no_such_file():
    # Проверка, что вызов функции с несуществующим файлом поднимает исключение
    with pytest.raises(FileNotFoundError):
        load_file("no_such_file.json")
