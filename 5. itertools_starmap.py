# itertools.starmap works like the map function
# but as the map function takes the arguement as it's own arguement
# here starmap takes the arguement of the callback function using list of tuples

from itertools import starmap

print("\nThe list is -\n")
squares = starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)])
squares = list(squares)
print(squares)