# ex1
"""A recipe you are reading states how many grams you need for the ingredient.
Unfortunately, your store only sells items in ounces.
Create a function to convert grams to ounces. ounces = 28.3495231 * grams"""


def grams_to_ounces(grams):
    return round(grams * 28.3495231, 2)

x = float(input("Enter the value:"))
print(x , "grams are equal to", grams_to_ounces(x) , "ounces")

# ex2
"""
Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F - 32)
"""


def to_celcius(temp):
    return round((5 / 9) * (temp - 32), 2)


temperature = float(input("Enter the value: "))
print(temperature, "degrees Fahrenheit is equal to", to_celcius(temperature), "degrees Celcius")

# ex3
"""
Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
"""

def solve(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if (2 * c) + (4 * r) == numlegs:
            return c, r
    return None


numheads, numlegs = map(int, input().split())
result = solve(numheads, numlegs)
if result is not None:
    chickens, rabbits = result
    print("Number of chickens:", chickens)
    print("Number of rabbits:", rabbits)
else:
    print("No solution for this case")

# ex4
"""
You are given list of numbers separated by spaces. 
Write a function filter_prime which will take 
list of numbers as an agrument and returns only prime numbers from the list."""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

arr = (input("Enter the elements of list:"))
numbers = arr.split()
result = [x for x in numbers if is_prime(int(x)) ]
print("Prime numbers are:", result)

# ex5
"""
Write a function that accepts string from user and print all permutations of that string.
"""

from itertools import permutations

def print_permutations(input_string):
    permuted_strings = permutations(input_string)
    for permuted_string in permuted_strings:
        print(''.join(permuted_string))


input_string = input("Enter the string: ")
print_permutations(input_string)

# ex6
"""
Write a function that accepts string from user, return a sentence with the words reversed. 
We are ready -> ready are We
"""

def text_reversed(text):
    words = text.split()
    i = len(words) - 1
    while i >= 0:
        print(words[i], end=' ')
        i -= 1

text = input('Enter text: ')
text_reversed(text)

# ex7
"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""

def has_33(nums_list):
    for i in range(len(nums_list) - 1):
        if nums_list[i] == '3' and nums_list[i + 1] == '3':
            return True
    return False

nums = input("Enter a list of numbers separated by space: ")
nums_list = nums.split()
print(has_33(nums_list))
# ex8
"""
Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""

def spy(nums_list):
    for i in range(len(nums_list) - 1):
        if nums_list[i] == '0' and nums_list[i + 1] == '0' and nums_list[i+2]=='7':
            return True
    return False

nums = input("Enter a list of numbers separated by space: ")
nums_list = nums.split()
print(spy(nums_list))
# ex9
"""
Write a function that computes the volume of a sphere given its radius.
"""
import math
def volume_of_sphere(radius):
    return round((4/3) * math.pi * radius**3, 2)

r = float(input("Enter a value of radius: "))
print("volume of a sphere with radius", r ,"is:",volume_of_sphere(r))
# ex10
"""
Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set.
"""


def unique(num_list):
    arr = []
    for i in num_list:
        if i not in arr:
            arr.append(i)
    return arr

nums = input("Enter the nums:")
num_list = nums.split()
res = unique(num_list)
print(res)
# ex11
"""
Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same 
backward as forward, e.g., madam
"""

def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]


phrase = input("Enter a phrase: ")
if is_palindrome(phrase):
    print("The phrase is a palindrome.")
else:
    print("The phrase is not a palindrome.")
# ex12
"""
Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******

"""

def histogram(n_list):
    for num in n_list:
        print(num * '*')

nums = input("Enter the nums separated by space: ")
n_list = [int(elem) for elem in nums.split()]
histogram(n_list)
# ex13
"""
Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""
import random


def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break


# Проверяем, является ли текущий модуль основным
if __name__ == "__main__":
    # Если текущий модуль основной, то вызываем функцию guess_the_number()
    guess_the_number()
# ex14
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0
guess_the_number()