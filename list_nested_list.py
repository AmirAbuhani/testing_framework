# Amir Abu Hani
def value_list_nested_list(tested_value, value_compare_to):
    if tested_value in value_compare_to:
        return True
    for item in value_compare_to:
        if isinstance(item, list):
            if value_list_nested_list(tested_value, item):
                return True
    return False
