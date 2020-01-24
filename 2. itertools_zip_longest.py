# normal zip function ends when the shortest iterable gets exhausted
# but the itertools.zip_longest function goes on till the longest iterable
# it fills the blanks with None

# as itertools.count() goes on forever
# therefore, we will use range

from itertools import zip_longest


print("\nThe list is\n")
numbers = [100, 200, 300, 400]
print("\n{}\n".format(numbers))
print("\nUsing the zip longest with range of 10 elements\n")
# range is longest as it has 10 elements
real_data = zip_longest(range(10), numbers)
real_data = list(real_data)
print("\n{}\n".format(real_data))
