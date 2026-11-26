#Question 1
def place():
    local = "city"
    return local
print(place())

#Question 2
name = "school"
def function():
    global name
    print(name)
    name = "school2"
function()

#Question 3
message = "hey!"
if True:
    message = "Hello, world!"
print(message)

#Question 4 
number = 0 
for i in range(5):
    number = i
print(number)

#Question 5
# scope = where we can access the code. 

# lifetime = it is the time period till the lable and the container are binded together.

#Question 6
value = 100
def test():
    value = 200
    print(value)
test()
print(value)

# output:-
# 200
# 100

#Question 7
clicks = 0
def click():
    clicks += 1

# nothing-------- (-_-)

#Question 8
name = "Asha"
def show():
    print(name)
    name = "Ravi"
show()

# output:~ UnboundlocalError = cause of it can not access local variable Name , with no value.

#Question 9 
def place():
    city = "pune"
    def area():
        print(city)
    area()
place()

#Question 10
def create_list():
    return [1, 2, 3, 4, 5]
my_list = create_list()
print("Original list:", my_list)
my_list.append(6)
print("Modified list:", my_list)

#Question 11
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
counter = make_counter()
print(counter())
print(counter())
print(counter())

#Question 12
# output:~ 
# 3
# 2
# 1

#Question 13
# 1. Loop Variable in a Normal For Loop
# ~ When we use a normal for loop, the loop variable is defined in the local scope of the function or the global scope if not inside a function.

# 2. List Comprehension Variable
# ~ In Python 3, the variable used in a list comprehension does not overwrite an outer variable

#Question 14 
def outer_function(message):
    def inner_function():
        print(message)
    return inner_function
greet = outer_function("Hello, World!")
greet()

#Question 15
# Built-in Names:~ list, str, and sum are built-in types and functions in Python. When you assign a variable to one of these names, you "shadow" the built-in functionality.

