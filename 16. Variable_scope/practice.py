# # Question 1
# text = input("Enter the string:~")
# char = {}
# for ch in text:
#     if ch.isalpha(): 
#         if ch in char:
#             char[ch] += 1  
#         else:
#             char[ch] = 1  
# for ch, count in char.items():
#     print(f"{ch}{count}", end=' ')  

# # Question 2
# i = 0
# while i >= -10:
#     name = "Ansh"
#     i -= 1  
# print(name)

# # Question 3
# def show_number():
#     number = 5
#     number = number + 1
#     return number

# print(show_number())
# print(show_number())

# # Question 4
# def outer():
#     def inner():
#         print(list("Hello"))
#     inner()
# outer()
# # -----------------------------------------
# def outer():
#     def inner():
#         print(list)
#     inner()
# outer()
# # -----------------------------------------
# message = "global"
# def outer():
#     message = "Enclosing/nonLocal"
#     def inner():
#         message = "local"
#         print(message)
#     inner()
# outer()
