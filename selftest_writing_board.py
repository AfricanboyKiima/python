foo = []
while True:#an infinite loop to allow one to insert elements into container objects
    item = input("Insert item : ")
    if item == "":
        print("Loop ended")
        break
    if item not in foo:
        foo.append(item)
    
    
