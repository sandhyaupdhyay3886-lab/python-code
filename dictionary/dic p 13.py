#Given a dictionary of items and prices, find and print the name of the cheapest item.
items={"pen":5,
       "book":50,
       "bag":100
}
cheapest =min(items,key=items.get)
print("cheapest item is :",cheapest)