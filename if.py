name = input("enter the name:")
age = int(input("enter your age:"))
if name == 'rahul'and age==25:
    print("name and age are matching")
elif name != 'rahul' and age==25:
    print("age matches")
elif name == 'rahul' and age!=25:
    print("name matches")
else:
    print(" name and ages doesnot matches")
