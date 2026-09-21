#Question 1
text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

#Question 2
fail = 0 
passed = 0
good = 0
excellent = 0

for i in range(1, 11):
    marks = int(input("Enter marks of student"+ str(i)+ ": "))

    if marks < 35:
        print("fail")
        fail += 1

    elif marks <= 49:
        print("pass")
        passed += 1

    elif marks <= 74:
        print("good")
        good += 1

    elif marks <=100:
        print("Excellent")
        excellent += 1

    else :
        print("Invalid marks")

print("Number of students in each category:~")
print("fail:",fail)
print("pass:", passed)
print("good:", good)
print("Excellent:",Excellent)

#Question 3
sentence = input("Enter a sentence:")
words = sentence.split()

highest_score = 0
highest_word = ""

for word in words:
    score = 0

    for ch in word:
        if ch.lower() in "aeiou":
            score += 2
        elif ch.isalpha():
            score += 1
        elif ch.isdigit():
            score += 3
        else :
            score += 4

    print(word, "=", score)

    if score > highest_score:
        highest_score = score
        highest_word = word

print("Word with highest score:", highest_word)
print("Highest score:", highest_score)

# Question 4

for i in range(5):
    str = input("Enter the Password:~")

    length = len(str) >= 8
    uppercase = False
    lowercase = False
    digit = False
    special = False

    for ch in str:
        if ch.isupper():
            uppercase = True
        elif ch.islower():
            lowercase = True
        elif ch.isdigit():
            digit = True
        else :
            special = True

    score = 0

    if length:
        score += 1
    
    elif uppercase:
        score += 1

    elif lowercase:
        score += 1

    elif digit:
        score += 1

    elif special:
        score += 1

    if score == 5:
        print("Strong")
    elif score >= 3:
        print("Medium")
    else:
        print("Weak")




