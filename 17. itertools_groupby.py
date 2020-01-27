from itertools import groupby


people = [
    {
        'name': 'Akbar',
        'age': 22
    }, {
        'name': 'Amar',
        'age': 21
    }, {
        'name': 'Anthony',
        'age': 22
    }, {
        'name': 'Amar Second',
        'age': 22
    }, {
        'name': 'Anthony Second',
        'age': 23
    }
]


def getAge(person):
    return person['age']


grouped = groupby(people, key=getAge)
for key, group in grouped:
    print(key)
    for person in group:
        print(person)
    print()
