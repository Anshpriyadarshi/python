# variable scope -> where we can use variable 
# types of variable scope 

# 01- Local Scope = Variables defined within a function or a block of code.
# Examole:~
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Outputs: 10
# print(x)  # This would raise a NameError

# 02. Enclosing Scope = Applicable in nested functions where the inner function can access variables from the outer function.
# Example:~
def outer_function():
    y = 20  # Enclosing variable
    def inner_function():
        print(y)  # Accessing enclosing variable
    inner_function()  # Outputs: 20

outer_function()

# 03. Global Scope = Accessible throughout the entire module, including inside functions (unless shadowed by a local variable)
#Example:~
z = 30  # Global variable

def another_function():
    print(z)  # Outputs: 30

another_function()

# 04. Built-in Scope = Contains built-in functions and variables that are always available in Python (e.g., print(), len(), etc.).
#Example:~
print(len("Hello"))  # Outputs: 5

"""Summary
Local:~ Inside a function.
Enclosing:~ In nested functions.
Global:~ Throughout a module , or outside a function.
Built-in:~ Always available."""

