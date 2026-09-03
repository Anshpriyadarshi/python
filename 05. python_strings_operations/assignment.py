# 1 Create strings

name="Ansh"
city="Patna"
programming_language="python"
message="i like 'python' and i love to code"

print(name)
print(city)
print(programming_language)
print(message)

# 2 Empty string

a="  "
print(a)
print(len(a))
print(type(a))

# 3 String information

a="Python Programming"
print(a)
print(len(a))
print(a[0])
print(a[17])
print(a[4])
print(a[16])

# 4 Positive Indexing 

a="programming"
print(a[0])
print(a[1])
print(a[4])
print(a[10])

# 5 Negative indexing
a="programming"
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-11])

# 6 Indexing Challenge
a="Ansh priyadarshi"
print(a[0])
print(a[-1])
print(a[5])

# 7 Basic Slicing
a="python programming"
print(a[0:6])
print(a[7:18])
print(a[0:18])
print(a[0:5])
print(a[13:18])

# 8 Slicing with step
a="ABCDEFGHIJKL"
print(a[::2])
print(a[::3])
print(a[1:8:2])
print(a[::-1])

# 9 Slicing with Negative indexes
a="Python Programming"
print(a[-5:])
print(a[-10:])
print(a[::-10])

# 10 Slicing Challenge
a="ABCDEFGHIJKL"
print(a[0:3])
print(a[9:13])
print(a[::2])
print(a[::-1])
print(a[1:10])

# 11 length
a="ant"
b="occupation"
c="spider man far from home"
print(len(a))
print(len(b))
print(len(c))

# 12 ''
text="python programming"
print(len(text))
print(text[17])

# 13 full Name
first_name="ansh"
last_name="priyadarshi"
print(first_name+" "+last_name)

# 14 Sentence creation
name="Ansh"
age=19
city="patna"
programming_language="python"
a=(str(age))
print(name+" "+a+" "+city+" "+programming_language)

# 15 string and integer
a="ansh"
b=22
c=(str(b))
print(a+c)

# 16 String Repetition
a="doomsday._."
print(3*a)
print(5*a)
print(10*a)

# 17 pattern
a="*"
print(10*a)

# 18 case conversion
a="onetwothree"
print(a.upper())

a="onetwothree"
print(a.lower())

a="one two three"
print(a.capitalize())

a="one two three"
print(a.title())

a="onetwothree"
print(a.swapcase())

# 19 Case-Insensitive comparision
a="Python"
b="python"
print(a,b.lower())

# 20 membership
a="Python is a programming language"
print("Python" in a)
print("programming" in a)
print("java" in a)
print("language" in a)

# 21 find
a="Python is a programming language"
print(a.find("Python"))
print(a.find("programming"))
print(a.find("language"))
print(a.find("java"))

# 22 index()
a="Python is a programming language"
print(a.index("Python"))
# print(a.index("java"))        #Error

# 23 Count characters
a="banana"
print(a.count("a"))
print(a.count("n"))
print(a.count(b))

# 24 starting and ends

# startswith 
name="student_notes.pdf"
b=name.startswith("student")
print(b)
#  Endswith

name="Student_notes.pdf"
b=name.endswith(".pdf")
print(b)

name="Student_notes.pdf"
b=name.endswith(".txt")
print(b)

# task 24
filename = "student_notes.pdf"
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))

# task 25
text = "I am learning Java"
new_text = text.replace("Java","python")
print(new_text)

# task 26
text = "apple apple apple"
print(text.replace("apple","mango"))

# task 27
text = "apple apple apple"
print(text.replace("apple","mango", 1))

# task 28
text = "Python"
print(text.upper())

# task 29
text = "   Python Programming   "
print(text.lstrip())
print(text.strip())
print(text.rstrip())

# task 30
text = "Python is easy to learn"
words = text.split()
print(words)

# task 31
text = "Python is easy to learn"

words = text.split()

print(words)


# Task 32 — Split with Separator

text = "apple,banana,mango,orange"

fruits = text.split(",")

print(fruits)


# Task 33 — Join

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)


# Task 34 — Join with Different Separators

words = ["Python", "is", "easy"]

print("-".join(words))
print("/".join(words))


# Task 35 — F-String

name = "ansh"
age = 19
city = "Kalol"

sentence = f"My name is {name}, I am {age} years old, and I live in {city}."

print(sentence)


# Task 36 — Arithmetic Inside F-String

a = 10
b = 20

print(f"The sum is {a + b}")


# Task 37 — Error Identification

# A — IndexError
text = "Python"

try:
    print(text[20])
except IndexError:
    print("IndexError: String index is out of range.")


# B — TypeError
text = "Python"

try:
    text[0] = "J"
except TypeError:
    print("TypeError: Strings cannot be changed directly.")


# C — TypeError
age = 20

try:
    print("Age: " + age)
except TypeError:
    print("TypeError: Cannot concatenate string and integer.")


# D — ValueError
text = "Python"

try:
    print(text.index("Java"))
except ValueError:
    print("ValueError: Substring not found.")


# Task 38 — Name Processor

full_name = input("Enter your full name: ")

cleaned_name = full_name.strip()

print("Original input:", full_name)
print("Cleaned name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title case:", cleaned_name.title())
print("Length:", len(cleaned_name))
print("First character:", cleaned_name[0])
print("Last character:", cleaned_name[-1])
print("Contains 'a':", "a" in cleaned_name.lower())


# Task 39 — Sentence Analyzer

sentence = input("Enter a sentence: ")
chosen_character = input("Enter a character to count: ")

print("Original sentence:", sentence)
print("Number of characters:", len(sentence))
print("Number of words:", len(sentence.split()))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Contains 'Python':", "Python" in sentence)
print("Character count:", sentence.count(chosen_character))


# Task 40 — Student Information

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = input("Enter age: ").strip()

full_name = first_name + " " + last_name

print("Full name:", full_name.title())
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Length:", len(full_name))
print("First character:", full_name[0])
print("Last character:", full_name[-1])
print("City:", city)
print("Course:", course)
print(f"Age: {age}")
print("Course contains Python:", "Python" in course)

updated_course = course.replace("Java", "Python", 1)
print("Updated course:", updated_course)

print("Number of words in course:", len(course.split()))