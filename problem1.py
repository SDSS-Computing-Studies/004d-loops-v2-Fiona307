#! python3

width = input("Enter the width of a box")
height = input("Enter the height of a box")
w = int(width)
h = int(height)

for i in range(1,h+1):
    print("*"*w)