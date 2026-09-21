# INPUT

# Read 1 subject marks
# Read 2 subject marks
# Read third subject marks

# PROCESSING

# Calculate average

# OUTPUT

# Display Pass or Fail


# Algorithm

# 1. Start
# 2. Read 1 subject marks
# 3. Read 2 subject marks
# 4. Read third subject marks
# 5. Calculate average
# 6. If average is greater than or equal to 40
# 7. Display Pass
# 8. Otherwise display Fail
# 9. Stop


# Code

marks_1 = float(input("Enter 1 subject marks: "))

marks_2 = float(input("Enter 2 subject marks: "))

marks_3 = float(input("Enter third subject marks: "))

average = (marks_1 + marks_2 + marks_3) / 3

if average >= 40:
    print("Pass")
else:
    print("Fail")