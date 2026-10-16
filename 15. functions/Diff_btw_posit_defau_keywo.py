# Difference between Positional, Default, and Keyword Arguments in Python

# 1. Positional Arguments:
# - Arguments that are passed to a function in the order they are defined.
# - The position of the argument matters.
# - Example:
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

greet("Alice", 30)  # "Alice" is name, 30 is age

# 2. Default Arguments:
# - Arguments that assume a default value if a value is not provided in the function call.
# - Useful for making certain parameters optional.
# - Example:
def greet(name, age=25):
    print(f"Hello, my name is {name} and I am {age} years old.")

greet("Bob")  # age defaults to 25

# 3. Keyword Arguments:
# - Arguments that are passed to a function by explicitly specifying the parameter name.
# - The order of the arguments does not matter.
# - Example:
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

greet(age=30, name="Charlie")  # Order does not matter


# positional arguement written after keyword arguement does not work 