# itertools.cycle function takes an arguement of iterator
# then it just cycles over the iterator
# by using the next method we can fetch the same elements over and over again

from itertools import cycle

print("\nThe list is - \n")
numbers = [100, 200, 300, 400, 500]
print(numbers)
number_iterator = cycle(numbers)
print("\n\nThe Cycle Iterator is printed 20 times below :\n")
for i in range(20):
    print(next(number_iterator))
