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


stringg = input('Input a strink ')
charr = input('Input the chunk you want replace in it ')
charr1 = input('What do you want to replace it to')

def one_char_replacer(str1, char1, char2):
    length_of_char_to_change = len(char1)
    finder = str1.find(char1)

    while finder > 0:
        str1 = string1[0:finder] + char2 + string1[finder + length_of_char_to_change:]
        finder = str1.find(char1)
    return str1


    # for i in str1:
    #     if i == char1:
    #         i = char2
    #     str2 += i
    # return str2

print(one_char_replacer(stringg, charr, charr1))
# I do not know how to solve this if there is more than one character to change
# def more_char_replacer(str1, char1, char2):


# ************************************************************
# * TODO: Write a function for decompressing string “a4b3c2d”

string1 = 'a4b3c2d'
string2 = 'h5s7'

def decompressor(str1):
    i = range(2, 10)
    list1 = []
    for t in i:
        list1.append(str(t))
    # this will create a list of numbers that contain strings i need for the
    # comparison
    result = ''

    for i in range(len(str1) - 1):
        if str1[i] not in list1:
            result += str1[i]
        elif str1[i] in list1:
            b = str1[i - 1]
            i = int(str1[i]) - 1
            b *= i

            result += b
    return result

print(decompressor(string1))

# this function is not perfect because it is not working with numbers of more than one digit

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


number = 4

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
#  I had to Google this one

def fibonacci_recursion(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci_recursion(n-1) + fibonacci_recursion(n-2))

n = int(input("What grade do you want to count to ? "))

print("Fibonacci sequence using Recursion :")
for i in range(n):
    print(fibonacci_recursion(i))