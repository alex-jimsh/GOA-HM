#1
def add_five(number):
    return number + 5
#2
def multiply_two_integers(a, b):
    return a * b
#3
def string_length(s):
    return len(s)
#4
def list_of_lengths(strings):
    return [len(s) for s in strings]
#5
def is_palindrome(s):
    return s == s[::-1]
#6
def longest_string(strings):
    return max(strings, key=len)
#7
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
#8
def sum_of_maxima(list1, list2):
    return max(list1) + max(list2)
#9
def difference_of_minima(list1, list2):
    return min(list1) - min(list2)
#10
def range_of_list(numbers):
    return max(numbers) - min(numbers)
#11
def sum_of_list(numbers):
    return sum(numbers)

#12
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

#13
def square_list(numbers):
    return [x ** 2 for x in numbers]

#14
def reverse_string(s):
    return s[::-1]

#15
def is_even(number):
    return number % 2 == 0

#16
def longest_string(strings):
    return max(strings, key=len)

#17
def smallest_number(numbers):
    return min(numbers)

#18
import math

def gcd(a, b):
    return math.gcd(a, b)

#19
def to_uppercase(s):
    return s.upper()

#20
def average(numbers):
    return sum(numbers) / len(numbers)

