#Create a dictionary inventory = {'Pens': 10, 'Erasers': 5}. Ask the user which item they bought and decrease that item's count by 1
inventory={'pens':10,'erasers':5}
item=input("enter item:")
if item in inventory:
    inventory[item]-=1
    print(inventory)
else:
    print("item not found")