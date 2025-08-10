# TASK1: Control Structures in python:

user = int(input("Enter a number: "))
if user%2==0:
    print(f"{user} is an even number.")
else:
    print(f"{user} is an odd number.")


# TASK2: Sum of integers from 1 to 50 Using a loop

x = 0
for i in range(1,51):
    x = x+i

print("The sum of numbers from 1 to 50 is: ", x)
