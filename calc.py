print("Enter which operation you want to do : ")
print("\n1. Add")
print("\n2. Subtract")
print("\n3. Multiply")
print("\n4. Divide")

choice = input("Enter your choice : ")

while True:
    try:
        number_1 = int(input("Enter a number : "))
        number_2 = int(input("Enter another number : "))
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    except ValueError:
        print("Add a number!")

    if choice == "Add" or "add":
        def add(a, b):
            return (a + b)
        print("result is : ", add(number_1, number_2))

    if choice == "Subtract" or "subtract" or "Sub" or "sub":
        def subtract(a, b):
            return (a - b)
        print("result is : ", subtract(number_1, number_2))

    if choice == "Multiply" or "multiply":
        def multi(a, b):
            return (a * b)
        print("result is : ", multi(number_1, number_2))

    if choice == "Divide" or "divide":
        def div(a, b):
            return (a / b)
        print("result is : ", multi(number_1, number_2))

    again = input("Want to calculate again? (y / n) : ")
    if again == "y":
        break