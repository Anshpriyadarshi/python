Lambda Syntax
lambda arguements: expression

#Example :~ 
marks = lambda a: "pass" if  a > 35 else "fail"
print(marks(79))

#Example 2 :~
marks = lambda a: "A Grade" if a>90 else "B Grade" if a>75 else "Pass" if a>35 else "Fail"
print(marks(79))

#Example 3 :~
number = lambda a: "even" if a % 2 == 0 else "odd"
print(number(15))



