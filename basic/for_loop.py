# the for loop works based on a Iterable object
# Iterable object is capable of returning values one at a time

# regular for loop
for i in range(5):
    print(i)

for i in [1, 3, 5, 7]:
    print(i)

for c in 'Hello':
    print(c)

for i in [(1,2), (3,4), (5,6)]:
    print(i)

# unpack the turple
for i, j in [(1,2), (3,4), (5,6)]:
    print(i, j)

# loop through a dict
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for k in d.keys():
    print(f'{k} -> {d.get(k)}')

for k, v in d.items():
    print(k, ':', v)

# sometime we need to have a logical index of iterm from an Iterable
# we can use 'enumerate' function
for i, c in enumerate('Hello World!'):
    print(i, c)