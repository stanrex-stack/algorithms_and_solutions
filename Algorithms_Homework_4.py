# Enter a string of words separated by spaces. Find the longest word.

users_string = input('Please input a string of words ')
string_of_words = 'Python I love  python a lot'
string_of_words_1 = 'Jack Wick Antonio Montana'
string_of_words_2 = 'I cant explain how much I love donuts'

def find_the_longest_word(given_string):
    given_string += ' '
    word_separator = ''
    list_of_words = []
    for i in given_string:
        if i != ' ':
            word_separator += i
        else:
            list_of_words.append(word_separator)
            word_separator = ''
    largest_word = ''
    list_of_largest_words = [' ']
    for i in list_of_words:
        if len(i) > len(largest_word):
            largest_word = i
        elif len(i) == len(largest_word):
            list_of_largest_words.append(i)
            list_of_largest_words.append(largest_word)
    if len(list_of_largest_words[-1]) == len(largest_word):
        list_of_largest_words.pop(0)
        while len(list_of_largest_words[0]) < len(list_of_largest_words[-1]):
            list_of_largest_words.pop(0)
        return f'There are multiple longest words in the string {list_of_largest_words}'
    else:
        return largest_word



print(find_the_longest_word(users_string))


irregular_string_of_words = '   Python '
users_irregular_string_of_words = input('Please input an irregular string of words ')

def words_regulizer(given_string):
    for i in range(len(given_string)):
        given_string = given_string.replace('  ', ' ')

    if given_string[0] == ' ':
        given_string = given_string[1:]
    if given_string[-1] == ' ':
        given_string = given_string[:len(given_string) - 1]
    return given_string

print(words_regulizer(irregular_string_of_words))


# codewars.com (3-4 problems)

# You are given an unsorted array
# containing all the integers
# from 0 to 100 inclusively.
# However, one number is missing.
# Write a function to find and return
# this number.
# What are the time and space
# complexities of
# your solution?
def missing_no(nums):
    allnums = list(range(0, 101))
    return sum(allnums) - sum(nums)

# Given an integer as input,
# can you round it to the next
# (meaning, "higher") 5?

def round_to_next5(n):
    while n % 5 != 0:
        n += 1
    return n


# Given a string and an array of integers
# representing indices,capitalize all
# letters at the given indices.

# For example:

# capitalize("abcdef",[1,2,5]) = "aBCdeF"
# capitalize("abcdef",[1,2,5,100]) = "aBCdeF".
# There is no index 100.
# The input will be a lowercase string with
# no spaces and an array of digits.

def capitalize(s,ind):
    for i in ind:
        s = s[:i] + s[i:].capitalize()
    return s