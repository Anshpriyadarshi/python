# Initialization     i=1
# condition         while i<=10:                      if program get out of control = (ctrl+c) in terminal
# update            print(i)
                    # i += 1

#  #Table of 2
# i=2
# while i<= 20:
#     print(i)
#     i+=2



#  #palindrome code with while loop.

# word = input("Enter a word:~ ")

# original = word
# reverse = ""

# i = len(word) - 1

# while i >= 0:
#     reverse += word[i]
#     i -= 1

# if original == reverse:
#     print(f"{word} - is a palindrome")
# else:
#     print(f"{word} - is Not Palindrome")



#  #Second code of palindrome 

# word = input("Enter the word:~")
# i=0
# j= len(word)-1
# flag = True
# while i<j:
#     if word[i]==word[j]:
#         i+=1
#         j-=1
#     else:
#         flag = False
#         break
# if flag:
#     print(f"{word} - is palindrome")
# else:
#     print(f"{word} - is Not palindrome")