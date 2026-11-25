# #Question 1
# def show(n):
#     if n == 0:
#         print("Stop")
#         return
#     print(n)
#     show(n - 1)
#     print(n)
# show(2)

# # Output:~
# # 2
# # 1
# # Stop
# # 1
# # 2

# # Question 2
# # In this function, identify the base case and explain why it stops recursion.
# def total(n):
#     if n == 0:
#         return 0

#     return n + total(n - 1)

# # OUTPUT:-1
#         # 2


# # Question 3
# # Explain why this function does not reach its base case when called with count(2). Rewrite the incorrect line.
# def count(n):
#     if n == 0:
#         return
#     count(n - 1)
# count(2)


# # Question 4
# # What does this function return when called as answer(3)? Explain why.
# def answer(n):
#     if n == 0:
#         return 0

#     n + answer(n - 1)

# print(answer(3))

# # OUTPUT:-NONE and TypeEror
# # Explanation:-
# # answer(3) calls answer(2).

# # answer(2) calls answer(1).

# # answer(1) calls answer(0).

# # answer(0) returns 0.


# #Question 5
# #Write countdown(n) that prints every integer from n down to 1, then prints "Done!".

# #Constraint: n is a non-negative integer.

# #Examples:

# #countdown(3)
# # Output:

# # 3
# # 2
# # 1
# # Done!
# #Edge case: countdown(0) should print only Done!.

# def count_down(n):
#     if n == 0:
#         print("Done!")
#         return

#     print(n)
#     count_down(n -1)

# count_down(3)


# #Question 6
# # Write count_up(n) that prints numbers from 1 through n in ascending order.

# # Example:

# # count_up(4)
# # Output:

# # 1
# # 2
# # 3
# # 4
# # Edge case: count_up(0) should print nothing.
# def count_up(n):
#     if n==1:
#         print(1)
#         return
#     count_up(n-1)
#     print(n)
# count_up(4)

# # Question 7
# # Write sum_to(n) that returns the sum of all integers from 1 through n.

# # Examples:

# # print(sum_to(5))  # 15
# # print(sum_to(0))  # 0
# # Constraint: n is a non-negative integer.

# def sum_to(n):
#     return n * (n + 1) // 2


# print(sum_to(5))  
# print(sum_to(0))  

# #Question 8
# # Write factorial(n) that returns n!.

# # Examples:

# # print(factorial(4))  # 24
# # print(factorial(0))  # 1
# # Constraint: n is a non-negative integer.
# # Constraint: n is a non-negative integer
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result


# print(factorial(4))  # 24
# print(factorial(0))  # 1

