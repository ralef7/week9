import random

def sort(items):
  # 1. TO DO: Implement a "bubble sort" routine here
  for position in range(len(items)-1,0,-1):
    for i in range(position):
      if items[i] > items[i+1]:
        temp = items[i]
        items[i] = items[i+1]
        items[i+1] = temp
  return items

numbers = list(range(10))
random.shuffle(numbers)


assert list(range(10)) == sort(numbers)
print("The list was sorted correctly!")

# 2. Change this print statement to display the complexity category.
#    Refer to the cheat sheet in week9-class for examples.
print("This algorithm is classified as: O(n^2)")
