#Name-Sandhya Upadhyay
#Roll no-81
#list Assignment Exersice
 #Take a list like [-5, 3, -2, 8]. Create a new list where all negative numbers are converted to positive.
number=[-5,3,-2,8]
new_list=[]
for i in number:
    if i<0:
        i=-i
        new_list.append(i)
        print(new_list)


