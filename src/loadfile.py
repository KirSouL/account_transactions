# импорт библиотек для работы с БД и форматом дата-время
import json
from datetime import datetime


def load_file():
    """
    Функция считывающая базу данных по операциям пользователя.
    :return: возвращает набор всех операций
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        operations = json.load(file)

    return operations


def executed_operation():
    """
    Функция формирования списка успешных операций
    :return: возвращает набор выполненных операций
    """
    list_executed = []

    for item in load_file():
        if item and item["state"] == "EXECUTED":
            list_executed.append(item)

    return list_executed


def sorted_executed_operation():
    """
    Функция сортировки операций по дате и времени
    :return: возвращает отсортированный по дате набор операций
    """
    list_sorted = executed_operation()

    list_sorted.sort(key=lambda x: datetime.strptime(x.get("date"), "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)

    return list_sorted
