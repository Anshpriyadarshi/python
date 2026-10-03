# Match-case basic syntax.
value = 2
match value:
    case 1:
        print("pattern1")
    case 2:
        print("pattern2")
    case 3:
        print("pattern3")
    case _:
        print("default code")

# Question 1
day = 8
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")

# Question 2
n1=int(input("Enter number 1:~"))
n2=int(input("Enter number 2:~"))
choice = int(input("Enter your choice (1-4):~"))
match choice:
    case 1:
        print("Add:~",n1+n2)
    case 2:
        print("Subtract:~",n1-n2)
    case 3:
        print("Multiply:~",n1*n2)
    case 4:
        print("Divide:~",n1/n2)
    case _:
        print("Invalid Choice")

#    or
n=int(input("Enter the day:~"))
match n:
    case 1|2|3|4|5:
        print("weekdays")
    case 6|7:
        print("weekend")
    case _:
        print("invalid day")

#       marks
marks = int(input("Enter the marks:~"))
match marks:
    case x if x >= 90:
        print("A")
    case x if x >= 75:
        print("B")
    case x if x >= 60:
        print("C")
    case x if x >= 40:
        print("D")
    case _:
        print("Fail")

#Question bank account
match account:
    case "saving":
        print("Saving Account")

        choice = input("Enter 1 for Deposit or 2 for Withdraw: ")

        match choice:
            case "1":
                print("Money Deposited")
            case "2":
                print("Money Withdrawn")
            case _:
                print("Invalid choice")

    case "current":
        print("Current Account")

        choice = input("Enter 1 for Deposit or 2 for Withdraw: ")

        match choice:
            case "1":
                print("money deposited")
            case "2":
                print("money withdraw")
            case _:
                print("Invalid choice")

    case _:
        print("please choose a valiid account details")
