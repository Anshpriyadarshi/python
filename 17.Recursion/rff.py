#Recurtion:~ Recurtion is when a function calls itself to solve a smaller version of the same problem.
# types of Recurtion:~
# 1. Base case ~ tells the function when to stop.
# 2. Recursive case ~ calls the function again with a smaller or similer problem.

#Question 1 
# add = 0
# def function(n):
#     global add
#     add += 1
#     if n == 10:
#         return add
#     return function(n + 1)
# result = function(1)
# print(result)

# # Recurtion frames  ///////////////////////////////////------------------------///////////////////////////////////

# # Step 1
# def factorial(5):
#     if 5 == 0:
#         return 1

#     return 5 * factorial(5 - 1)

# print(factorial(5))
# print(factorial(0))

# # Step 2 
# def factorial(4):
#     if 4 == 0:
#         return 1

#     return 4 * factorial(4 - 1)

# #step 3
# def factorial(3):
#     if 3 == 0:
#         return 1

#     return 3 * factorial(3 - 1)

# #step 4
# def factorial(2):
#     if 2 == 0:
#         return 1

#     return 2 * factorial(2 - 1)

# #step 5
# def factorial(1):
#     if 1 == 0:
#         return 1

#     return 1 * factorial(1 - 1)

# #Step 6
# def factorial(0):
#     if 0 == 0:
#         return 0

# /////////////////////////////////------------------------------------/////////////////////////////////

