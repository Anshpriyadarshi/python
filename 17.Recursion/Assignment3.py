# #Question 1
def my_message(message,n):
    if n <= 0:
        return
    print(message)
    my_message(message,n-1)
my_message("Hello", 3)

#Question 2
n = int(input("Enter a number: "))
def even(n):
    if n == 0:
        return
    even(n - 1)
    if n % 2 == 0:
        print(n, end=" ")
even(n)

#Question 3
n = int(input("Enter a number: "))
def odd(n,add = 0):
    if n == 0:
        return add
    if n % 2 != 0:
        add+=n
    return odd(n - 1,add)
print(odd(n))

#Question 4
def digit(num, target):
    if num == 0:
        return 0
    count = 0
    if num % 10 == target:
        count = 1
    return count + digit(num // 10, target)
print(digit(54354544, 5))

#Question 5
def product(n):
    if n == 0:
        return 1
    i= n%10
    return i*product(n//10)
print(product(234333))

#Question 6
def left(n):
    if 0<=n<10:
        return n
    i = n%10
    count =i
    return left(n//10)
print(left(6837))

#Question 7
def left(n,tar=23):
    if 0<=n<10:
        return True
    if n%10 == tar:
        return True
    return left(n//10)
print(left(1234))

#Question 8
def cnt(n):
    if n == "":
        return 0
    return 1 + cnt(n[1:])
print(cnt("coding"))

#Question 9
def left(n, i=0):
    if i == len(n):
        return 0
    vowels = "aeiou"
    if n[i] in vowels:
        return 1 + left(n, i + 1)
    else:
        return left(n, i + 1)
print(left("education"))

#Question 10
n = input("Enter a String: ")
def palan(n,a=0):
    b=len(n)-1-a
    if a > b:
        return True
    if n[a]!=n[b]:
        return False
    return palan(n,a+1)
print(palan(n))
