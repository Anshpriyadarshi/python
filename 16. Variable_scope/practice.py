# Question 1

text = input("Enter the string:~")
char = {}
for ch in text:
    if ch.isalpha(): 
        if ch in char:
            char[ch] += 1  
        else:
            char[ch] = 1  
for ch, count in char.items():
    print(f"{ch}{count}", end=' ')  

# Question 2

i = 0
while i >= -10:
    name = "Ansh"
    i -= 1  
print(name)

# Question 3

def show_number():
    number = 5
    number = number + 1
    return number

print(show_number())
print(show_number())

# Question 4

def outer():
    def inner():
        print(list("Hello"))
    inner()
outer()

# -----------------------------------------

def outer():
    def inner():
        print(list)
    inner()
outer()

# -----------------------------------------

message = "global"
def outer():
    message = "Enclosing/nonLocal"
    def inner():
        message = "local"
        print(message)
    inner()
outer()

# Question 5

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

# -------------------------------

# same as Q5

count = 0
def increment():
    global count
    count += 1
    return count

print(increment())
















