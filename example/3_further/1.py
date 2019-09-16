def second_lowest_number(numbers):
    numbers.sort()

    if len(numbers) < 2:
        raise Exception('You need at least 2 numbers!')

    return numbers[1]
