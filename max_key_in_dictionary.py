# Return the key(s) in a dictionary whose value is the maximal among values
def max_key(dictionary):
    """Return the key(s) in a dictionary whose value is the maximal among values"""
    max_value = max(dictionary.values())
    return tuple(key for key, value in dictionary.items() if value == max_value)


