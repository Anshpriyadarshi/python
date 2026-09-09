#question 1
for i in range(1,6):
    print("Hello")

#question 2
for i in range(0,10):
    print(i)

#question 3
for i in range(1,10):
    print(i)

#question 4
for i in range(10,1):
    print(i)

#question 5
for i in range(1,11):
    print(i*5)

#question 6
for i in range(1,11):
    print(i*2)

#question 7
for i in range(1,20):
    if i % 2 != 0:
        print(i)

#question 8
for i in range(1,7):
    print(i*3)

#question 9
for i in range(1,11):
    print(i*2)

#question 10 
n=int(input("Enter the number:~"))
for i in range(1,n+1):
    print(i)

#question 11
n=int(input("Enter the number:~"))
for i in range(1,n):
    if i % 2==0:
        print(i)

#question 12
n=int(input("Enter the number:~"))
for i in range(1,n):
    if i % 2 != 0:
        print(i)

#question 13
n=int(input("Enter the number :~"))
for i in range(1,n):
    if i % 2 != 0:
        print(i)

#question 14
n=int(input("Enter the number :~"))
for i in range(1,n):
    if i % 2 != 0 and i % 2 == 0:
        print(i)

#question 15
n=int(input("Enter the number:~"))
count=0
for i in range(1,n+1):                               #using count
    if n % 2 == 0:
        count+=2
        print("even no.", count)

#question 16
n=int(input("Enter the number:~"))
for i in range(1,n+1):                                #using end
    print(i,"+",end=" ")

#question 17
n = int(input("Enter number:~"))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i                                        #using sum
print("Sum of even numbers:", sum)

#question 18
n=int(input("Enter the number:~"))
sum =0
for i in range(1,n+1):
    if n % 2 != 0:
        sum+=i
        print("sum of the odd number:",sum)

#question 19
n=int(input("Enter the number:~"))
for i in range(1,n+1):
    print(i*n)

#question 20
n=int(input("Enter the number:~"))
for i in range(1,n+1):                                
    print(i,"*",end=" ")

#question 21
string = input("Enter a string: ")
for char in string:                              #using char
    print(char)

#question 22
String = input("Enter the string:-")
for char in String:
    print(char, end=" ")

# question 23








