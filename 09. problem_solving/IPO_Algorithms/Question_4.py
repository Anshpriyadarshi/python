# IPO 

# INPUT 
# Read person's age

# PROCESSING
# If person is greater than or equal to 18 -  Eligible to vote
# Otherwise - Not eligible to vote

# OUTPUT
# Print either eligible to vote or not eligible to vote


# Algorithm
# 1. Start 
# 2. Read person's age 
# 3. If person is greater than or equal to 18
# 4. Display eligible to vote
# 5. otherwise display not eligible to vote
# 6. Stop 

# code
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")