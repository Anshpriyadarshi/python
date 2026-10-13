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

# Q4. Stop at a Target Number
# Take an integer limit. Print numbers from 1 through limit, but stop before printing 7.

# If limit is less than 7, print all numbers up to limit.

# Test cases

# Input Expected output

limit = int(input())

for i in range(1, limit + 1):
    if i == 7:
        break
    print(i, end=" ")
# Q5. Find the First Matching Character
# Take a string and a target character. Scan the string from left to right. Print each character as it is checked. Stop immediately after finding the target.

# If the target does not appear, check the entire string.

# Test cases

# Input string Target Expected checked characters

# computer p c o m p banana x b a n a n a level l l

s = input()
target = input()

for ch in s:
    print(ch, end=" ")
    if ch == target:
        break
# Q6. Stop at a Negative Number
# Given a sequence of integers, print numbers from left to right and stop when the first negative number is encountered. Do not print the negative number.

# Test cases

# Input Expected output

# 4 8 2 -3 9 4 8 2 -1 5 6 No numbers printed 2 4 6 2 4 6
numbers = list(map(int, input().split()))

for num in numbers:
    if num < 0:
        break
    print(num, end=" ")
# A3. Think Carefully --- Challenging
# Q7. break Only Exits the Inner Loop
# Predict the output.

# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)
# Explain why the outer loop continues.
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2


# Q8. Search a Word
# Take a sentence and a target word. Check the words from left to right. Print "Found" and stop when the target word is found. If the target is absent, print "Not found".

# Test cases

# Sentence Target Expected output

# python makes coding fun coding Found loops are useful java Not found learn python python python Found
sentence = input().split()
target = input()

for word in sentence:
    if word == target:
        print("Found")
        break
else:
    print("Not found")


# Section B --- Practice Problems on continue
# The continue statement skips the remaining statements in the current iteration and proceeds to the next iteration.

# B1. Output Prediction --- Easy
# Q9. Skip Number 4
# Predict the output.

for i in range(1, 7):
    if i == 4:
        continue
    print(i)
    # output;-
# 1
# 2
# 3
# 5
# 6


# Q10. Skip Vowels
# Predict the output.

for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")
    # d c t n


# Q11. continue in a while Loop
# Predict the output.

# n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)
# 1
# 2
# 4
# 5


# B2. Write a Program --- Medium
# Q12. Print Numbers That Are Not Multiples of 3
# Take an integer n. Print numbers from 1 to n, skipping multiples of 3.

# Test cases

# Input Expected output

# 8 1 2 4 5 7 8 3 1 2 2 1 2
n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")

# Q13. Remove a Chosen Character from Display
# Take a string and a character. Print the string without displaying any occurrence of that character. Do not use string replacement methods; use a loop and continue.

# Test cases

# String Character Expected output

# mississippi s miippi banana a bnn hello x hello
s = input()
ch = input()

for c in s:
    if c == ch:
        continue
    print(c, end="")



# Q14. Print Only Passing Marks
# Given marks separated by spaces, print only marks that are at least 40. Use continue to skip marks below 40.

# Test cases

# Input Expected output

# 25 40 75 32 90 40 75 90 10 20 30 No marks printed 40 40 40 40 40 40
marks = list(map(int, input().split()))

for mark in marks:
    if mark < 40:
        continue
    print(mark, end=" ")



# B3. Think Carefully --- Challenging
# Q15. continue Does Not Skip the Whole Loop
# Predict the output.

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)
# Which lines are skipped when i == 2?
# A 1
# B 1
# A 3
# B 3
# A 4
# B 4
# Q16. Fix the Infinite Loop
# The following program does not finish. Rewrite it so that it skips 3 and prints 1, 2, 4, and 5.

# n = 0

# while n < 5:
#     if n == 3:
#         continue
#     n += 1
#     print(n)
# Expected output after correction

# 1
# 2
# 4
# 5
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)


# Q17. Count Non-Vowel Characters
# Take a word and count how many characters are not vowels. Use continue to skip vowels.

# Test cases

# Input Expected output

# education 4 rhythm 6 apple 3

# For this question, treat a, e, i, o, and u as vowels.
word = input()
count = 0

for ch in word:
    if ch in "aeiou":
        continue
    count += 1

print(count)


# Section C --- Practice Problems on for-else
# A loop's else block runs if the loop finishes normally without executing break. It also runs when the iterable is empty.

# C1. Output Prediction --- Easy
# Q18. Normal Completion
# Predict the output.

# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")
# Output
# text:-
# 1
# 2
# 3
# Done


# Q19. Completion After continue
# Predict the output.

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")
# output:-
# 1
# 3
# 4
# Completed


# Q20. Completion After break
# Predict the output.

# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside loop")
# output;-
# 1
# 2
# Outside loop

# Q21. Empty Iterable
# Predict the output.

for item in []:
    print("Inside")
else:
    print("Else block")
#    output:-
    # Else block

# C2. Write a Program --- Medium
# Q22. Search for a Number
# Take a list of integers and a target number. If the target exists, print "Found". Otherwise, print "Not found" using for-else.

# Test cases

# List Target Expected output

# 4 8 12 16 12 Found 3 6 9 5 Not found 7 7 7 7 Found
numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for num in numbers:
    if num == target:
        print("Found")
        break
else:
    print("Not found")

# Q23. Check Whether a Character Exists
# Take a string and a target character. Use for-else to print "Character exists" if found, or "Character missing" otherwise.

# Test cases

# String Target Expected output

# programming g Character exists computer z Character missing a a Character exists
text = input("Enter a string: ")
target = input("Enter a character: ")

for char in text:
    if char == target:
        print("Character exists")
        break
else:
    print("Character missing")

# Q24. Find the First Divisor
# Take a positive integer n greater than 1. Search for a divisor from 2 through n - 1. If a divisor is found, print "Not prime" and stop. If the loop finishes without finding one, print "Prime" using for-else.

# Test cases

# Input Expected output
#   `7` `Prime`
#  `12` `Not prime`
#   `2` `Prime`
# Assume the input is always an integer greater than or equal to 2.
n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

# Q25. Trace the else
# Predict the output.

values = [2, 4, 6, 8]

for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")
    # output:-
# All are even

# Q26. Does else Run?
# For each case, state whether the loop's else block runs and explain why.

# Case A

for x in range(3):
    continue
else:
    print("A")

# Output:

# text
# A

# Case B

for x in range(3):
    break
else:
    print("B")
    # No output.
# Case C

for x in range(0):
    print(x)
else:
    print("C")
# Output:

# text
# C


# Q27. Find the First Repeated Character
# Given a string, scan each character and check whether it appears again later in the string. Stop at the first character that meets your chosen repeated-character rule and print it. If no character repeats, use for-else to print "No repeated character".

# Test cases

# Input Expected output

# lamp No repeated character level l abcded d

# Rule: A character is considered repeated if it occurs at least twice in the string. Scan characters from left to right and report the first character whose total frequency is at least two.
text = input("Enter a string: ")

for char in text:
    if text.count(char) >= 2:
        print(char)
        break
else:
    print("No repeated character")


# Section D --- Practice Problems on pass
# The pass statement performs no action. It is useful as a placeholder when Python requires a statement but the programmer has not implemented the block yet.

# D1. Output Prediction --- Easy
# Q28. pass Inside a Loop
# Predict the output.

for i in range(1, 4):
    if i == 2:
        pass
    print(i)
#     Output:

# text
# 1
# 2
# 3

# Q29. Empty if Block
# Predict the output.

x = 10

if x > 5:
    pass

print("Finished")
# Output:

# text
# Finished

# Q30. pass in a Loop Body
# Predict the output.

for letter in "cat":
    pass

print("Loop ended")
# Output:

# text
# Loop ended

# D2. Write a Program --- Medium
# Q31. Create a Placeholder for Future Work
# Write a program with a for loop from 1 to 5. Inside the loop, use pass when the number is even. Print every number after the conditional block.

# Test cases

# Input range Expected output

# 1 to 5 1 2 3 4 5 1 to 3 1 2 3

# Explain why the even numbers are still printed.

for number in range(1, 6):
    if number % 2 == 0:
        pass
    print(number)

# Q32. Incomplete Menu Option
# Write a simple menu-like program using if / elif / else. For one option, put pass as a temporary placeholder. Print "Program closed" after the conditional structure.

# Test cases

# Choice Expected output
#    `1` The message for option 1, then `Program closed`
#    `2` No action for option 2, then `Program closed`
#    `9` The message for an unknown option, then `Program closed`
# Choose and clearly document the messages for options 1 and 9.
choice = int(input("Enter your choice (1, 2, or 9): "))

if choice == 1:
    print("You selected Option 1")
elif choice == 2:
    pass
else:
    print("Unknown option")

print("Program closed")

# D3. Think Carefully --- Challenging
# Q33. Compare pass and continue
# Predict the output of each program.

# Program A

for i in range(1, 5):
    if i == 3:
        pass
    print(i)
#     Output:

# text
# 1
# 2
# 3
# 4
# Program B

for i in range(1, 5):
    if i == 3:
        continue
    print(i)
# Output:

# text
# 1
# 2
# 4
# Explain the difference.

# Q34. Complete the Skeleton
# Fill in the blank with exactly one of break, continue, or pass so the output is 1 2 4 5.

for i in range(1, 6):
    if i == 3:
    
     print(i)
# 1
# 2
# 4
# 5
# Explain why the other two choices do not produce the required output.

# Section E --- Mixed Challenge Questions
# These questions combine two or more concepts. Read the indentation carefully.

# Q35. Output Prediction
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")
#     Exact output
# text
# 1
# 3
# Write the exact output and explain why else does or does not run.

# Q36. Search and Report
# Write a program that searches for a target number in a list.

# Skip negative numbers using continue.
# Stop when the target is found using break.
# Use for-else to print "Target not found" if the loop finishes without finding the target.
# Test cases

# List Target Expected output

# -2 4 7 9 7 Target found -5 -1 3 6 8 Target not found 2 4 6 2 Target found
numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for num in numbers:
    if num < 0:
        continue

    if num == target:
        print("Target found")
        break
else:
    print("Target not found")

# Q37. Skip, Stop, or Complete?
# Write a program that reads integers from a list in order:

# Skip 0 using continue.
# Stop before printing -1 using break.
# If the loop finishes without encountering -1, print "All values processed" using for-else.
# Test cases

# Input Expected output

# 2 0 4 -1 8 2 4 0 3 5 3 5 followed by All values processed -1 2 3 No numbers printed and no completion message
numbers = list(map(int, input("Enter integers: ").split()))

for num in numbers:
    if num == 0:
        continue
    if num == -1:
        break
    print(num)
else:

# Q38. Understand Nested Loops
# Predict the output.

 for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")
# Answer these questions: 1. Which pairs are printed? 2. Which inner loops finish without break? 3. Does the inner loop's else run for every row?
# Exact output
# text
# 1 1
# 1 3
# Inner loop completed
# 2 1
# 2 3
# Inner loop completed

# Q39. Find the First Number Divisible by Both 4 and 6
# Given a list of integers, find the first number divisible by both 4 and 6. Skip negative numbers using continue. Stop when a matching number is found using break. Use for-else to report when no matching number exists.

# Test cases

# Input Expected output

# -3 8 12 24 Found: 12 5 7 10 14 No matching number -12 6 18 No matching number
numbers = list(map(int, input("Enter integers: ").split()))

for num in numbers:
    if num < 0:
        continue

    if num % 4 == 0 and num % 6 == 0:
        print("Found:", num)
        break
else:
    print("No matching number")


# Q40. Explain the Best Statement
# For each situation, choose the most suitable option: break, continue, for-else, or pass. Some situations may need more than one.

# Stop searching immediately after finding a username.
# Skip a blank string and process the remaining strings.
# Display "Not found" only when a search loop finishes without finding a match.
# Keep an unfinished function syntactically valid while its implementation is planned.
# Skip the current number but keep processing later numbers.
# Stop a loop when a user enters a sentinel value.
# Report that all items were checked, provided no match caused an early stop.
# Temporarily leave a conditional block empty without causing a syntax error.


# def future_function():
#     pass

# if x > 0:
#     pass