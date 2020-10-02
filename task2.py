#! python3

name = input("Enter a name")
namelist = ("Lebron","Kobe","Michale","Shaq","Dennis")

for i in namelist:
    if i == name:
        print("That name is on the list")
        break
if i != name:
        print("That name is not on the list")
