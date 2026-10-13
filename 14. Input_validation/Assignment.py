# # Question 1
# while True:
#     try:
#         marks = float(input("Enter marks between 0 and 100 (inclusive):~"))
#         if 0 <= marks <= 100:
#             print(f"Accepted marks: {marks}")
#             break
#         else:
#             print("Invalid input. Please enter marks within the range of 0 to 100.")
#     except ValueError:                                                                         
#         print("Invalid input. Please enter a numeric value.")            

# Q - what is except valueError:
# Purpose: This line catches exceptions that are raised when the code inside the try block encounters a ValueError.


# # Question 2
# while True:
#     try:
#         num = int(input("Enter the Number:~"))
#         if num > 0:
#             print(f"Accepted Number:{num}")
#             break
#         else:
#             print("Invalid input, please enter the positive number:~")
#     except ValueError:
#         print("Invalid input, please enter a numeric value:~")

# # Question 3
# while True:
#     age=int(input("Enter the age 0 to 120:~"))
#     if 0<= age <=120:
#         print(f"Age is accepted:{age}")
#         break
#     else:
#         print("Error, please enter age properly")

# # Question 4
# while True:
#     print("\nMenu")
#     print("1. View profile")
#     print("2. Edit profile")
#     print("3. Settings")
#     print("4. Exit")
#     choice = int(input("Enter Your Choice (1-4):~"))
#     if choice in [1,2,3,4]:
#         print("Choice is Accepted:{choice}")
#         break
#     else:
#         print("Invalid input, chal foot, nhi nhi ruk firse input de (-_-):~")

# Question 5
