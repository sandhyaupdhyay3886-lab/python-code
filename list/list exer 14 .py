#Name-Sandhya Upadhyay
#Roll no-81
#list Assignment Exersice
##Store prices of 5 items in a list. Calculate the total bill and the average price per item.
prices=[30,50,70,80]
total=0
for i in prices:
 total=total+i
average=total/len(prices)
print("total bill:",total)
print("average price:",average)