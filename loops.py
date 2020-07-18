# FOR LOOPS EXERCISES

# Enter your name, save it in name variable and create function print_name_three_times which returns
# value that is equal to your name three times
#
# name_1 = 'Stanisaw'
# def print_name_three_times(nam):
#     return 3 * (nam)
#
# result = print_name_three_times(name_1)
# print(result)

# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then display their name that number of times. Each time add your name to result
# variable

# name_2 = input('Stanislaw ')
# number_1 = int(input('Number'))
#
# def print_name_number_times(number, name):
#     return number * name
#
# print(print_name_number_times(number_1, name_2))

# string_1 = 'I love Python'
#
# for x in string_1:
#     print(x)
#
# number_1 = range(10)
# for y in number_1:
#     print(y)

# number_1 = range(10)
#
# result = 0
#
# for y in number_1:
#     result += y
# print(result)
#
# string_1 = '1234567'
# char_2 = 0
# for char in string_1:
#     char_2 += int(char)
#
# print(char_2)
#
# string_1 = '1234567'
#
# result = 0
#
# for char in string_1:
#     result += int(char)
#
# print(result)

# string_1 = 'I love Python'
#
# for char in string_1:
#     if char == 'P' or char == 'p':
#         print(True)
#     else:
#         print(False)

# string_1 = 'I love Python'
# flag = False
#
# for char in string_1:
#     if char == 'P' or char == 'p':
#         flag = True
#
# print(flag)


# numbers = range(10, 85)
#
# for num in numbers:
#     if num % 5 == 0:
#         print(num)

# char = '\U0001f929'
#
# numbers = range(5)
#
# for num in numbers:
#     print(char * num)
#
numbers = range(1, 10)

# print(numbers[0])

# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1
# string_1 = '123456789'
# numbers = range(10)
# result = 0
# for num in numbers:
#    result += num
#
# print(result)
#    print(numbers[index])


# numbers = range(1, 10)
#
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1

#
# numbers = range(1, 10)
#
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1

# FOR LOOPS EXERCISES

# Enter your name, save it in name variable and create function print_name_three_times which returns
# value that is equal to your name three times
#
#
# string_1 = input('Please enter your name ')
#
# def pr_3_t(str):
#     return str * 3
# print(pr_3_t(string_1))

# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then display their name that number of times. Each time add your name to result
# variable



# string_1 = input('Please enter your name ')
# string_2 = int(input('Please enter a number '))
#
# def pr_3_t(str, num):
#      return str * num
#
# print(pr_3_t(string_1, string_2))

# Enter a random string, which includes only digits. Write function sum_digits which find a sum of digits in this string

# string_number_1 = '123456789'
# result = 0
#
# def sumofnumb(num, char):
#     for x in num:
#          char += int(x)
#     return char
# print(sumofnumb(string_number_1, result))


# # Create function which sums up all even numbers between 2 and 100 (include 100)
#
# number_1 = range(2, 100)
# sum = 0
# def sumofevens(rng, num):
#     for x in rng:
#         if x % 2 == 0:
#          num += int(x)
#
#     return num
# print(sumofevens(number_1, sum))

# WHYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY does it only return '2'
#
# number_1 = range(2, 100)
# result = 0
#
# for x in number_1:
#     if x % 2 == 0:
#         result += x
# print(result)

# # This one does return sum

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write function counter, which will count how many times your character is included in your string



# string_2 = input('Write a phrase ')
# string_1 = input('Choose the symbol you are trying to find ? ')
# count = 0
# for x in string_2:
#     if x == string_1.lower() or x == string_1.upper():
#         count += 1
#
# print(f'There are {count} symbols of {string_1} in your text')


# Enter a random number and save it in variable number_1. Then create a function number_multiplication
# that will multiply all the digits together and return the result.

# number_1 = input('Enter a number ')
#
# count = 1
# for x in number_1:
#    count *= int(x)
# print(count)

# Enter a random number and save it in variable number_2. Then create function number_reverse which will return
# a number with digits of number_1 in reverse order
#
# string_1 = input('Enter a number ')
# print(string_1[::-1])

