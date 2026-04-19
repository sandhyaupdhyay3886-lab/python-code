#Given a dictionary of employees and their salaries, increase every salary by 10% and update the dictionary
emp={"rohit":50000,
     "mohan":40000,
     "sujeet":30000
}
for name in emp:
 emp[name]=emp[name]*1.10
 print(emp)