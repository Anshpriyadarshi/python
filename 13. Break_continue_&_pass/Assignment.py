#Question 1
for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished")

#Question 1 - output ~
#1
#2
#3
#4
#Finished

#Question 2
word = "skyline"
for ch in word:
    if ch in "aeiou":
        break
    print(ch)

# #Question 2 - output ~
# s
# k
# y
# l

#Question 3
n = 2
while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2

#Question 3 - output ~
# 2
# 4
# 6

