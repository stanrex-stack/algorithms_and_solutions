# Enter a country and save it to variable your_choice_country. Write find_index_by_value function which will check
# if the tuple countries contains a country of your choice. If your_choice_country is in the tuple, return its
# index, otherwise return a -1 value

# tuple = ('USA', 'Canada', 'United Kingdom', 'Mexico', 'Brazil', 'Argentina', 'Chili', 'South Africa', 'Egypt',
#              'Morocco', 'India', 'China', 'Ukraine', 'Spain', 'France', 'Russia')
# value_1 = input('Please choose a country ')
#
#
# def find_index_by_value(int, tuple1):
#     index = 0
#     result_1 = -1
#     while index < len(tuple1):
#         if int == tuple1[index]:
#             result_1 = index
#
#         index += 1
#     return result_1
# print(find_index_by_value(value_1, tuple))

# Change the previous exercise. Enter a random number and save it to variable your_choice_number. Write
# find_value_by_index function which will check if the tuple countries contains a country with this index.
# If there is a value with this index your_choice_number in the tuple, return this value,
# otherwise return a 'No such index' text
# tuple = ('USA', 'Canada', 'United Kingdom', 'Mexico', 'Brazil', 'Argentina', 'Chili', 'South Africa', 'Egypt',
#              'Morocco', 'India', 'China', 'Ukraine', 'Spain', 'France', 'Russia')
# your_choice_number = int(input('Please enter an index number '))
#
# def find_value_by_index(index, tuple1):
#     if index < len(tuple1):
#         print(tuple1[index])
#     else:
#         print('No such index')
# find_value_by_index(your_choice_number, tuple)


# Enter a pair of values in variables new_team_name, new_team_city. Then write add_your_own_team function
# to add them to nhl_hockey_teams dictionary, where the name will be the key.

team = 'Roberts'
city = 'South_Side'

hockey = {
    "Canadians": "Montreal",
    "Maple Leafs": "Toronto",
    "Red Wings": "Detroit",
    "Bruins": "Boston",
    "Blackhawks": "Chicago",
    "Oilers": "Edmonton",
    "Penguins": "Pittsburgh",
    "Islanders": "New York",
    "Rangers": "New York",
    "Devils": "New Jersey",
    "Avalanche": "Colorado",
    "Kings": "Los Angeles",
    "Flyers": "Philadelphia",
    "Ducks": "Anaheim",
    "Flames": "Calgary",
    "Hurricanes": "Carolina",
    "Stars": "Dallas",
    "Blues": "St. Louis",
    "Lightning": "Tampa Bay",
    "Capitals": "Washington"

}

# def stan_is_trying(team1, city1, hockey1):
#     hockey1[team1] = city1
#     return hockey1
#
# print(stan_is_trying(team, city, hockey))

#
# def ilya_was_coding(team2, city2, hockey2):
#     hockey2.update({team2: city2})
#     return hockey2

# print(ilya_was_coding(team, city, hockey))





# def add_your_own_team(dict_name, team_name, team_city):
#     list_items = list(dict_name.items())
#     list_items.append(team_name, team_city)
#     pass

# Create two dictionaries in dict_1, dict_2 variables. Write a join_dicts function to concatenate the following
# dictionaries to create a new one.
#
# dict_1 = dict(one=1, two=2, three=3, number_1=100)
# dict_2 = dict(eins=11, zwei=22, drei=3, hundert=110)
#
# def join_dicts(dict1, dict2):
#     dict3 = {}
#     dict3.update(dict1)
#     dict3.update(dict2)
#     return dict3
# print(join_dicts(dict_1, dict_2))



# # Enter a random number and save it to number_1 variable. Then write create_numbers_dict function to generate
# a dictionary that contains items with keys from 1 to number_1 and values in format "x": "x**2".

number_1 = 5

# def create_numbers_dict(number1):
#     number_1 = number1 ** number1
#     number_2 = str(number1)
#     dict1 = dict()
#     dict1[number_2] = number_1
#     return dict1
#
# print(create_numbers_dict(number_1))

# Write sum_up_hockey_cups functions to sum all values in a dictionary dict_3.

dict_3 = {
    "Montreal Canadiens": 24,
    "Toronto Maple Leafs": 13,
    "Detroit Red Wings": 11,
    "Boston Bruins": 6,
    "Chicago Blackhawks": 6,
    "Edmonton Oilers": 5,
    "Pittsburgh Penguins": 5,
    "New York Islanders": 4,
    "New York Rangers": 4,
    "New Jersey Devils": 3,
    "Colorado Avalanche": 2,
    "Los Angeles Kings": 2,
    "Philadelphia Flyers": 2,
    "Anaheim Ducks": 1,
    "Calgary Flames": 1,
    "Carolina Hurricanes": 1,
    "Dallas Stars": 1,
    "St. Louis Blues": 1,
    "Tampa Bay Lightning": 1,
    "Washington Capitals": 1
}

# def sum_up_hockey_cups(teams_dict):
#     result_1 = 0
#     for x in teams_dict.values():
#
#         result_1 += x
#
#     return result_1
#
# print(sum_up_hockey_cups(dict_3))
# Write remove_item_by_key function to remove a key True from dict_4 dictionary.

dict_4 = {
    "a": 231,
    "b": 'hello',
    True: False,
    42: 'answer'
}

# def remove_item_by_key(dict1):
#     index = 0
#     for x in dict1.keys():
#         if x == True:
#             result1 = 1
#     if index == 1:
#         dict1.pop(True)
#     return dict1
#
# print(remove_item_by_key(dict_4))
# Write find_min_max function to get the maximum and minimum value in dict_5 dictionary. Return the answer in format
# {
#     "min": 111,
#     "max": 222
# }

dict_5 = {
    "Cyprus": 1207359,
    "Czechia": 10708981,
    "Democratic Republic of the Congo": 89561403,
    "Denmark": 5792202,
    "Djibouti": 988000,
    "Dominica": 71986,
    "Dominican Republic": 10847910,
    "Ecuador": 17643054,
    "Egypt": 102334404,
    "El Salvador": 6486205,
    "Equatorial Guinea": 1402985,
    "Eritrea": 3546421,
    "Estonia": 1326535,
    "Eswatini": 1160164,
    "Ethiopia": 114963588,
    "Fiji": 896445,
}
#
# def find_min_max(dict1):
#     for x in dict1.values():
#         lastobject = x
#         lastobject1 = lastobject
#     for x in dict1.values():
#         if lastobject < x:
#             lastobject = x
#         elif lastobject1 > x:
#             lastobject1 = x
#     dict2 = {}
#     dict2['min'] = lastobject1
#     dict2['max'] = lastobject
#     return dict2
# print(find_min_max(dict_5))
# Write remove_duplicates functions to remove duplicates from dictionary dict_6.

dict_6 = {
    "Lessie": "collie",
    "Marlie": "labrador",
    "Spike": "boxer",
    "Buddy": "labrador",
    "Milo": "labrador",
    "Archie": "corgi",
    "Tobby": "pit bull",
    "Jack": "poodle",
    "Lucy": "german shepherd",
    "Bailey": "labrador"
}

def remove_duplicates(dict1):
    dict2 = {}
    for key, value in dict1.items():
        if value not in dict2.values():
            dict2[key] = value
    return dict2

print(remove_duplicates(dict_6))