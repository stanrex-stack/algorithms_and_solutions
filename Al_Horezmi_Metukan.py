# Write a Python function, which will count how many times a character (substring) is included in a string. DON’T USE METHOD COUNT


string = input('Input a string ')
char = input('What charachter are you looking for  ? ')

def count_string_char(str1, char1):
    char2 = char1.lower()
    str2 = str1.lower()
    counter = 0
    for index in range(len(str2)):
        if str2[index:(index+len(char2))] == char2:
            counter += 1
    if counter == 0:
        return f'No {char1} in {str1}'
    else:
        return counter

print(count_string_char(string, char))

# Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings.
# DON’T USE METHOD REPLACE


str1 = input('Input a strink ')
char1 = input('Input the chunk you want replace in it ')
char2 = input('What do you want to replace it to ')

def one_char_replacer(given_string, char_to_replace, char_replacer):
    length_of_char_to_change = len(char_to_replace)
    finder = given_string.find(char_to_replace)

    while finder > 0:
        given_string = given_string[0:finder] + char_replacer + given_string[finder + length_of_char_to_change:]
        finder = given_string.find(char_to_replace)
    return given_string

print(one_char_replacer(str1, char1, char2))


# * TODO: Write a function for decompressing string “a4b3c2d”

def get_first_number(the_function_string):
    numbers_range = range(10)
    list_of_all_numbers = []
    for one_number in numbers_range:
        list_of_all_numbers.append(str(one_number))
    new_string =''
    for string_index in range(len(the_function_string)):
        if the_function_string[string_index] not in list_of_all_numbers:
           new_string += the_function_string[string_index]

        elif the_function_string[string_index] in list_of_all_numbers:


            if the_function_string[string_index - 1] not in list_of_all_numbers:
                char_to_be_multiplied = the_function_string[string_index - 1]
                empty_number_1 = ''

                def get_a_full_number(an_initial_string, an_initial_index, an_initial_list_of_numbers):
                    empty_number_2 = ''
                    empty_number_2 += an_initial_string[an_initial_index]
                    if (an_initial_index + 1) != len(an_initial_string):
                        an_initial_index += 1
                        if an_initial_string[an_initial_index] in an_initial_list_of_numbers:
                            result_of_reccursion = get_a_full_number(an_initial_string, an_initial_index,
                                                                     an_initial_list_of_numbers)
                            empty_number_2 += result_of_reccursion
                    return empty_number_2

                result_of_function = get_a_full_number(the_function_string, string_index, list_of_all_numbers)

                empty_number_1 += result_of_function

                empty_number_1 = (int(empty_number_1) - 1)
                char_to_be_multiplied *= empty_number_1
                new_string += char_to_be_multiplied

    return new_string


# factorial recurssion


def factorial(num1):
    if num1 == 0:
        return 1
    elif num1 < 0:
        return 'ooops'
    elif num1 >= 1:
        result = factorial(num1 - 1) * num1
    return result

# digital root recursion

def digital_root(num1):
    result = 0
    while num1 > 0:
        result += num1 % 10
        num1 = num1 // 10

    while result > 10:
        result = digital_root(result)

    return num1

#  fibbonaci recursion


def fibonacci_recursion(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci_recursion(n-1) + fibonacci_recursion(n-2))

n = int(input("What grade do you want to count to ? "))

print("Fibonacci sequence using Recursion :")
for i in range(n):
    print(fibonacci_recursion(i))



# Extra 3-4 Katas


# Given a string, capitalize the letters that occupy
# even indexes and odd indexes separately,
# and return as shown below. Index 0 will be considered even.
#
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF'].
# See test cases for more examples.
#
# The input will be a lowercase string with no spaces.
test_string = 'abcdef'

def capitalizer(string_to_capitalize):
    new_string_1 = ''
    new_string_2 = ''
    list_to_return = []

    for index in range(len(string_to_capitalize)):
        if (index + 1) % 2 != 0:
            new_string_1 += string_to_capitalize[index].upper()
            new_string_2 += string_to_capitalize[index].lower()
        else:
            new_string_1 += string_to_capitalize[index].lower()
            new_string_2 += string_to_capitalize[index].upper()
    list_to_return.append(new_string_1)
    list_to_return.append(new_string_2)
    return list_to_return

print(capitalizer(test_string))

# Given a positive integer n, calculate the following sum:
#
# n + n/2 + n/4 + n/8 + ...
# All elements of the sum are the results of integer division.
#
# Example
# 25  =>  25 + 12 + 6 + 3 + 1 = 47
# ALGORITHMS
import math


def devider(number_to_sum):
    number_to_divide = number_to_sum
    while number_to_divide > 1:
        number_to_divide = math.floor(number_to_divide / 2)

        number_to_sum += number_to_divide

    return number_to_sum


print(devider(25))


# Say hello!
#
# Write a function to greet a person.
#
# Function will take name as input and greet the person
# by saying hello. Return null/nil/None if input is empty string or null/nil/None.
#
# Example:
#
# greet("Niks") --> "hello Niks!"
# greet("")    --> None # Return None if input is empty string
# greet(None)  --> None # Return None if input is None

def greeter(received_name):
    if received_name != None:
        if len(received_name) > 0:
            return 'hello '+ received_name
        else:
            return None
    else:
        return None
print(greeter(''))

#         The Amazon riddle from Automation Homework

def return_ilsl_non_uni(str1):
    str2 = str1.lower()
    counter = 0
    for i in str2:
        if str2.count(i) < 2:

           index = str2.find(i)
           counter += 1
           return str1[index]

    if counter == 0:
        return ''



#     The Kata from Automation homework



# Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.
#
# Your fellow coders have bought you several drinks tonight in the form of a string. Return a string suggesting how many glasses of water you should drink to not be hungover.
#
# Examples
# "1 beer"  =>  "1 glass of water"
# "1 shot, 5 beers and 1 glass of wine"  =>  "7 glasses of water"
# Notes
# To keep the things simple, we'll consider that anything with a number in front of it is a drink: "1 bear" => "1 glass of water" or "1 chainsaw and 2 pools" => "3 glasses of water"
# The number in front of each drink lies in range [1; 9]

def return_da_water(str1):
    numbers_range = range(1, 10)
    list_of_all_numbers = []
    for one_number in numbers_range:
        list_of_all_numbers.append(str(one_number))
    print(list_of_all_numbers)

    counter = 1
    for i in str1:
        if i in list_of_all_numbers:
            counter += int(i)
    if counter == 1:
        return '1 glass of water'
    else:
        return f'{counter} glasses of water'



