#Name-Sandhya Upadhyay
#Roll no-81
#list Assignment Exersice
runs=[45,60,10,80,55,90]
total=0
highest=runs[0]
count=0
for r in runs:
 total=total+r
if r>highest:
 highest=r
if r>50:
 count=count+1
print("total runs:",total)
print("highest dcore:",highest)
print("matches>50 runs:",count)
