# Question 1
name = input("Enter your name:-")
print(name)

# Question 2
name = input("Enter your city:-")
print("your city is "+ (name))

# Question 3
name = input("Enter your name:-")
age = input("Enter your age:-")
print(name,age)

# Question 4
"string is the answer"

# Question 5
age = input("Enter your age:-")
print(type(age))

# Question 6
first_name = input("Enter first name:-")
last_name = input("Enter last name:-")
print(first_name,last_name)

# Question 7
name = input("Enter name:-")
city = input("Enter city:-")
college = input("Enter college:-")
print(name,city,college)

# Question 8
first , last = input ("Enter first and last name:").split()[:2]
print(first)
print(last)

# Question 9
first , last = input ("Enter first and last name:").split()[:2]
print(first)
print(last)         #user will get python in one variable and programming in another 

# Question 10 
first , middle , last = input ("Enter first,middle and last name:").split()[:3]
print(first)
print(middle)
print(last)    

# 11. Convert string to integer
a = "25"
a = int(a)
print("Q11:", a)

# 12. Convert string to float
a = "25.5"
a = float(a)
print("Q12:", a)

# 13. Convert integer to string
a = 100
a = str(a)
print("Q13:", a)

# 14. Take integer and print its type
a = int(input("Q14 - Enter an integer: "))
print(type(a))

# 15. Take float and print its type
a = float(input("Q15 - Enter a floating-point number: "))
print(type(a))

# 16. Input returns strings
a = input("Q16 - Enter first value: ")
b = input("Q16 - Enter second value: ")
print("String concatenation:", a + b)

# 17. Numeric addition
a = int(input("Q17 - Enter first number: "))
b = int(input("Q17 - Enter second number: "))
print("Numeric addition:", a + b)

# 18. f-string with name and age
name = "Rahul"
age = 20
print(f"Q18: My name is {name} and I am {age} years old.")

# 19. f-string with sum
a = 10
b = 20
print(f"Q19: The sum is {a + b}")

# 20. User name and age
name = input("Q20 - Enter your name: ")
age = int(input("Q20 - Enter your age: "))
print(f"My name is {name} and I am {age} years old.")

# 21. Price with exactly two decimal places
price = float(input("Q21 - Enter product price: "))
print(f"Price: {price:.2f}")

# 22. :.2f example
price = 99.5
print(f"Q22: {price:.2f}")

# 23. Product name, price and quantity
product_name = input("Q23 - Enter product name: ")
price = float(input("Q23 - Enter price: "))
quantity = int(input("Q23 - Enter quantity: "))

print(f"Product: {product_name}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")

# 24. Default print separator
print("Q24:", "A", "B", "C")

# 25. Print using - as separator
print("Q25:", "2026", "08", "19", sep="-")

# 26. Two print statements on same line
print("Q26: Hello", end=" ")
print("World")

# 27. Two integers and their sum
first = int(input("Q27 - Enter first number: "))
second = int(input("Q27 - Enter second number: "))

sum = first + second

print(f"First number: {first}")
print(f"Second number: {second}")
print(f"Sum: {sum}")

# 28. Price, quantity and total cost
price = float(input("Q28 - Enter price: "))
quantity = int(input("Q28 - Enter quantity: "))

total = price * quantity

print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")

# 29. Student name, age and marks
name = input("Q29 - Enter student name: ")
age = int(input("Q29 - Enter age: "))
marks = float(input("Q29 - Enter marks: "))

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks:.2f}")

# 30. Student Information
name = input("Q30 - Enter student name: ")
age = int(input("Q30 - Enter age: "))
height = float(input("Q30 - Enter height: "))
city = input("Q30 - Enter city: ")

print("\nStudent Information")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f}")
print(f"City: {city}")