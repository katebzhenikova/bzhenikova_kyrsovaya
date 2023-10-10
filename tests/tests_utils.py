import pytest
import json
from func.utils import executed_sorted_file
from func.utils import Cardoperations
from datetime import datetime


def test_executed_sorted_file():
    file = [
        {"id": 3, "state": "EXECUTED", "date": "2020-01-02T02:08:58.425572"},
        {"id": 1, "state": "EXECUTED", "date": "2020-03-02T02:08:58.425572"},
        {"id": 2, "state": "CANCELED", "date": "2020-02-02T02:08:58.425572"},
        {"id": 4, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 5, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    ]
    result = executed_sorted_file(file)
    assert result[0]['id'] == 1
    assert result[1]['id'] == 3
    assert result[2]['id'] == 5
    assert len(result) == 3


def test_executed_sorted_file_empty():
    file = []
    result = executed_sorted_file(file)
    assert result == []


def test_Cardoperations_operation_count():
    info_list = [{'status': 'EXECUTED', 'date': '2023-12-01T12:30:00.000', 'from': 'Visa Gold 1234567812345678',
                  'to': 'МИР 8765432187654321'},
                 {'status': 'EXECUTED', 'date': '2023-11-11T12:30:00.000', 'from': 'Visa Classic 1596837868705199',
                  'to': 'Счет 64686473678894779589'},
                 {'status': 'CANCELED', 'date': '2023-11-11T12:30:00.000', 'from': 'Maestro 1596837868705199',
                  'to': 'Visa Gold 1234567812345678'},
                 {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'Visa Platinum 7158300734726758',
                  'to': 'Visa Classic 1596837868705199'},
                 {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'MasterCard 7158300734726758',
                  'to': 'Visa Platinum 8990922113665229'},
                 {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'Счет 48894435694657014368',
                  'to': 'Счет 38976430693692818358'},
                 {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'МИР 8765432187654321',
                  'to': 'MasterCard 7158300734726758'},
                 ]
    card_operation = Cardoperations(info_list)
    card_operation.operation_count()
    assert len(card_operation.operation) == 5


def test_Cardoperations_date_format():
    info_list = [{'status': 'EXECUTED', 'date': '2023-12-01T12:30:00.000', 'from': 'Visa Gold 1234567812345678',
                  'to': 'МИР 8765432187654321'},
                 ]
    card_operation = Cardoperations(info_list)
    card_operation.operation_count()
    new_operations = card_operation.date_format()
    assert new_operations[0]['date'] == datetime.strptime('2023-12-01', '%Y-%m-%d').strftime("%d.%m.%Y")


def test_Cardoperations_card_format():
    info_list = [
        {'status': 'EXECUTED', 'date': '2023-12-01T12:30:00.000', 'from': 'Visa Gold 1234567812345678',
         'to': 'МИР 8765432187654321'},
        {'status': 'EXECUTED', 'date': '2023-11-11T12:30:00.000', 'from': 'Visa Classic 1596837868705199',
         'to': 'Счет 64686473678894779589'},
        {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'Visa Platinum 7158300734726758',
         'to': 'Visa Classic 1596837868705199'},
        {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'MasterCard 7158300734726758',
         'to': 'Visa Platinum 8990922113665229'},
        {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'Счет 48894435694657014368',
         'to': 'Счет 38976430693692818358'},
        {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'МИР 8765432187654321',
         'to': 'MasterCard 7158300734726758'},
        ]
    card_operation = Cardoperations(info_list)
    card_operation.operation_count()
    new_operations = card_operation.card_format()
    assert new_operations[0]['from'] == 'Visa Gold 1234 56** **** 5678'
    assert new_operations[1]['from'] == 'Visa Classic 1596 83** **** 5199'
    assert new_operations[2]['from'] == 'Visa Platinum 7158 30** **** 6758'
    assert new_operations[3]['from'] == 'MasterCard 7158 30** **** 6758'
    assert new_operations[4]['from'] == 'Счет **4368'


def test_Cardoperations_count_format():
    info_list = [{'status': 'EXECUTED', 'date': '2023-12-01T12:30:00.000', 'from': 'Visa Gold 1234567812345678',
                  'to': 'МИР 8765432187654321'},
                 {'status': 'EXECUTED', 'date': '2023-11-11T12:30:00.000', 'from': 'Visa Classic 1596837868705199',
                  'to': 'Счет 64686473678894779589'},
                 {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'Visa Platinum 7158300734726758',
                  'to': 'Visa Classic 1596837868705199'},
                 {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'MasterCard 7158300734726758',
                  'to': 'Visa Platinum 8990922113665229'},
                 {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'Счет 48894435694657014368',
                  'to': 'Счет 38976430693692818358'},
                 {'status': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'from': 'МИР 8765432187654321',
                  'to': 'MasterCard 7158300734726758'},
                 ]
    card_operation = Cardoperations(info_list)
    card_operation.operation_count()
    new_operations = card_operation.count_format()
    assert new_operations[0]['to'] == 'МИР 8765 43** **** 4321'
    assert new_operations[1]['to'] == 'Счет **9589'
    assert new_operations[2]['to'] == 'Visa Classic 1596 83** **** 5199'
    assert new_operations[3]['to'] == 'Visa Platinum 8990 92** **** 5229'
    assert new_operations[4]['to'] == 'Счет **8358'
