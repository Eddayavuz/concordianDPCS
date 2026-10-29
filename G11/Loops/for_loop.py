# Let's write a function to calculate the sum from 0 to another number.
 
# COUNT CONTROLLED LOOP: for
def sum_of_nums(num):
    total = 0
    for i in range(num + 1):
        total = total + i
    return total
 
print("total:", sum_of_nums(5))
 
# Let's write a function where we count the number of 't's in a sentence.
# COUNT CONTROLLED LOOP: for
sentence = "Concordian students are the best."
 
def num_of_ts(sentence):
    count = 0
    top = len(sentence)
    for i in range(top):
        if sentence[i] == "t":
            count += 1
    return count
 
print("number of t's:", num_of_ts(sentence))
 
# Let's write a function to check whether an item exists in a shopping list and
# returns a message
# FOR LOOP OVER A LIST: goes through every item in the list
def look_up_item(shopping_list, new_item):
    for item in shopping_list:
        if item == new_item:
            return "item exists"
    return "no such item"
 
print(look_up_item(["eraser", "pen", "ruler"], "ruler"))
 
