# compress functions take 2 iterators as arguements
# then compress the first iterator based on the corresponding
# true and false values of the second iterator
# it is somewhat similiar to the filter function
# but here we dont need to have a function

from itertools import compress

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
selector = [True, False, False, True, False, True, True, False, True, False]

print("The list is \n\n\n")
print(numbers)
print("The selector is \n\n\n")
print(selector)
compressedList = compress(numbers, selector)
print("The result is \n\n\n")
compressedList = list(compressedList)
print(compressedList)
