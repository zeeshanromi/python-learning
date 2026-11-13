a = float(input("enter 1at number: "))
b = float(input("enter 2nd number: "))
op = (input("Enter operator: "))

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "**":
    print(a**b)
elif op == "%":
    print(a % b)
elif op == "/":
    print(a/b)
elif op == "//":
    print(a//b)
else:
    print("error")
input("\nPress Enter to exit...")
