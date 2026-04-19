#You have two lists: keys = ['ID', 'Name', 'Salary'] and values = [101, 'Rahul', 50000]. Convert them into a single dictionary
keys={"id","name","salary"}
values={101,"rahul,50000"}
data=dict(zip(keys,values))
print(data)