# q1
choice = 2

match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Pasta")
    case _:
        print("Sandwich")

#q2
choice=2

match choice:
        case 1:
            print("wi-Fi")
        case 2:
            print("Blutooth")
        case 3:
            print("Mobile Data")
        case 4:
            print("Airplane made")    
        case 5:
            print("Exit")
        case 6:
            print("Invalid setting")

# q3
choice=4
match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw Money") 
    case 3:
        print("Deposite Money") 
    case 4:
        print("Change PIN ")
    case _:
        print("Exit")

# q4
choice = (input("Enter choice colour:red, yellow, Green,other "))

match choice:
    case "red":
        print("stop")
    case "yellow":
        print("Wait")
    case "Green":
        print("Go")
    case _:
        print("For any other colour")

# q5
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You selected View Profile.")
    case 2:
        print("You selected View Courses.")
    case 3:
        print("You selected View Marks.")
    case 4:
        print("You selected View Attendance.")
    case 5:
        print("Logged out successfully.")
    case _:
        print("Invalid choice. Please select 1-5.")

#q6
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Electronics")
    case 2:
        print("Clothing")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")

# Q7
choice=int(input("Enter a statement"))
match choice:
    case 1:
        print("Account Balance")
    case 2:
        print("Mini Statement")
    case 3:
        print("Fund Transfer")
    case 4:
        print("Bill Payment")
    case _:
        print("Customer Support")

#q8
choice=int(input("Enter a show"))
match choice:
    case 1:
            print("Morning Show")
    case 2:
            print("Afternoon Show")
    case 3:
            print("Evening Show")
    case _:
            print("Night show")

#q9
choice=(input("Enter a season : ,sunny, rainy,cloudy, snowy"))
match choice:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy":
        print("Wear warm clothe")

# Q10
choice=int(input("Enter a mathod of payment no:"))
match choice :
    case 1:
        print("UPI Payment method selected")
    case 2:
        print("Cash Payment method selected")
    case _:
        print("wallet Payment method selected")

# q11
choice=(input("Enter a extention pdf ,jpj, png , mp3,mp4:"))
match choice:
    case "pdf":
        print("Document")
    case "jpg":
        print("Image")
    case "png":
        print("Image")
    case "mp3":
        print("Audio")
    case "mp4":
        print("Video")
    case _:
        print("Invalid case")

#q12
role =input("Enter a role :Admin, Teacher, Student,Guest,For unkonwn ")
match role:
    case "Admin":
        print("Full Access")
    case "Teacher":
        print("Teacher Dashboard")
    case"Student":
        print("Student Dashboard")
    case"Guest":
        print("Limited Access")
    case _:
        print("Invalid Role")

# q13
day=input("Enter a Week days :-,""Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
"Sunday:-")
day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")

# q14
service=int(input("Enter a priority""low""Medium""High""Critical:-  "))

match service:
    case 1|2:
        print("normal ")
    case 3|4:
        print("Urgent")
    case 5:
        print("invalid")

#q15
level = int(input("Enter membership level (1-4): "))

if level == 1 or level == 2:
    print("Basic Membership")
elif level == 3 or level == 4:
    print("Premium Membership")
else:
    print("Invalid membership level")



