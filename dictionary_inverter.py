# %% """Invert a dictionary: keys become values and vica-versa"""
def dict_inverter(dictionary):
    """Invert a dictionary: keys become values and vica-versa"""
    return {value:key for key, value in dictionary.items()}


