again = 'Y'
while again == 'Y':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    o = input("Enter operation (+, -, *, /): ")
    if o == '+':
        print(a + b)
    elif o == '-':
        print(a - b)
    elif o == '*':
        print(a * b)
    elif o == '/':
        if b != 0:
            print(a / b)
        else:
            print("Error: Division by zero")
    again = input("Do you want to perform another calculation? (Y/N): ").upper()