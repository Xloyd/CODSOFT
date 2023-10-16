def add(num1, num2):
  """Returns the sum of two numbers."""
  return num1 + num2

def subtract(num1, num2):
  """Returns the difference of two numbers."""
  return num1 - num2

def multiply(num1, num2):
  """Returns the product of two numbers."""
  return num1 * num2

def divide(num1, num2):
  """Returns the quotient of two numbers."""
  return num1 / num2

def main():
  """Prompts the user for two numbers and an operation, and then performs the operation on the numbers."""

  # Get the user input
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Enter the operation (+, -, *, or /): ")

  # Perform the operation
  result = None
  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operation.")
    return

  # Print the result
  print(f"{num1} {operator} {num2} = {result}")


if __name__ == "__main__":
  main()
