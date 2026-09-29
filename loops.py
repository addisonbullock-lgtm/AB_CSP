# AB, Loops Notes
import random

#1:startpoint
#2:stp point boolean statement
#3:increase iterater

count = 1

while count <= 10:
    print(count)
    count += 1

ducks= 1
goose= random.randint(1,11)
while True:
    if ducks == goose:
        breaks
    print("Duck....")
    ducks += 1 #ducks= ducks + 1
print("GOOSE!!!!")

#Complex Data Type= holds other data in it
siblings= ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]
peint(siblings[2])
name= input("What is your name: ")
siblings.append(name)# <=1 adds the item to the end of the list
siblings.insert(3, "Vienna")
print(siblings)
#Remove from a list
siblings.pop() # <= if no number given pop removes the last item
print(siblings)

#print each item in a list
for sibling in siblings:
    print(sibling)


#For Loops
for num in range(1,25):
 if num % 15 == 0:
    print("FizzBuzz")
 elif num % 3 == 0:
    print("Fizz")
 elif num % 5 == 0:
    print("Buzz")
else:
    print(num)