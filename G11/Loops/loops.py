# Let's write a function to calculate the sum from 0 to another number.

# COUNT CONTROLLED LOOP: for
def sum_of_nums(num):
    total = 0
    for i in range(num):
        total = total + i
    return total

print("total:", sum_of_nums(5))

# Let’s write a program to sum up all the numbers until the total exceeds 100
# CONDITION CONTROLLED LOOP: while
num = 0
total = 0

while total < 100 :
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

avg = total / count
print("average", avg)


# Let’s write a function where we count the number of ‘t’s in a sentence.
sentence = "Concordian students are the best."

def num_of_ts(sentence):
    count = 0
    top = len(sentence)+1
    for i in range(top):
        if sentence[i] == "t":
            count +=1
    return count

# Let's write a function to check whether an item exist in a shopping list and
# returns a message
def look_up_item(shopping_list, new_item):
    for item in shopping_list:
        if item == new_item:
            return "item exists"
    return "no such item"

look_up_item(["eraser", "pen", "ruler"], "ruler")

# Let’s write a program to calculate the total score of a player in a game.
# The user can enter up to 3 scores.

total_score = 0
num_of_scores = 0
score = int(input("enter score "))
while score != -1 and num_of_scores<3:
    total_score += score
    num_of_scores += 1
    if num_of_scores < 3:
        score = int(input("enter score "))
print("total:", total_score)

