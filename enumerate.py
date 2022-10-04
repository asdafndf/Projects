# How does enumerate() work?

values = ["a", "b", "c"]
for value in values:
    print(value)

values = ["a", "b", "c"]
index = 0
for value in values:
    print(index, value)
    index += 1

values = ["a", "b", "c"]
for index in range(len(values)):
    value = values[index]
    print(index, value)


values = ["a", "b", "c"]
for index, value in enumerate(values):
    print(index, value)

for x, y in [[0,"a"], [1, "b"], [3, "c"]]:
    print(x,y)




