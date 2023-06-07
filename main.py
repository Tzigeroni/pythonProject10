def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def  divide(a, b):
    return a / b

print("Welcome to the calculator")

while True:
    print("Please choose an operator: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Please choose (1-4) ")
    if choice == "5":
        print("Exiting Calculator ")
        break

    num1 = float(input("Please choose First number: "))
    num2 = float(input("Please choose second number: "))

    if choice == "1":
        result = add(num1, num2)
        print("Result is: ", result)
    elif choice == "2":
        result = subtract(num1, num2)
        print("Result is ", result)
    elif choice == "3":
        result = multiply(num1, num2)
        print("Result is ", result)
    elif choice == "4":
        if num1 != 0 and num2 != 0:
            print("Error, Cant divide by Zero")
        else:
            result = divide(num1, num2)
            print("Result is ", result)
    else:
        print("Please choose a valid operator")


#Check check Test test
#Tes Tes Test 2


#Dolev Dolev Dolev








