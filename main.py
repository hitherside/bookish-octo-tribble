"""description:

Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number
and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”. """

"""
3 = "Fizz"
5 = "Buzz"
2 = 2
15 = "FizzBuzz"
11 = 11


"""

def fizzorbuzz(number):
    """Return given number as string, Fizz, Buzz, or FizzBuzz
    :rtype: object
    """
    if number % 3 == 0:
        if number % 5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)

fizz_range = range(1,101)

for index in fizz_range:
    print(fizzorbuzz(index))



