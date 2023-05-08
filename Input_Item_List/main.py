grocery_list = []

more_items = True 

while more_items:
    print()
    grocery_item = input ("Grocery item to add to the list? > ")
    grocery_list.append(grocery_item)
    print()
    keep_adding_items = (input("Do you want to add more items? (y or n) ")).lower()
    
    if keep_adding_items != 'y':
        more_items = False

print()
print("The Items on the grocery list are:")

for item in grocery_list:
    print(item)