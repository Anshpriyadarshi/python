#  #found or not found
# str_input = input("Enter the word:~")
# count = 0
# flag = True
# for i in range(len(str_input)):
#     count += 1
#     if str_input[i] == 'o':
#         flag = False
#         print("found")
#     else:
#         print("not found")

#  # Questions of the break.
#q1
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)

#q2
# numbers = [10, 20, 30, 40, 50]
# for number in numbers:
#     if number == 30:
#         print("Found 30!")
#         break

#q3
# while True:
#     number = int(input("Enter a number (0 to stop): "))
#     if number == 0:
#         print("Stopping input.")
#         break
#     print(f"You entered: {number}")

#q4
# for i in range(1, 101):
#     if i % 17 == 0:
#         print(f"Stopped at: {i}")
#         break
#     print(i)


# pass = place holder , editable inside code , acts as a code place holder. 
# continue = it skips the iteration or the specific set of code or input, Skip current iteration .
# Break = it stops or breaks the code , prevent it from running,Stop the nearest loop .


# contionu Questions 

# # Q1 
# for number in range(1, 21):
#     if number % 2 == 0: 
#         continue  
#     print(number)

# #Q2
# numbers = [10, -2, 30, -5, 40, -8]
# for n in numbers:
#     if n < 0: 
#         continue 
#     print(n) 

# #Q3
# for number in range(1,20):
#     if number % 3 == 0:
#         continue
#     print(number)

# #Q4
# numbers = [5,12,8,21,30,7]
# for n in numbers:
#     if n<10:
#         continue
#     print(n)


# pass Question 

# # Q1
# num = int(input("Enter the number to check positive or not:~"))
# if  num >= 0:
#     pass
# else:
#     print("neg")

# class task 1
# numbers = [10, -2, 20, 0, 30]

# for number in numbers:

#     if number < 0:
#         continue

#     if number == 0:
#         break

#     print(number)

# class task 2 
# number=[12,5,-4,18,0,25,30]

# for number in number:

#     if number < 0:
#         continue

#     if number == 0:
#         break

#     print(number)

# class task 3 
# number=[12,5,-4,18,0,25,30]

# for number in number:

#     if number < 0:
#         continue

#     if number == 0:
#         break

#     print("number not found")

for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break
    print(i)
else:
    print("Completed")
print("Outside")