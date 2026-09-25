#Question 1
for i in range(3):
    for j in range(3):
        print("* ",end="")
    print()

#Question 2
for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()

#Question 3
for i in range(1,4):
    for j in range(1,4):
        print(i,end="")
    print()

#Question 4
for i in range(6):
    for j in range(1,i+1):
        print("* ",end="")
    print()

#Question 5
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

# Question 6
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Question 7
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#Question 8
for i in range(1,11):
    for j in range(1,6):
        print(j*i,end="\t")
    print()

# Question 9
for i in range(1,4):
    for j in range(1,6):
        print(i*j,end=" ")
    print()

# Question 10
for i in range(1,6):
    for j in range(1,6):
        print(j*j,end=" ")
    print()

#question 11
for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()

#Question 12
for i in range(6):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()

#question 13 
for i in range(1,6):
    for j in range(1,i+1):
        print(2*j-1,end=" ")
    print()

#Question 13 with input
n = int(input("Enter the Number:~"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j-1,end=" ")
    print()

#Question 14
for i in range(1,6):
    for j in range(1,i+1):
        print(2*j,end=" ")
    print()

#Question 15
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

#Question 16
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

#Question 17
num=1
for i in range(1,4):
    for j in range(1,4):
        print(num,end=" ")
        num+=1
    print()

#Question 18
num=1
for i in range(1,5):
    for j in range(1,6):
        print(num,end=" ")
        num+=1
    print()

#Question 19
for i in range(1,4):
    for j in range(1,4):
        print(f"{i,j}",end=" ")
    print()

#Question 20
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

# Question 21
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print()

# Question 22
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#Question 23
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()

#Question 24
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

# Question 25
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()


