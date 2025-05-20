print("welcome to calculator")

while 1:
    number1 = int(input("please Enter the first number :"))
    number2 = int(input("please Enter ther last number :"))
    opration = input("please enter / or +or - or * :")
    if opration == "/":
        print(number1 / number2)
    elif opration == "+":
        print(number1 + number2)
    elif opration == "-":
        print(number1 - number2)
    elif opration == "*":
        print(number1 * number2)
    cn = input("if you want to continue y/n :")
    if cn == "n":
        break
