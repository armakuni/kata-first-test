import unittest


def second_lowest_number(numbers):
    numbers.sort()
    return numbers[1]


class LowestNumberTestCase(unittest.TestCase):
    def test_with_multiple_numbers_it_returns_the_second_lowest(self):
        actual = second_lowest_number([9, -1, 4, 15, 7])
        self.assertEqual(actual, 4)

    def test_that_with_one_number_it_none(self):
        actual = second_lowest_number([9])
        self.assertEqual(actual, None)


if __name__ == '__main__':
    unittest.main()