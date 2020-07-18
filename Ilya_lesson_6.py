# def countries_and_cities(data, needed_cities):
#     dictionary = {}
#     for item in data:
#         index = 1
#         while index < len(item):
#             dictionary[item[index]]  = item[0]
#             index += 1
#     result = []
#     for needed_city in needed_cities:
#         if needed_city in dictionary:
#             result.append(dictionary[needed_city])
#         else:
#             result.append(f'{needed_city} is not in our list')
#     return result
#
# print(countries_and_cities([
#     ['USA', 'Dallas', 'Washington', 'Los Angeles', 'San Fransico'],
#     ['Canada', 'Ottawa', 'Vancouve', 'Montreal']
# ], ['Montreal', 'Washington', 'Dallas', 'Omsk'])
# )
#
#
#
# def assign_jobs(keys, values):
#     result = {}
#     index = 0
#     while index < len(keys):
#         if index < len(values):
#             result[keys[index]] = values[index]
#         else:
#             result[keys[index]] = None
#
#         index += 1
#     return result
#
# array = [2, 4, 6]
# array_1 = [2, 4, 6]
# def sum_array(array: list ):
#     if len(array) == 0:
#         return 0
#     else:
#         value = array.pop()
#         return value + sum_array(array)
#
# print(sum_array(array))
#
# def sum_array_1(array: list ):
#     if len(array) == 1:
#         return array[0]
#     else:
#         value = array[0:1]
#         array = array[1:]
#         return value[0] + sum_array(array)
#
# print(sum_array_1(array_1))


def split_farms(heigth, width):
    if heigth > width:
        parts = heigth % width
        if parts == 0:
            return tuple([width, width])
        else:
            heigth = parts
            return split_farms(heigth, width)

    else:
        parts = width % heigth
        if parts == 0:
            return tuple([heigth, heigth])
        else:
            width = parts
            return split_farms(heigth, width)

print(split_farms(10, 8))