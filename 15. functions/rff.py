# # Syntax of function 
# def greet():                          #function_name 
#     print("Hello, Students!")         #function body
# greet()                               #function call

# #show more then 1 msg
# def Show_welcome():
#     print("Welcome to python")
# Show_welcome()
# Show_welcome()
# Show_welcome()

# #Addition
# def add():
#     a=int(input("Enter 1st number:~"))
#     b=int(input("Enter 2nd number:~"))
#     print(a+b)
# add()

# #marks of student
# def print_line():
#     print("-----------------------")

# print("Student Report")
# print_line()
# print("Name:~ Ansh")
# print_line()
# print("Marks:~85")
# print_line()

# #substraction 
# def add():
#     a=int(input("Enter 1st number:~"))
#     b=int(input("Enter 2nd number:~"))
#     print(a-b)
# add()

# #Multiplication
# def add():
#     a=int(input("Enter 1st number:~"))
#     b=int(input("Enter 2nd number:~"))
#     print(a*b)
# add()

# #floor division
# def add():
#     a=int(input("Enter 1st number:~"))
#     b=int(input("Enter 2nd number:~"))
#     print(a//b)
# add()

# #Even or odd
# def even_odd():
#     num = int(input("Enter the number:~"))
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# even_odd()

# # How value reach parameters
# def show_number(number):
#     print(number)
# show_number(36)
# show_number(39)
# show_number(37)

# # Addition 
# def addition(a,b):
#     c=a+b
#     print(c)
# a=int(input("Enter the first number:~"))
# b=int(input("Enter the second number:~"))
# addition(a,b)

# # pass a return value into another function # passed as an arguement.
# def triple(number):
#     return number * 3

# def add_five(number):
#     return number + 5

# result = add_five(triple(20))
# print(result)

# # this case prints the value 14 , 6 but in next line it shows None as output.
# def calculate(a,b):
#     total = a + b
#     difference = a - b
#     print(total,difference)

# print(calculate(10,4))

# # it will only give None as output.
# def calculate(a,b):
#     total = a+b
#     difference = a-b
#     return
# print(calculate(10,4))
# ----------------------------------------------------------------------------------------
# <positional arguments> :~ their position in the function call determines which parameter they are assigned to in the function definition.

# 3. Default and Keyword Arguments------------------------------------------------------

# A <default argument> :~ is a parameter value provided in the function definition. Python uses it when the caller does not supply an argument for that parameter.

# # Example-----------------------------------------------------------------------------
# def greet(name="Guest"):                #name is parameter , guest is value.
#     print("Hello", name)                

# greet()           #uses the default value.
# greet("Asha")     #supplies an argument, so "Asha" is used instead.

# # Example-----------------------------------------------------------------------------
# def introduce(name, city="Pune"):        #default arguement
#     print(name, "is from", city)

# introduce("Asha")                  #positional arguement
# introduce("Rahul", "Mumbai")

# 4.Keyword Arguments-------------------------------------------------------------------

# Example
# def introduce(name, age):
#     print(name, age)

# introduce(name="Asha", age=21)       # Keyword arguement



