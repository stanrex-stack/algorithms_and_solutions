list_1 = ['Hello', 'world', True, False, None, range(10)]
list_2 = [1, 2, 3, 4]
list_3 = list()
# list_4 = list(range(10))
list_5 = ['I', 'love', 'python', 'a', 'lot']
# print(list_4)
# print(1 in list_2)
# print(1 in list_1)
# print([1] + [2] + [3] + [4])
# print(list_2 * 3)
# print(list_2[3])
# print(list_2[0:2])
# print(min(list_2))
print(max(list_5))


# print(list_1[-1])
# print(list_2.index(2))
# print(list_2.count(3))
#
# result = list_2[0]
# for item in list_2:
#     if item < result:
#         result = item
# print(result)


# result = list_5[0]
# for item in list_5:
#     if item < result:
#         result = item
# print(result)
#

# list_1[0] = 'that\'s cool'
# print(list_1)
#
# list_1[1:3] = range(9, 95, 10)
# print(list_1)
#
# list_1[1:3] = 'Hello'
# print(list_1)

# list_1[1:3] = ['Hello']
# print(list_1)
#
# list_2[1:3] = list_1
# print(list_2)
#
# list_3.append(100)
# list_3.append('Hello')
# list_3.append(True)
# print(list_3)


# list_3.append(100)
# list_3.append('Hello')
# list_3.append(True)
# list_3.insert(1, False)
# print(list_3)

# list_3.append(100)
# list_3.append('Hello')
# list_3.append(True)
# list_3.insert(1, False)
# list_3.extend(range(5))
# print(list_3)

#
# list_3.append(100)
# list_3.append('Hello')
# list_3.append(True)
# list_3.insert(1, False)
# list_3.extend(range(5))
# list_3.clear()
# print(list_3)


# list_3.append(100)
# list_3.append('Hello')
# list_3.append(True)
# list_3.insert(1, False)
# list_3.extend(range(5))
# list_3.pop(0)
# print(list_3)


# list_3.append(100)
# list_3.append('Hello')
# list_3.append(True)
# list_3.insert(1, False)
# list_3.extend(range(5))
# print(list_3)
# removed_element = list_3.pop(0)
# removed_element_1 = list_3.pop()
# print(list_3)
# print(removed_element)
# print(removed_element_1)
#
# list_1.reverse()
# print(list_1)
#
# list_5 = [110, 57, 37.6, 277, 100]
# list_5.sort()
# print(list_5)

# string_1 = ''.join(list_5)
# print(string_1)

# string_1 = ' '.join(list_5)
# print(string_1)

# string_1 = ','.join(list_5)
# print(string_1)
#
# string_1 = ', '.join(list_5)
# print(string_1)

# string_1 = 'I love Python'
# list_6 = string_1.split()
# print(list_6)

# string_1 = 'I love Python'
# list_6 = string_1.split('love')
# print(list_6)

# for item in list_2:
#     print(item)
#
# index = 0
# while index < len(list_5):
#     print(list_5[index])
#     index += 1


# list_6 = [110, 57, 37.6, 277, 100]
# sum = 0
# for item in list_6:
#     sum += item
# print(sum)
#
# #
# num = list_6[0]
# for item in list_6:
#     if num < item:
#         num = item
# print(num)
#
# array = [1, 2, 3, 4, 5]
# print(array[0])
# array[1], array[2] = array[2], array[1]
# print(array)


# You are given a list in list_1 variable, write a swap_first_last function to return a new list with
# the first and the last elements of the list swapped.
# list_1 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]

# def swap_fst_lst(list_any):
#     # print(list_any)
#     index = -1
#     for x in list_any:
#      index += 1
#     list_any[0], list_any[index] = list_any[index], list_1[0]
#     return list_any
# print(swap_fst_lst(list_1))

# def rvrs_lst(lst):
#     return lst[::-1]


# list_1 = [1, 2, 3, 4, 5]
#
# def multiply_list(lst):
#     result_2 = 1
#     for x in lst:
#         result_2 *= x
#
#     return result_2
# print(multiply_list(list_1))


#
# list_1 = [10, 5, 4 ,2, 1.37, 100]
#
# def smallest_numbr(lst):
#    return min(lst)
#
# print(smallest_numbr(list_1))



# array = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
# array[0], array[1] = array[1], array[0]
# print(array)
# print(array[1][2])


#
# list_5 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello', 'hello', 1]
#
# def remove_dplcts(lst):
#     lst_1 = []
#     for x in lst:
#         if x not in lst_1:
#             lst_1.append(x)
#     return lst_1
#
# print(list_5)
# print(remove_dplcts(list_5))
#

# You are given a list in list_6 variable.Enter an integer number and save it to number_1 variable,
# write a longer_words_list function which will return the list of words that are longer than number_1
# from a given list of words.
# number_1 = int(input('Please input a number '))
# list_6 = ['On', 'it', 'differed', 'repeated', 'wandered', 'required', 'in.', 'Then', 'girl', 'neat', 'why', 'yet',
#           'knew', 'rose', 'spot.', 'Moreover', 'property', 'we', 'he', 'kindness', 'greatest', 'be', 'oh', 'striking',
#           'laughter.', 'In', 'me', 'he', 'at', 'collecting', 'affronting', 'principles', 'apartments.', 'Has', 'visitor',
#           'law', 'attacks', 'pretend', 'you', 'calling', 'own', 'excited', 'painted.', 'Contented', 'attending',
#           'smallness', 'it', 'oh', 'ye', 'unwilling.', 'Turned', 'favour', 'man', 'two', 'but', 'lovers.', 'Suffer',
#           'should', 'if', 'waited', 'common', 'person', 'little', 'oh.', 'Improved', 'civility', 'graceful', 'few',
#           'smallest', 'screened', 'settling.', 'Likely', 'active', 'her', 'warmly', 'has.']
# def list_of_longer_words(lst, nmbr1):
#     dmmy = []
#     for x in lst:
#         if len(x) > nmbr1:
#             dmmy.append(x)
#     return print(f'The list of words that are larger then {nmbr1} is {dmmy}')
#
# list_of_longer_words(list_6, number_1)

#
# list_7 = [1, 0, 3]
# list_8 = [4, 5, 7]
#
# def one_common_member(lst_1, lst_2):
#     index = 0
#     for x in lst_1:
#         for i in lst_2:
#             if i == x:
#                 index += 1
#     if index != 0:
#         return True
#     else:
#         return False
# print(one_common_member(list_7, list_8))

# list_9 = ['I', ' ', 'l', 'i', 'k', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n']
#
# def list_to_string(lst):
#     str2 = ''.join(lst)
#     return print(str2)
#
# list_to_string(list_9)

# Given a list of numbers in list_10 and a number number_2, write count_items_list function which will count number of
# occurrences of x in the given list
# list_10 = [1, 2, 3, 1, 1, 1, 2, 3, 4]
# number_2 = 3
#
# def count_items_list(array_10, number2):
#    return array_10.count(number2)
#
# print(count_items_list(list_10, number_2))


# list_11 = [1, 2, 3, 1, 1, 1, 2, 3, 4]
#
# def even_items_list(array_11):
#     array_12 = []
#     for x in array_11:
#         if x % 2 == 0:
#             array_12.append(x)
#             array_12.sort()
#
#     return array_12
# print(even_items_list(list_11))

# array = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
# index_1 = 0

# while index_1 < len(array):
#     result_1 = array[index_1]
#     print(result_1)
#     index_1 += 1
#     array_2 = result_1
#     index_2 = 0
#     while index_2 < len(array_2):
#         result_2 = array_2[index_2]
#         print(result_2)
#         index_2 += 1
#
#
# while index_1 < len(array):
#     result_1 = array[index_1]
#     index_1 += 1
#     array_2 = result_1
#     index_2 = 0
#     while index_2 < len(array_2):
#         result_2 = array_2[index_2]
#         print(result_2)
#         index_2 += 1
#
# while index_1 < len(array):
#     result_1 = array[index_1]
#     index_2 = 0
#     while index_2 < len(result_1):
#         print(result_1[index_2])
#         index_2 += 1
#     index_1 += 1

#
# while index_1 < len(array):
#     index_2 = 0
#     while index_2 < len(array[index_1]):
#         print(array[index_1][index_2])
#         index_2 += 1
#     index_1 += 1

# for result in array:
#     for item in result:
#         print(item)
#
# list_6 = [1, 2, 3]
# list_7 = list_6
# list_8 = list_6.copy()

# print(list_6)
# print(list_7)
# print(list_8)
#
# list_7.append(4)
# list_8.append(5)
#
# print(list_7)
# print(list_6)
# print(list_8)
# print(list_6 == list_7)
# print(list_7 == list_8)
# print(list_6 == list_8)
#
# print(list_6 is list_7)
# print(list_7 is list_8)
# print(list_6 is list_8)



# char_1 = 5
# char_2 = char_1
#
# print(char_1)
# print(char_2)
#
# char_1 += 1
# print(char_1)
# print(char_2)