while True:
    number_uno = input("Enter a number: or enter letter (q) to quit: ")
    if number_uno.lower() == 'q':
        print("Exiting the calculator, see you next time")
        break

    number_dos = input("Enter the second number: ")
    operation = input("Choose an operation for the calculator (case insensitive):\n"
                      "A FOR ADDITION:\n"
                      "B FOR SUBTRACTION:\n"
                      "C FOR MULTIPLICATION:\n"
                      "D FOR DIVISION\n"
                      "Operation: ")

    try:
        num1 = int(number_uno)
        num2 = int(number_dos)
    except ValueError:
        try:
            num1 = float(number_uno)
            num2 = float(number_dos)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

    if operation.upper() == "A" or operation.lower() == "a":
        resul = num1 + num2
        print("The addition is:", resul)
    elif operation.upper() == "B" or operation.lower() == "b":
        result = num1 - num2
        print("The subtraction is:", result)
    elif operation.upper() == "C" or operation.lower() == "c":
        result = num1 * num2
        print("The multiplication is:", result)
    elif operation.upper() == "D" or operation.lower() == "d":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            res = num1 / num2
            print("The division is:", res)
    else:
        print("Invalid choice, make sure you chose from the options given above.")

    retry = input("Do you want to perform another calculation? (y/n) ")
    if retry.lower() != 'y':
        break

print("Thank you for using the calculator!")