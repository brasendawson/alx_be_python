def perform_operation(num1: float, num2: float, operation: str):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"  # Handle division by zero
        return num1 / num2
    else:
        return "Invalid operation"

# Example usage
result = perform_operation(10, 5, 'divide')
print(result)  # Output will be 2.0
