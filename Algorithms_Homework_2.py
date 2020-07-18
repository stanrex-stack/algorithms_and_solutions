# # TODO: HW: Rewrite code, which will return only needed element of Fib sequence
# num = int(input('Please enter a grade of Fibonacci sequence '))
#
# def fiboncacci_calculator(n):
#     fib_1 = 1
#     fib_2 = 1
#     str_1 = input('Would you like to see the whole sequence\n'
#                   'or just the last element ? y/n ')
#     if str_1 == 'y':
#         if n == 0:
#             print(0)
#         if n > 0:
#             print(fib_1)
#         if n > 1:
#             print(fib_2)
#         if n > 2:
#             index = 0
#             while index < n - 2:
#                 fib_1, fib_2 = fib_2, fib_1 + fib_2
#                 index += 1
#                 print(fib_2)
#     elif str_1 != 'y':
#         if n == 0:
#             print(0)
#         elif n == 1 or n == 2:
#             print(1)
#         else:
#             index = 0
#             while index < n - 2:
#                 fib_1, fib_2 = fib_2, fib_1 + fib_2
#                 index += 1
#             print(fib_2)
#
# fiboncacci_calculator(num)
#
# # # TODO Use datetime library to solve problem Seconds to Date
# import datetime
# time_unit = str(datetime.timedelta(seconds=55))
# print(time_unit)
#
#
# a = 145000
# b = 0
# c = 2700
#
#
#
# def remove_last_zeros(elm):
#     if elm == 0:
#         return elm
#     elm = str(elm)
#     len_1 = len(elm)
#     reversed = elm[::-1]
#     for i in reversed:
#         #first I tried to use while instead of if over and it didn't work, why
#         if i == '0':
#             len_1 -= 1
#         else:
#             elm = reversed[::-1]
#             elm = elm[:len_1:]
#             return int(elm)
#             break
# print(remove_last_zeros(a))
# print(remove_last_zeros(b))
# print(remove_last_zeros(c))
#
# a = 18
# b = 245
# c = 333
#
# def continue_summing_up(elm):
#     str1 = str(elm)
#     len1 = len(str1)
#     while len1 > 1:
#         sum = 0
#         for i in str1:
#             sum += int(i)
#         str1 = str(sum)
#         len1 = len(str1)
#
#     return  int(str1)
#
# print(continue_summing_up(a))
# print(continue_summing_up(b))
# print(continue_summing_up(c))
#
#
# # **************************************************************************
#
# def fibonacci(n):
#     fib1 = 1
#     if n < 0:
#         print('Wrong value')
#
#     elif n == 0:
#         print(0)
#     elif n == 1 or n == 2:
#         print(fib1)
#     else:
#         fib2 = 1
#         i = 0
#         while i < n - 2:
#             fib1, fib2 = fib2, fib1 + fib2
#             i = i + 1
#         if i == n - 2:
#             print(fib2)
#
# fibonacci(int(input("Which grade of Fibonnaci sequene would you like to obtain ")))
#
# # *****************************************************************************************
# from datetime import timedelta
#
# result = timedelta(seconds=800)
# print(str(result))
#
#
# #*****************************************************************************
#
# def zeroes_for_heroes(num):
#     if num == 0:
#         return 0
#     while num % 10 == 0:
#         num = num // 10
#     return num
#
# print(zeroes_for_heroes(123500))
#
# # ************************************************************

#
# # *****************************************************************
# # 25, 153, 75
# def sum_of_digits(num):
#     result = 0
#     while num > 0:
#         result += num % 10
#         num = num// 10
#     return result
#
# def sum_of_digits_1(num):
#     while num >= 10:
#        num = sum_of_digits(num)
#     return num
#
# print(sum_of_digits_1(1753))
#
# #***************************************************************************8
#
#
#
# def reversed_string(str):
#     return str[::-1]
#
# def reversed_string_1(str):
#     return ''.join(reversed(str))
#
# def reversed_string_2(str):
#     result = ''
#     index = len(str)
#     while index > 0:
#         result += str[index - 1]
#         index -= 1
#     return result

# **********************************************************

# str1 = input('input a string ')
#
# def palindrome_check(str):
#     str = str.lower()
#     if str == str[::-1]:
#         return True
#     else:
#         return False
# print(palindrome_check(str1))


# ************************************

str1 = input('xuy')
str2 = input('xuy')

def anagram_check(string1, string2):
    string1, string2 = string1.lower(), string2.lower()
    if string1 == string2 or len(string1) != len(string2):
        return False
    for i in string1:
        if string1.count(i) != string2.count(i):
            return False
    return True

# **********************************

str1 = input(' Input a string ')

def str_compressor(string):
    counter = 1
    result = string[0]
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            counter += 1
        else:
            if counter > 1:
                result += str(counter)
            result += string[i + 1]
            counter = 1
    if counter > 1:
        result += str(counter)

        return result


# **************************************************

strink = input('Input a string ')

def unique_char(str1):
    result = ''
    for char in str1:
        if result.count(char) == 0:
            result += char

    return result

# ************************************************

numer = 2
index = 3

result1 = numer ** index

def power(number, index):
    if index == 0:
        return 1
    elif index == 1:
        return number
    else:
        result = power(number, index - 1) * number
        return result


# ******************************

# 6! = 6 * 5 * 4 * 3 * 2 * 1

number = 6

def factorial(num1):
    if num1 == 0:
        return 1
    elif num1 >= 1:
        result = factorial(num1 - 1) * num1
    return result