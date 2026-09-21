

# IPO 

# INPUT 
# Read price of an item 

# PROCESSING 
# Create a discount variable and assign 0 value to it.
# If price is greater than or equal to 2000,
# Give 20% discount and subtract it from original price 
# otherwise discount = 0

# OUTPUT
# Display the final price

# Algorithm
# 1. Start 
# 2. Read price of an item
# 3. Create a discount variable and assign 0 value to it
# 4. If price is greater than or equal to 2000
# 5. Update the discount value 
# 6. otherwise keep the discount 0
# 7. Subtract it from original price
# 8. Display the final price
# 9. Stop

# Code
price = float(input("Enter price: "))
discount = 0

if price >= 2000:
    discount = price * 0.2
    price = price - discount
else:
    discount = 0

print(f"Price: {price} ₹")