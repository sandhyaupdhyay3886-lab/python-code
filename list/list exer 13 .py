#Name-Sandhya Upadhyay
#Roll no-81
#list Assignment Exersice
#Create a list of ages. Create two new lists: minors (under 18) and adults (18 and above)
#Store prices of 5 items in a list. Calculate the total bill and the average price per item.
ages = [12, 25, 17, 19, 30, 15, 18]

minors = []
adults = []

for age in ages:
    if age < 18:
        minors.append(age)
    else:
        adults.append(age)

print("Minors:", minors)
print("Adults:", adults)