#Name-Sandhya Upadhyay
#Roll no-81
#list Assignment Exersice
marks=[78,65,89,90,56]
total=0
highest =marks[0]
lowest= marks[0]
for m in marks:
    total=total+m
if m>highest:
 higest=m
if m<lowest:
 lowest=m
average=total/len(marks)
print("marks:",marks)
print("total:",total)
print("average:",average)
print("lowest marks:",lowest)
print("highest marks:",highest)
            