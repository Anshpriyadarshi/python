# startswith()
test="Python programming"
print(test.startswith("Py"))
print(test.startswith("ng"))        #false


#  Endswith()
test="python programming"
print(test.endswith("ng"))
print(test.endswith("py"))           #false

#  limiting replacement

# string.replace(old,new,count)
text="apple apple apple"
print(text.replace("apple","mango" ,1))              # 1 at the last refers to which word it will change 

# string comparision 
a="apple"
b="banana"
print(a==b)                      #false

a="ansh"
b="ansh"
print(a==b)

# strip
text="  hello  "
print(text.strip())

# lstrip and rstrip
text="    hey   "
print(text.rstrip())
print(text.lstrip())

#Escape character
print("hello\nworld")                                  #(9,8)- touple   #[9,8]- list

#string membership
text="python programming"
print("python" in text)

# string formating()
name="John"
age=20
print(f"my name is {name} and i am {age} years old.")

#split()
text="python is easy"
words=text.split()
print(words)


