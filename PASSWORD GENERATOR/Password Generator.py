import random

def generate_password(length=12, include_lower=True, include_upper=True, include_numbers=True, include_symbols=True):
  """Generates a random password of the specified length, including the specified character types.

  Args:
    length: The length of the password.
    include_lower: Whether to include lowercase letters in the password.
    include_upper: Whether to include uppercase letters in the password.
    include_numbers: Whether to include numbers in the password.
    include_symbols: Whether to include symbols in the password.

  Returns:
    A random password of the specified length, including the specified character types.
  """

  # Create a list of all the possible characters
  characters = []
  if include_lower:
    characters.extend(list("abcdefghijklmnopqrstuvwxyz"))
  if include_upper:
    characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
  if include_numbers:
    characters.extend(list("0123456789"))
  if include_symbols:
    characters.extend(list("!@#$%^&*()-_"))

  # Generate a random password
  password = ""
  for i in range(length):
    password += random.choice(characters)

  return password


def main():
  """Generates a random password and prints it to the console."""

  password = generate_password()
  print(f"Your new password is: {password}")


if __name__ == "__main__":
  main()
