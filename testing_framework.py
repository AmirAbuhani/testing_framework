# Amir Abu Hani
from mathematical import condition
from list_nested_list import value_list_nested_list
from key_dict_nested_dict import key_in_nested_dictionary
from value_in_nested_dictionary import value_in_nested_dictionary

players_team_nested = {
    "real madrid": {"vini": "brazilian", "rodrygo": "brazilian", "modric": "croatian"},
    "barcelona": {"gavi": "spanish", "pedri": "spanish"},
    "liverpool": {"salah": "egyptian", "alonso": "spanish"}
}

players = {"real madrid": "vini", "barcelona": "pedri"}

my_nested_list = [[1, 2, 3], [4, 6], 7]
my_list = [8, 9, 10]

################################################ Tests ##############################################

# To check the mathematical assertion module
isbigger = condition(9, 10)
# print(isbigger)

# To check if value is in list or nested list
isExistsInList = value_list_nested_list([1,2,3], my_nested_list)
print(isExistsInList)

# To check if key in dictionary or nested dictionary
isExistsKey = key_in_nested_dictionary("real madrid", players)
# print(isExistsKey)

# To check if value in dictionary or nested dictionary
isExistsValue = value_in_nested_dictionary("pedri", players)
# print(isExistsValue)
