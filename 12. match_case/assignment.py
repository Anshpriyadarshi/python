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

# q16
user = input("Enter the specification ,""Teacher"
"Student:~")
user =2
match user:
    case 2:
        print("1- view cources\n 2- view marks\n 3- view Attendence")
    case 1:
        print("1- view student\n 2- Enter marks\n 3- view Attendance")

# q17
account = int(input("Enter account type:~"))
operation = int(input("Enter operation:~"))
match account:
    case 1:
        print("Savings Account")
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")
    case 2:
        print("Current Account")
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")
    case _:
        print("Invalid Account Type")

# q18
catagory = int(input("Enter the catagory:~"))
operations = int(input("Enter the operation:~"))
match catagory:
    case 1:
        print("Electronics")
        match operations:
            case 1:
                print("1.Mobile")
            case 2:
                print("2.Laptop")
            case 3:
                print("3.Headphones")
            case _:
                print("Invalid operation")
    case 2:
        print("clothing")
        match operations:
            case 1:
                print("1.shirt")
            case 2:
                print("2.Jeans")
            case 3:
                print("3.Shoes")
            case _:
                print("Invalid operation")
    case _:
        print("Invalid catagory type")

#q19
category = int(input("Enter the category:~"))
operations =int(input("Enter the operation:~"))
match category:
    case 1:
        print("vegetarian")
        match operations:
            case 1:
                print("1.paneer")
            case 2:
                print("2.dal")
            case 3:
                print("3.veg Biryani")
            case _:
                print("Invalid operation")
    case 2:
        print("Non-vegetarian")
        match operation:
            case 1:
                print("1.chicken Biryani")
            case 2:
                print("2.chicken curry")
            case 3:
                print("3.fish curry")
            case _:
                print("Invalid operation")
    case _:
        print("Invalid category type")

# q20
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator: ")

match operator:
    case "+":
        result = num1 + num2
        print("Result =", result)

    case "-":
        result = num1 - num2
        print("Result =", result)

    case "*":
        result = num1 * num2
        print("Result =", result)

    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print("Result =", result)

    case _:
        print("Invalid operator")

#q21
choice = int(input("Enter choice: "))
temperature = float(input("Enter temperature: "))

match choice:
    case 1:
        fahrenheit = (temperature * 9 / 5) + 32
        print("Temperature =", fahrenheit, "F")

    case 2:
        celsius = (temperature - 32) * 5 / 9
        print("Temperature =", celsius, "C")

    case _:
        print("Invalid choice")

#q22
choice = int(input("Enter choice: "))

match choice:
    case 1:
        age = int(input("Enter age: "))

        if age >= 18:
            print("You can start the exam")
        else:
            print("You cannot start the exam")

    case 2:
        print("View Result")

#q23
ticket_type = int(input("Enter ticket type: "))

match ticket_type:
    case 1:
        ticket = "Regular"
        age = int(input("Enter age: "))

        if age < 5:
            print("Free Entry")
        else:
            print("Regular Ticket")

    case 2:
        ticket = "Premium"
        age = int(input("Enter age: "))

        if age < 5:
            print("Free Entry")
        else:
            print("Premium Ticket")

    case 3:
        ticket = "VIP"
        age = int(input("Enter age: "))

        if age < 5:
            print("Free Entry")
        else:
            print("VIP Ticket")

    case _:
        print("Invalid ticket type")

#24
choice = int(input("Enter choice: "))

match choice:
    case 1:
        age = int(input("Enter age: "))

        if age >= 18:
            print("You can start the exam")
        else:
            print("You cannot start the exam")

    case 2:
        print("View Result")

    case 3:
        print("Exit")

    case _:
        print("Invalid choice")

#q25
device = int(input("Enter device: "))

match device:
    case 1:
        print("Light Controller Opened")

    case 2:
        print("Fan Controller Opened")

    case 3:
        print("AC Controller Opened")

    case 4:
        print("TV Controller Opened")

    case _:
        print("Invalid Device")

#q26
department = int(input("Enter department: "))

match department:
    case 1:
        print("General Medicine")

    case 2:
        print("Cardiology")

    case 3:
        print("Orthopedics")

    case 4:
        print("Pediatrics")

    case 5:
        print("Emergency")

    case _:
        print("Invalid Department")

#q27
department = int(input("Enter department: "))

match department:
    case 1:
        print("General Medicine")

    case 2:
        print("Cardiology")

    case 3:
        print("Orthopedics")

    case 4:
        print("Pediatrics")

    case 5:
        print("Emergency")

    case _:
        print("Invalid Department")

#q28
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Book Ticket selected.")
elif choice == 2:
    print("Cancel Ticket selected.")
elif choice == 3:
    print("Check PNR selected.")
elif choice == 4:
    print("Train Schedule selected.")
elif choice == 5:
    print("Exiting Railway Ticket System...")
else:
    print("Invalid choice.")

#q29
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Search Book selected.")
    case 2:
        print("Issue Book selected.")
    case 3:
        print("Return Book selected.")
    case 4:
        print("View Issued Books selected.")
    case 5:
        print("Exiting Library Management System...")
    case _:
        print("Invalid choice.")

#q30

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Search Book selected.")
    case 2:
        print("Issue Book selected.")
    case 3:
        print("Return Book selected.")
    case 4:
        print("View Issued Books selected.")
    case 5:
        print("Exiting Library Management System...")
    case _:
        print("Invalid choice.")

