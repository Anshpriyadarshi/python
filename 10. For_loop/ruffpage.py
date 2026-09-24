# #sintax of for_loop
# for number in range(1,6):
#     print("number")

# for num in range(0,40):                                    
#     print("Ansh")                                          #print(num, end=" ")~ prints horizontally

# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print( num * i)

# #palindrome string
# name=input("Enter the string:~").strip().lower()
# length=len(name)
# sum=""
# for i in range(length-1,-1,-1):
#     sum=sum+name[i]
# print(sum)

# if name==sum:
#     print("string is palindrome")
# else:
#     print("not palindrome") 

# #pattern
# n=input("Enter the number:~")
# length=len(n)
# for i in range(length-1,0,+1):
#     print(sum)

# # iterating over a string
# name="python"
# for char in name:
#     print(char)

# #counter
# word = "Python"                                   #word.count("a")
# count = 0
# for character in word:
#     count = count + 1
# print("Characters:", count)

# #pattern
# for row in range(3):                              # ****
#     for column in range(4):                       # ****            
#         print("*", end="")                        # ****
#     print()

# #pattern
# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print("")
# print("*"*4)

# #pattern
# for i in range(4):
#     print("*"*4)

# #pattern positive star
# for i in range(1, 6):
#     for j in range(i):
#         print("*" , end="")
#     print()

# #Negative star pattern 
# n = 5
# for i in range(n, 0, -1):
#     print("*" * i)

# #pattern decreasing but from another side
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * i)

# #pattern pyramid
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)

# # Question no.8 of exam
# total=0
# flag=True
# passed=True
# grade=""
# for i in range(5):
#     marks=int(input("Enter the marks:~"))
#     total+=marks
#     if marks<35:
#         passed=False

# if passed :
#     percentage=total/5
#     if percentage>=90:
#         grade="A+"
#     elif percentage>=80:
#         grade="A"
#     elif percentage>=70:
#         grade="B"
#     elif percentage>=60:
#         grade="c"
#     elif percentage>=50:
#         grade="D"
#     else:
#         grade="F"

# if passed ==True:
#     print(f"Totalmarks is :~ {total} and your percentage is:~ {percentage} with grade:~ {grade}...")
#     print("You are Passed")
# else :
#     print("YOU are fail, bhago yaha se")

# Question no.9 of exam
# total=0
# flag=True

