# repeat returns an iterator with a fixed value or constant
# the first arguement is the constant
# the second value is the number of times

from itertools import repeat

squares = map(pow, range(10) , repeat(2))
print(list(squares))