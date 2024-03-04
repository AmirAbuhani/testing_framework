# Amir Abu Hani
def value_in_nested_dictionary(tested_value, value_compare_to):
    for value in value_compare_to.values():
        if value == tested_value:
            return True
    for value in value_compare_to.values():
        if isinstance(value, dict):
            if value_in_nested_dictionary(tested_value, value):
                return True
    return False

