# iterables are something that can be looped over
# lists are iterables because we can loop over it
# lists are not iterators

nums = [1, 2, 3, 4]
print("\nList as iterable is printed by for loop : \n")
for number in nums:
    print(number)


# an iterable is an object having the __iter__ method
# if we invoke the __iter__ method, then it returns the iterator


# iterator is an object that returns a state
# so that it can remember where it is currently iterating

# iterator has __next__ method

# if we call next and iter method
# then they automatically invoke the __next__ and __iter__ method

print("\nList as iterator is printed : \n")
iterNums = iter(nums)
print(iterNums)

print("\nNext method on the iterator is invoked three times \n")
print(next(iterNums))
print(next(iterNums))
print(next(iterNums))

# an iterator is also an iterable just because it also has __iter__ method