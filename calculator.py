# Very basic calculator. Have fun!

num1 = float(input("First number: "))
op = input("Operator (+-*/): ")
num2 = float(input("Second number: "))

if op == "+":
    print(num1 + num2)
elif op == "*":
    print(num1 * num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
else:
    print("Not valid operator, sorry")