#Given a dictionary with some duplicate values, find a way to print all the unique values.
dict={"a":10,"b":20,"c":10,"d":40}
unique=set(dict.values())
print(unique)