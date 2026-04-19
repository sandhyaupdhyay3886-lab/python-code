#A small shop sells 5 items. You need to create a program that acts as a POS (Point of Sale) system.Tasks:
#The Database: Create a dictionary called menu where keys are item names (e.g., "Samosa", "Tea", "Coffee") and values are their prices.
#The Shopping List: Create an empty list called cart.
#The Input Loop: Use a while loop to ask the user to type an item name to add to their cart. Type "done" to stop.
#Validation: If the user types an item not in the menu, print "Item not available."
#The Bill: After "done" is typed, loop through the cart list. For each item, look up its price in the menu dictionary and calculate the total sum.
#inal Output: Print a "Receipt" showing the items bought and the final total price.
# 1. Menu (Database)
menu = {
    "Samosa": 10,
    "Tea": 15,
    "Coffee": 20,
    "Burger": 50,
    "Sandwich": 40
}

# 2. Cart (Shopping List)
cart = []

# 3. Input Loop
while True:
    item = input("Enter item name (type 'done' to finish): ")

    if item.lower() == "done":
        break

    # 4. Validation
    elif item in menu:
        cart.append(item)
        print(item, "added to cart\n")
    else:
        print("Item not available\n")

# 5. Bill Calculation
total = 0

print("\n----- RECEIPT -----")

for item in cart:
    price = menu[item]
    print(item, ":", price)
    total += price

# 6. Final Output
print("-------------------")
print("Total Amount =", total)