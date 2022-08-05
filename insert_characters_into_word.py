# How to insert extra characters between the letters of a word

#1
string = "Hello"
extra = "***"
new_string = [x + extra for x in string]
result = ""
for x in new_string:
    result += x

print(result[:-len(extra)])

#2
new_string = [x for x in string]
new_new_string = "***".join(new_string)

print(new_new_string)