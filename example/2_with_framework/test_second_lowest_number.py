import pytest


def second_lowest_number(numbers):
    numbers.sort()
    return numbers[1]


def test_with_multiple_numbers_it_returns_the_second_lowest():
    actual = second_lowest_number([9, -1, 4, 15, 7])
    assert actual == 4


def test_that_with_one_number_it_none():
    actual = second_lowest_number([9])
    assert actual is None


if __name__ == '__main__':
    pytest.main()
