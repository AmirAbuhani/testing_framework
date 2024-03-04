# Amir Abu Hani
def key_in_nested_dictionary(tested_value, value_compare_to):
    if tested_value in value_compare_to:
        return True
    for key in value_compare_to:
        if isinstance(key, dict):
            if key_in_nested_dictionary(tested_value, key):
                return True
    return False

