print("we are in \n Dubai")          #\n = next line 


a="sameer"
b="sameer"
print(a==b)                          #comparision operator (==)    gives answer in bool data type


a="sameer"
print(a[2])                          #indexing (sameer=0,1,2,3,4,5) or (sameer=-6,-5,-4,-3,-2,-1)

#()=paranthesis - used for functions   ,   []=square     ,   {}= curl

a="python"
print(len(a))                        # len - findes the length without counting from 0 it counts from 1

a="python"
print(a[0:4])                        #slicing - includes first letter but exclude last letter

a="python"
print(a[::-1])                       #prints opposite using (::)

a="python"
print(a[0:5:3])                      #starting index : ending index : steps 

first_name="ansh"
last_name="priyadarshi"
full_name=first_name+" "+last_name
print(full_name)

first_name="ansh"
last_name="priyadarshi"
print(first_name+" "+last_name)

#mutablity , mutable - to which we can change  (string - immutable)

a="python"
b="f"+a[1:]                          #to build logic, and to change the string indirectly
print(b)

a="python"
b="l"+a[1::3]
print(b)

#string methods

#upper
a="python"
print(a.upper())

# lower
a="ZEBRA"
print(a.lower())

#capitalize
a="donkey"
print(a.capitalize())

#title
a="Monkey"
print(a.title())

#swapcase
a="panda"
print(a.swapcase())

#casefold
a="michael $"
print(a.casefold())

#searching in strings

#in
a="superman"
print("superman" in a)            #replys in bool 

#find
a="thor"
print(a.find("r"))

# index 
text="hello python"
print(text.index("python"))

# text="hello python"
# print(text.index("java"))         #value error

#count
text="banana"
print(text.count("a"))            #used to count the letter

#startswitch
text="Python Programming"
print(text.startswith("Python"))

#endswith
filename="notes.txt"
print(filename.endswith(".txt"))

