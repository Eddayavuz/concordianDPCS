# CONDITION CONTROLLED LOOP: while
# Let's write a program to sum up numbers until the total reaches 100 or more
total = 0
while total < 100:
    number = int(input("Enter a number: "))
    total = total + number
print("Total:", total)

# Let's write a program that lets the user try until they get the password correct.
password = "python123"
attempt = input("Enter the password: ")
while attempt != password:
    print("Wrong password, try again.")
    attempt = input("Enter the password: ")
print("Access granted")

# Let's write a program that keeps asking for test scores until the user types -1, then prints the average
total = 0
count = 0
score = int(input("Enter a score (-1 to stop): "))
while score != -1:
    total = total + score
    count = count + 1
    score = int(input("Enter a score (-1 to stop): "))
if count > 0:
    print("Average:", total / count)
else:
    print("No scores entered")
