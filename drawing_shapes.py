# Drawing shapes

lst = [1,1,1,1,5]
for x in lst:
    line = ""
    for y in range(x):
        line += "x"
    print(line)

lst = [1,1,1,1,5]
for x in lst:
    print(x*"x")

count = 0
stars = "*"
while count < 5:
    print(stars)
    count += 1
    stars += "*"