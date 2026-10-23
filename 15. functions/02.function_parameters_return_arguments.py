# #Q1
# def greet(name):
#     print("Hello", name)

# greet("Asha")
# greet("Rahul")

# output:~ 
# Hello Asha
# Hello Rahul

# #Q2
# def subtract(a, b):
#     return a - b

# print(subtract(8, 3))
# print(subtract(3, 8))

# output:~
# 5
# -5

# #Q3
# def calculate(number):
#     return number * 2

# result = calculate(5)
# print(result + 3)

# Output:~
# 13

# #Q4
# def greet(name="Guest"):
#     return "Hello " + name

# print(greet())
# print(greet("Asha"))

# output:~
# Hello Guest
# Hello Asha

# #Q5
# def values():
#     return 10, 20

# a, b = values()
# print(a + b)

# output:~
# 30

# #Q6
# def show(a, b=5):
#     print(a, b)

# show(10)
# show(10, 20)
# show(a=7, b=3)

# output:~
# 10,5
# 10,20
# 7,3

# #Q7
# def demo():
#     print("A")
#     return 5
#     print("B")

# print(demo())

# output:~
# A 
# 5

# #Q8
# def total(a, b, c=10):
#     return a + b + c

# print(total(1, c=3, b=2))

# output:~
# 6

# # BEGINNER---------------------------------------------------------------------------------------

# #Q1 
# def welcome():
#     print("Welcome to python")

# welcome()
# welcome()
# welcome()

# #Q2
# def greet(name):
#     print(f"Hello, {name}! Welcome!")

# greet("Ansh")

# #Q3
# def show_number(number):
#     print(number)

# show_number(43)

# #Q4
# def add(a,b):
#     sum = a + b
#     print(sum)
#     return sum

# add(4,9)

# # Q5 
# def square(n):
#     squ = n*n
#     print(squ)

# square(5)

# #Q6
# def is_even(n):
#     if n % 2 == 0:
#         print("True")
#     else:
#         print("False")

# is_even(10)
    
# #Q7
# def get_full_name(first_name,last_name):
#     fullname = first_name + last_name
#     print(fullname)
#     return fullname

# get_full_name("Ansh ","priyadarshi")

# #Q8
# def introduce(name, city="pune"):
#     intro = name+" is from "+ city
#     print(intro)
#     return intro

# introduce("Ansh")

# #Q9
# def subtract(a,b=5):
#     sub = a - b 
#     print(sub)
#     return sub

# subtract(10)

# #10
# def get_min_max(a,b):
#     if a < b :
#         return a,b 
#     else :
#         return b,a 
# smaller,larger = get_min_max(5,10)
# print("smaller:~", smaller)
# print("larger:~", larger)

# # INTERMEDIATE----------------------------------------------------------------------------

# # Q11 
# def calculate(a,b):
#     sum = a + b 
#     sub = a - b 
#     prod = a * b 
#     quot = a // b 
#     print("sum:~",sum)
#     print("sub:~",sub)
#     print("product:~",prod)
#     print("quotient:~",quot)

# calculate(10,5)

# # Q12
# numbers = [0,1,2,3,4,5,6,7,8,9,]
# def count_digits(number):
#     print(len(numbers))

# count_digits(numbers)

# # Q13
# def classify_number(number):
#     if number > 0:
#         return "positive"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "zero"

# result = classify_number(-5)
# print("The number is:~", result)
    
# # Q14
# def calculate_total(price,quantity=1):
#     total_price = price * quantity
#     return total_price

# result = calculate_total(115)
# print("The total price =", result)

# # Q15
# def create_email(username,domain="@gmail.com"):
#     email = username + domain
#     return email

# result = create_email("Ansh")
# print("your email is:~", result)

# # Q16
# def format_name(first,last,uppercase=False):
#     full_name = first + last
#     if uppercase:
#         return full_name.upper()
#     return full_name

# print(format_name("Ansh ","priyadarshi"))

# # Q17
# def percentage(marks,total=100):
#     percent = marks / total
#     return percent * 100

# result = percentage(89)
# print(result)

# # Q18
# def convert_minutes(minutes, second_per_minute=60):
#     total_sec = minutes * second_per_minute
#     print("total_sec =",total_sec)
#     return total_sec

# convert_minutes(10)

# # Q19
# def student_details(name,age,city):
#     return f"Name:{name},Age:{age},City:{city}"

# details = student_details(age="19",city="patna",name="Ansh")
# print(details)

# # Q20
# def bill(item,quantity=1,price=100):
#     total_count = item * quantity
#     total_bill = total_count * 100
#     print(total_bill)
#     return total_bill

# bill(5)

# challenging----------------------------------------------------------------------------  

# # Q21 
# def analyze_number(number):
#     absolute_value = number if number >= 0 else -number
#     is_even = number % 2 == 0
#     num_digits = len(str(absolute_value))
#     return absolute_value,is_even,num_digits

# result = analyze_number(-1234)
# print(result)

# # Q22
# def calculate_stats(a,b,c):
#     smallest = min(a,b,c)
#     largest = max(a,b,c)
#     total_num = a+b+c
#     return smallest,largest,total_num

# result = calculate_stats(10,29,38)
# print(result)

# # Q23
# def make_sentence(subject,verb,object):
#     return f"{subject} {verb} {object}"

# final = make_sentence(object="The ball",subject="Ansh",verb="kicked")
# print(final)

# # Q24
# def apply_discount(price,discount=20):
#     total_price = price - discount
#     return total_price
    
# result = apply_discount(300)
# print(result)

# # Q25
# def calculate_pay(hours,rate=200,bonus=0):
#     return (hours * rate) + bonus

# result = calculate_pay(24,bonus=30)
# print(result)
    

# # Q26
# def get_coordinates(x=0,y=0):
#     return x,y 

# default_coordinates = get_coordinates()
# print(default_coordinates)

# coordinates_x = get_coordinates(x=5)
# print(coordinates_x)

# coordinates_y = get_coordinates(y=10)
# print(coordinates_y)

# coordinates_both = get_coordinates(x=3, y=4)
# print(coordinates_both)  

# # Q27
# def compare(a, b):
#     if a > b:
#         result = "A is greater"
#         difference = a - b
#     elif a < b:
#         result = "B is greater"
#         difference = b - a
#     else:
#         result = "Equal"
#         difference = 0
    
#     return result, difference

# comparison1 = compare(10, 5)
# comparison2 = compare(3, 7)
# comparison3 = compare(4, 4)

# print(comparison1) 
# print(comparison2) 
# print(comparison3)  

# # Q28
# def convert_temperature(value, scale="C"):
#     if scale == "C":
        
#         converted_value = (value * 9/5) + 32
#     elif scale == "F":
        
#         converted_value = (value - 32) * 5/9
#     else:
#         raise ValueError("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")
    
#     return converted_value

# celsius_to_fahrenheit = convert_temperature(25, "C")  
# fahrenheit_to_celsius = convert_temperature(77, "F")  

# print(celsius_to_fahrenheit)  
# print(fahrenheit_to_celsius)   

# Q29
