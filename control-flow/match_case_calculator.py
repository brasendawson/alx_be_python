num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")


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
        if num2 <=1:
            print("Cannot divide by zero.")
        num1 / num2
        print(f"The result is {num1 / num2}")
        
    

        



