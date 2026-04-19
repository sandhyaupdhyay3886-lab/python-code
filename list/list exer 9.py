# Name-Sandhya Upadhyay
#Roll no-81
#list Assignment Exersice
# Write a program that takes a list of names and a "search_name" from the user. Print the index where the name is found, or "Not Found."
name_list=["sandhya","riya","golda","romal"]
search_name=input("enter the name")
if search_name in name_list:
    print("found")
else:
    print("not found")