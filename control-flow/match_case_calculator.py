num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /): \n")


match operation:
    case "+":
        num1 + num2
        print(f"The result is {num1+num2}")
    case "-":
        num1 - num2
        print(f"The result is {num1 - num2}")
    case "*":
        num1 * num2
        print(f"The result is {num1 * num2}")
    case "/":
        num1 / num2
        print(f"The result is {num1 / num2}")
    

        



