#! python3

number = input("Enter an integer")
x = int(number)
a = 1
for i in range(1,x+1):
    a = a*i

print(number + "! is " + str(a))