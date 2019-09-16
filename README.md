# Kata: First Test

This is a short exercise to get you used to the basic ideas of testing. The code is all in this README. However, to see the examples in a code directory see the "example" [directory](example).

## Testing without a framework

Here are a list of numbers

* 9
* -1
* 4
* 7
* 15

We're now going to write some code that returns the second lowest number.

```python
def second_lowest_number(numbers):
    numbers.sort()
    return numbers[1]


assert second_lowest_number([9, -1, 4, 15, 7]) is 4
```

What happens if we now pass in a different data set?


```python
def second_lowest_number(numbers):
    numbers.sort()
    return numbers[1]


assert second_lowest_number([9]) is None
```

### Exercise

Here are a list of numbers

* 35 
* 34 
* 19 
* 28 
* 23

Write some code to tell me what the second **highest** number is, and write a test for it.


## Testing with a framework

We're going to repeat what we did the first time now, except this time using the testing framework that's built into python.

Here's that list of input data again

* 9
* -1
* 4
* 7
* 15

We're now going to write some code that returns the second lowest number.

```python
import unittest


def second_lowest_number(numbers):
    numbers.sort()
    return numbers[1]


class LowestNumberTestCase(unittest.TestCase):
    def test_with_multiple_numbers_it_returns_the_second_lowest(self):
        actual = second_lowest_number([9, -1, 4, 15, 7])
        self.assertEqual(actual, 4)


if __name__ == '__main__':
    unittest.main()
```

What happens if we now pass in a different data set?


```python
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

```

This is a bit nicer formatted than previously, and we can run multiple tests.

### Exercise

Now you have a go

* 17 
* 47 
* 13 
* 19
* 3


Write some code to tell me what the second **highest** number is, and write a test for it.

Next explore some of the other functions of the testing framework

Try checking it returns a number that is in the provided list (hint: try out [assertIn](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn))

### Taking it further...

How might you test code that raises an exception

```python
def second_lowest_number(numbers):
    numbers.sort()
    
    if len(numbers) < 2:
        raise Exception('You need at least 2 numbers!')
    
    return numbers[1]
```

Try it without a unit testing framework and with!
