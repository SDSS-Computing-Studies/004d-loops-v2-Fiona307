#! python3

number = input("Enter an inetger that is smaller than 10")
x = int(number)
a = 0
b = 1

for i in range(1,x):
    a = a + b
    b = (10*b) + 1

print("the sum of the series is " + str(a+b))