# for loop assignment Questions into while loop 

# Question 1
i = 1
while i<=5: 
    print("Hello")
    i+=1

#Question 2
i=0
while i<=9:
    print(i,end=" ")
    i+=1

#Question 3
i= 1
while i<=10:
    print(i)
    i+=1

#Question 4
i=10
while i>=1:
    print(i)
    i-=1

#Question 5
i=5
while i<=50:
    print(i)
    i+=5

#Question 6
i=2
while i <=20:
    print(i)
    i+=2

#Question 7
i=1
while i<=19:
    print(i)
    i+=2

#Question 8
i=3
while i<=18:
    print(i)
    i+=3

#Question 9
i=20
while i>=2:
    print(i)
    i-=2

#Question 10
n = int(input("Enter the positive integer:~"))
i=1
while i<=n:
    print(i)
    i+=1

# Question 11
n=int(input("Enter the number:~"))
i = 0
while i <= n:
    print(i)
    i+=2

# Question 12
n= int(input("Enter the number:~"))
i=1
while i<=n:
    print(i)
    i+=2

# Question 13
n=int(input("Enter the Number:~"))
i = 1
while i<=n:
    print(i)
    i+=2

#Question 14 
n=int(input("Enter the number:~"))
i=1
while i<=n:
    if i % 2==0 and i % 3==0:
        print(i)
    i+=1

# Question 15
n=int(input("Enter the number :~"))
i = 1
count = 0
while i <=n:
    if i % 2==0:
        count+=1
    i += 1
print("Even numbers are:~",count)

#Question 16
n = int(input("Enter n:~ "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum =", total)

#Question 17
n = int(input("Enter the number:~"))
i= 1
total =  0
while i <=n:
    if n%2==0:
        total +=i
    i+=1
print("sum of even number:~",total)

#Question 18
n = int(input("Enter the number:~"))
i = 1
total = 0
while i <= n:
    if n%1==0:
        total += i
    i+=1
print("sum of odd number:~",total)

# Question 19
n = int(input("Enter the number:~"))
i = 1
while i<=10:
    print(n,"X", i, "=", n*i)
    i*=n

# Question 20
n = int(input("Enter a number:~ "))
i = 1
product = 1
while i <= n:
    product *= i
    i += 1
print("Product:", product)

#Question 21
n = int(input("Enter the number:~"))
i = 0
while i <= n:
    i +=1
    print(i-1)

#Question 22
n = int(input("Enter the number:~"))
i = 0
while i <= n:
    i += 1
    print(i-1,end=" ")

# Question 23
word = input("Enter the word:~")
count = 0
i=0
while i < len(word):
    count+=1
    i+= 1
print(count)




