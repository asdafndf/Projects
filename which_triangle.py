#Chose the length of a triangle's 3 sides. The code tells you whether it is equilateral, isosceles, scalene or no triangle at all.
a = 6
b = 6
c = 6
if a==b==c:
    print("equilateral triangle")
elif a==b or a==c or b==c:
    print("isosceles triangle")
elif a+b>c and a+c>b and b+c>a:
    print("scalene triangle")
else:
    print("no such triangle exists")
