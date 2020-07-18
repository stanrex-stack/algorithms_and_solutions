# input_for_first_function = int(input('Which row would you like to add up ?'))

def sum_of_pyramid(number_1):
    return pow(number_1, 3)

# When given a list, the program should return
# a list of all the elements that are below
# the arithmetical mean of the original list.
# The arithmetical mean is the sum of all
# elements divided by the number of elements.

input_for_second_function = [1, 2, 3, 4, 5]

# def below_the_mean(list_var):
#     list_2 = []
#     arithmetical_mean = sum(list_var) / len(list_var)
#     for i in list_var:
#         if i < arithmetical_mean:
#             list_2.append(i)
#
#     return list_2


def below_the_mean_1(list_var):
    return [x for x in list_var if x < sum(list_var) / len(list_var)]

print(below_the_mean_1(input_for_second_function))

input_for_third_function = [76, 100, 3, 4, 5]

# def return_two_smalest(list_var):
#     list_var.sort()
#     list_var_2 = []
#     for i in range(2):
#         list_var_2.append(list_var.pop(0))
#     return list_var_2
#
# print(return_two_smalest(input_for_third_function))

def return_two_smallest_1(list_var):
    list_var.sort()
    return [[list_var.pop(0) for i in range(2)]]

print(return_two_smallest_1(input_for_third_function))