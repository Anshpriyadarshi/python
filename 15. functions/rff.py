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
# # ----------------------------------------------------------------------------------------
# <positional arguments> :~ their position in the function call determines which parameter they are assigned to in the function definition.

# # 3. Default and Keyword Arguments------------------------------------------------------

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

# # 4.Keyword Arguments-------------------------------------------------------------------

# Example
# def introduce(name, age):
#     print(name, age)

# introduce(name="Asha", age=21)       # Keyword arguement

# # FUNCTION AND RECURSION FULL REVISION ===============================================================================================

# # sum of two numbers 
# def calculate_sum(a,b):
#     sum = a + b 
#     print(sum)
#     return sum

# calculate_sum(5,10)
# calculate_sum(20,30)
    

# #Average of three numbers
# def avg_num(n1,n2,n3):
#     sum = n1+n2+n3
#     avg = sum / 3
#     print(avg)
#     return avg

# avg_num(20,30,40)

# # Count the number of the elements of list
# cities = ["delhi", "pune", "mumbai", "noida"]

# def cities_len(list):
#     print(len(list))

# cities_len(cities)

# # program to write all the list elements in a single line 

# cities = ["delhi", "pune", "mumbai", "noida"]

# def print_list(list):
#     for item in list:
#         print(item , end=" ")

# print_list(cities)

# # prpgram to write factorial of 8 :~ means 1x2x3x4x5x6x7x8

# def factorial(n):
#     fact = 1 
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# factorial(8)

# # write a function to convert USD to INR 

# def converter(usd_val):
#     inr_val = usd_val * 95
#     print(usd_val,"$ is converted into INR =",inr_val,"Rs")

# converter(10)

# # function to print even or odd

# def even_odd(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# even_odd(7)
# even_odd(8)

# *args = arguments






