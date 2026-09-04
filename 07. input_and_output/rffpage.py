# to take input from user

age = input("Enter your age: ")
print(type(age))                           #asks for age and after entering age it showes class string

first , last = input ("Enter first and last name:").split()[:2]
print(first)
print(last)

#formating Decimal places
price = 99.5678
print(f"{price:.2f}")                      



