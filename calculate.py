
def calculate(num_1, num_2, operation):
    """Perform calculation and return the expression and result."""

    operation = operation.strip().lower()

    def format_number(number):
        return f"{number:g}"

    if operation in ["addition", "add", "plus", "+"]:
        result = num_1 + num_2
        expression = f"{format_number(num_1)} + {format_number(num_2)}"

    elif operation in ["sub", "subtraction", "subtract", "minus", "-"]:
        result = num_1 - num_2
        expression = f"{format_number(num_1)} - {format_number(num_2)}"

    elif operation in ["multiply", "mul", "*"]:
        result = num_1 * num_2
        expression = f"{format_number(num_1)} * {format_number(num_2)}"

    elif operation in ["divide", "div", "/"]:
        if num_2 == 0:
            raise ValueError("Division by zero is not allowed.")
        result = num_1 / num_2
        expression = f"{format_number(num_1)} / {format_number(num_2)}"

    elif operation in ["modulus", "mod", "%"]:
        if num_2 == 0:
            raise ValueError("Modulus by zero is not allowed.")
        result = num_1 % num_2
        expression = f"{format_number(num_1)} % {format_number(num_2)}"

    elif operation in ["percentage", "percent", "per", "of"]:
        result = (num_1 / 100) * num_2
        expression = f"{format_number(num_1)}% of {format_number(num_2)}"

    else:
        raise ValueError("Invalid operation. Please try again.")

    return expression, result


def calculator():
    """Run the calculator in the terminal."""

    try:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Percentage (of)")

        operation = input("\nEnter operation: ").strip().lower()

        expression, result = calculate(num_1, num_2, operation)

        print(
            f"\nThe answer of {expression} is: "
            f"{result:g}"
        )

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    calculator()
