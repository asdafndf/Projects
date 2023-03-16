# Sort the dictionary keys in alphabetical order
my_dict = {
    "z" : 1,
    "d" : 2,
    "e" : 3
}

sorted_dict = {key:value for key, value in sorted(my_dict.items())}

print(sorted_dict) # {'a': 1, 'e': 2, 'z': 3}


