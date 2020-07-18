# Write a recursive function to count all the elements in a list (divide and rule).
array_1 = [2, 4, 6]

def sum_array(array: list ):
    if array == []:
        return 0
    else:
        array.pop()
        return 1 + sum_array(array)

print(sum_array(array_1))

# Find the biggest number in the list (divide and rule).
array_2 = [4, 2, 6]

def biggest_number(array: list):
    if len(array) == 1:
        return array[0]
    else:
        big_num = array[-1]
        if big_num < array[0]:
            array.pop(-1)
            return biggest_number(array)
        else:
            array.pop(0)
            return biggest_number(array)

print(biggest_number(array_2))




# Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.
#
# You need to consider the following ratings:
#
# Terrible: tip 0%
# Poor: tip 5%
# Good: tip 10%
# Great: tip 15%
# Excellent: tip 20%
# The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:
#
# "Rating not recognised" in Javascript, Python and Ruby...
# ...or null in Java
# ...or -1 in C#
# Because you're a nice person, you always round up the tip, regardless of the service.

# sting1 = input('How was your service ? ')
# cash1 = int(input('How much is a bill ? '))


import math


def count_the_tip(service, cash):
    service.capitalize()
    dict1 = {'Terrible': 0, 'Poor': 5, 'Good': 10, 'Great': 15, 'Excellent': 20}
    if service in dict1:
        return math.ceil((cash * dict1[service]) / 100)
    else:
        return 'Rating not recognised'

print(count_the_tip('Good', 123))



# The purpose of this kata is to work out just how many bottles of duty free whiskey you would have to buy such that the saving over the normal high street price would effectively cover the cost of your holiday.
#
# You will be given the high street price (normPrice), the duty free discount (discount) and the cost of the holiday.
#
# For example, if a bottle cost £10 normally and the discount in duty free was 10%, you would save £1 per bottle. If your holiday cost £500, the answer you should return would be 500.
#
# All inputs will be integers. Please return an integer. Round down.

def duty_calcultaor(normal_price, discount, travel):
    if discount == 100:
        return math.floor(travel / normal_price)
    elif discount >= 100:
        return 'Inflation is not a joking matter'
    elif discount <= 0:
        return math.floor(travel / normal_price)
    else:
        savings = (normal_price * discount) / 100
        return math.floor(travel / savings)

print(duty_calcultaor(10, 10, 500))