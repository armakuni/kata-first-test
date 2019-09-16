def second_lowest_number(numbers):
    numbers.sort()
    return numbers[1]


assert second_lowest_number([9, -1, 4, 15, 7]) is 4
