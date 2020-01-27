# chain allows us to go through
# all of the iterables that are chained together

from itertools import chain

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4, 5]
names = ['Tokyo', 'Berlin']

combine = list(chain(letters, numbers, names))
print(combine)
