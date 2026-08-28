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
