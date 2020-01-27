# accumulate function takes the accumulation of the list
# at every index of the list
# the accumulation is bydefault addition
# but by importing the operators
# we can pass the second arg as operator.mul

from operator import mul
from itertools import accumulate

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n\nThe list is - \n")
print(numbers)

acc = list(accumulate(numbers, mul))
print("\n\nThe accumulated multiply result is -\n")
print(acc)