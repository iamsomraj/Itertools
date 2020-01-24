# combination is a selection of items where the order does not matter
# picking a team of virat and rohit or rohit and virat - both are same

from itertools import combinations

print("The players available are - ")
letters = ['a', 'b', 'c', 'd']
print(letters)
comb = combinations(letters,2)
print("\nThe teams of 2 mates are as follows - \n")
print(list(comb))