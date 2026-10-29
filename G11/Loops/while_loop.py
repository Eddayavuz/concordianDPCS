# Let's write a program to sum up numbers until the total reaches 100 or more
# CONDITION CONTROLLED LOOP: while
total = 0

while total < 100:
    num = int(input("enter a num "))
    total += num

print(total)

# Let's write a program that accepts grades until the user inputs -1 and returns the average
# SENTINEL CONTROLLED LOOP: while

total = 0
count = 0
grade = int(input("enter grade "))

while grade != -1:
    total += grade
    count += 1
    grade = int(input("enter grade "))

avg = total / count # Do you see anything suspicious in this line?
print("average", avg)



# SENTINEL + COUNT CONTROLLED LOOP: while
# A bubble tea can have up to 3 toppings. But the customer can type done to stop early.
price = 4
toppings = 0

topping = input("Add a topping (or type done): ")
while topping != "done" and toppings < 3:
    toppings += 1
    price += 1
    print("Added", topping)
    if toppings < 3:
        topping = input("Add a topping (or type done): ")

print("You ordered", toppings, "toppings. Total:", price)
