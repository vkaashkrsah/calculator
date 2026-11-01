
def calculator():
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

        # Remove unnecessary decimal zeros
        def format_number(number):
            return f"{number:g}"

        # Perform calculations
        if operation in ["addition", "add", "plus", "+"]:
            result = num_1 + num_2
            expression = f"{format_number(num_1)} + {format_number(num_2)}"

        elif operation in ["sub", "Subtraction", "subtract", "minus", "-"]:
            result = num_1 - num_2
            expression = f"{format_number(num_1)} - {format_number(num_2)}"

        elif operation in ["multiply", "mul", "*"]:
            result = num_1 * num_2
            expression = f"{format_number(num_1)} * {format_number(num_2)}"

        elif operation in ["divide", "div", "/"]:
            if num_2 == 0:
                print("Error: Division by zero is not allowed.")
                return

            result = num_1 / num_2
            expression = f"{format_number(num_1)} / {format_number(num_2)}"

        elif operation in ["modulus", "mod", "%"]:
            if num_2 == 0:
                print("Error: Modulus by zero is not allowed.")
                return

            result = num_1 % num_2
            expression = f"{format_number(num_1)} % {format_number(num_2)}"

        elif operation in ["percentage", "percent", "per", "of"]:
            result = (num_1 / 100) * num_2
            expression = (
                f"{format_number(num_1)}% of {format_number(num_2)}"
            )

        else:
            print("Invalid operation. Please try again.")
            return

        print(f"\nThe answer of {expression} is: {format_number(result)}")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
