import pytest
from src.loadfile import load_file, executed_operation, sorted_executed_operation


@pytest.fixture
def database_test():
    list_test_one = [
                        {
                            'id': 873106923,
                            'state': 'EXECUTED',
                            'date': '2019-03-23T01:09:46.296404',
                            'operationAmount': {
                                                'amount': '43318.34',
                                                'currency': {
                                                            'name': 'руб.',
                                                            'code': 'RUB'
                                                            }
                                                },
                            'description': 'Перевод со счета на счет',
                            'from': 'Счет 44812258784861134719',
                            'to': 'Счет 74489636417521191160'
                        },
                        {
                            'id': 736942989,
                            'state': 'EXECUTED',
                            'date': '2019-09-06T00:48:01.081967',
                            'operationAmount': {
                                                'amount': '6357.56',
                                                'currency': {
                                                            'name': 'USD',
                                                            'code': 'USD'
                                                            }
                                                },
                            'description': 'Перевод организации',
                            'from': 'Visa Gold 3654412434951162',
                            'to': 'Счет 59986621134048778289'
                        }
                    ]
    return list_test_one


@pytest.fixture
def example_executed_zero():
    dict_test = {
                'id': 441945886,
                'state': 'EXECUTED',
                'date': '2019-08-26T10:50:58.294041',
                'operationAmount': {
                                    'amount': '31957.58',
                                    'currency': {
                                                'name': 'руб.',
                                                'code': 'RUB'
                                                }
                                    },
                'description': 'Перевод организации',
                'from': 'Maestro 1596837868705199',
                'to': 'Счет 64686473678894779589'
                }
    return dict_test


@pytest.fixture
def sorted_example():
    list_test_two = [
                        {
                            'id': 360577236,
                            'state': 'EXECUTED',
                            'date': '2019-09-07T07:20:13.889610',
                            'operationAmount': {
                                                 'amount': '18536.73',
                                                 'currency': {
                                                                 'name': 'руб.',
                                                                 'code': 'RUB'
                                                             }
                                                },
                            'description': 'Перевод с карты на карту',
                            'from': 'Maestro 4284341727554246',
                            'to': 'МИР 1582474475547301'
                        },
                        {
                            'id': 361044570,
                            'state': 'EXECUTED',
                            'date': '2018-03-02T02:03:11.563721',
                            'operationAmount': {
                                                'amount': '7484.91',
                                                'currency': {
                                                                'name': 'USD',
                                                                'code': 'USD'
                                                            }
                                                },
                            'description': 'Перевод организации',
                            'from': 'Счет 96008924215040031147',
                            'to': 'Счет 30377212495530283001'
                        }
                    ]

    return list_test_two


def test_loadfile_one(database_test):
    assert load_file()[5] == database_test[0], load_file()[-10] == database_test[1]


def test_loadfile_two(example_executed_zero):
    assert executed_operation()[0] == example_executed_zero


def test_loadfile_three(sorted_example):
    assert sorted_executed_operation()[8] == sorted_example[0], sorted_executed_operation()[-9] == sorted_example[1]
