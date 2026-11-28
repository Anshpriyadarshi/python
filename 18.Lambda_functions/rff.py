# # Lambda Syntax
# # lambda arguements: expression

# #Example :~ 
# marks = lambda a: "pass" if  a > 35 else "fail"
# print(marks(79))

# #Example 2 :~
# marks = lambda a: "A Grade" if a>90 else "B Grade" if a>75 else "Pass" if a>35 else "Fail"
# print(marks(79))

# #Example 3 :~
# number = lambda a: "even" if a % 2 == 0 else "odd"
# print(number(15))

# #Example 4 ~ Sort Words by Length
# words = ["Ninjahatori","Brahmastra","Nankhatai","idk"]
# result = sorted(words , key = lambda word:len(word))
# print(result)

# #Example 5 ~ Sort Words by Length in Descending Order
# words = ["apple", "kiwi", "banana", "fig"]
# result = sorted(words , key = lambda word: len(word), reverse=True)
# print(result)

# #Example 6
# numbers = [23,15,42,31,18]
# result = sorted(numbers , key = lambda n: n % 10)
# print(result)

