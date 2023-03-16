# This is like the Counter from collections
txt = """But soft what light through yonder window breaks
It is the east and Juliet is the sun 
Arise fair sun and kill the envious moon
Who is already sick and pale with grief"""

txt_list = txt.split()

counts = {}
"""
for word in txt_list:
    if word in counts.keys():
        counts[word] += 1
    else:
        counts[word] = 1
"""
for word in txt_list:
    counts[word] = counts.get(word, 0) + 1 # Above 4 lines condensed

# First way to sort the counts
max_value = max(counts.values())
new_counts = {}

while max_value > 0:
    for key, value in counts.items():
        if value == max_value:
            new_counts[key] = value
    max_value -= 1

# Second way to sort the counts
sorted_tuple_list = sorted([(value, key) for key, value in counts.items()], reverse=True)

sorted_counts = {key:value for value, key in sorted_tuple_list}


