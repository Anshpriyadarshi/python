# Predict the output before running each program.

# Question 1
def greet():
    print("Hello")

print("Start")

output:~ Start

# Question 2
def greet():
    print("Hello")

greet()
greet()

output:~Hello
        hello

# Question 3
def first():
    print("A")

def second():
    print("B")

second()
first()
second()

output:~
B
A 
B

# Question 4
def show():
    print("Inside")

print("One")
show()
print("Two")
show()

output:~
One
Inside
Two
Inside

# Question 5
def outer():
    print("Start")
    print("Middle")

print("A")
outer()
print("B")

output:~
A
Start
Middle
B


# Question 6
def task():
    print("Task")

task
print("Done")

output:~
Done

# Question 7
def greet():
    print("Hello")

Greet()

# no output its an error 

Identify the error, if any.

# Question 8
def show():
    print("A")
    print("B")

print("C")
show()

output:~ 
C 
A 
B 

# 13. Coding Practice Problems
# Q1
def greet():
    print("Hello, Python!")

greet()  

# Q2
def show_name():
    print("Monica")

show_name()  
show_name()
show_name()

# Q3
def print_line():
    print("-" * 20)

print_line() 
print("Heading") 
print_line() 

#Q4
def show_rules():
    print("1. Respect others.")
    print("2. Raise your hand to speak.")
    print("3. Follow instructions.")

# show_rules()

#Q5
def show_square():
    print("****\n****\n****\n****")

show_square() 

#Q6
def show_menu():
    print("1. Option A")
    print("2. Option B")
    print("3. Option C")

show_menu()  
show_menu()  

#Q7
def morning_message():
    print("Good morning! Have a great day!")

def evening_message():
    print("Good evening! Hope you had a wonderful day!")

evening_message()
morning_message()

#Q8
def show_student_card():
    print("Student Card")
    print("Name: John Doe")  
    print("Roll Number: 12345") 

show_student_card() 

#Q9
def print_numbers():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)

print_numbers()  
print_numbers()  

#Q10
def show_pattern():
    print("*\n**\n***")

show_pattern()
show_pattern()

# Q11
def show_header():
    print(" Report Header ")

def show_body():
    print("This is the body of the report.")
    print("Here you can include detailed information.")

def show_footer():
    print(" End of Report ")

show_header()
show_body()
show_footer()

#Q12
def show_separator():
    print("================================")

def show_report():
    print("Report Title")
    show_separator()

    print("section 1")
    print("Body")
    show_separator()

    print("Section 2")
    print("Body")
    show_separator()

show_report()
    
#Q13
def step_one():
    print("Step One")

def step_two():
    print("Step Two")

def step_three():
    print("Step Three")

step_three()
step_one()
step_two()

#Q14
def show_table_heading():
    print("ID | Name | Age")
    print("-------------")

show_table_heading()
print("1  | Alice | 20")
print("2  | Bob   | 22")

# #Q15
def print_stars():
    print("*****")

print_stars():
print_stars():
print_stars():
print_stars():

#Q16
def show_welcome():
    print("Welcome to the Course Management System")
    print("Course: Python Programming")

show_welcome()

#Q17
def show_help():
    print("Instructions for the Simple Calculator:")
    print("1. Enter numbers to perform calculations.")
    print("2. Use + for addition, - for subtraction, * for multiplication, / for division.")

show_help()

#Q18
def print_receipt_opening():
    print("===== Receipt =====")

def print_receipt_closing():
    print("===================")

print_receipt_opening()
print("Item: Book   | Price: $10")
print("Item: Pen    | Price: $2")
print_receipt_closing()

# Q19
def print_box():
    print("This is a fixed text box.")
    print("Line 2 of the text box.")
    print("Line 3 of the text box.")

print_box()
print_box()

#Q20
def show_program_title():
    print("Program Title: Simple Program")

def show_menu():
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")

def show_closing_message():
    print("Thank you for using the program!")

show_program_title()
show_menu()
show_closing_message()

# Q21
def greet():
    print("Hello")        # indentation error fixed

# Q22
def welcome():
    print("Welcome")

welcome()                 # call function added

# Q23 
def show():
    print("Hello")

show()                       # Always call function at the End

# Q24
def print_report():
    print("Report")

print_report()                 # changed capital P and R to p and r

# Q25
def a():
    print("A")

def b():
    print("B")

a()
b()
a()       # output:~ A B A    cause its function call

# Q26
def message():
    print("Python")

message()
message()
message()
message()         # 4 times

# Q27
def example():
    print("One")             # belongs to function body
    print("Two")             # belongs to function body

print("Three")        

# Q28
f ~ function_f
DoTask ~ perform_task
studentdetails ~ student_details
x1 ~ display_menu

# Q29
def greet():
    print("Hello, welcome!")

def farewell():
    print("Goodbye, see you later!")

greet()

#Q30
def display_message():
    print("This is the message from the function.")


print("This message is printed before the function call.")

display_message()

print("This message is printed after the function call.")

