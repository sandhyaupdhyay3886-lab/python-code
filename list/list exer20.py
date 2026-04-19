#Name-Sandhya Upadhyay
#Roll no-81
#list Assignment Exersice
runs=[45,60,10,80,55,90]
total=0
highest=runs[0]
for r in runs:
 total=total+r
if r>highest:
 highest=r
 print("total run:",total)
print("highest score:",highest)