import pytest
from src.utils import get_mask, date_operation


@pytest.fixture
def list_test():
    list_to_utils = [
                        ['Maestro', '1234123412341234'],
                        ['Visa', 'Platinum', '1234123412341234'],
                        ['Счет', '12341234123412341234'],
                        ['2018-11-29T07:18:23.941293']
                    ]
    return list_to_utils


def test_get_mask_one(list_test):
    assert get_mask(list_test[0]) == "Maestro 1234 12** **** 1234"


def test_get_mask_two(list_test):
    assert get_mask(list_test[1]) == "Visa Platinum 1234 12** **** 1234"


def test_get_mask_three(list_test):
    assert get_mask(list_test[2]) == "Счет **1234"


def test_date_operation(list_test):
    assert date_operation(list_test[3][0]) == "29.11.2018"
