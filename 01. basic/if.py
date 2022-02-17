# regular if/else statement
a = 10
if a > 5:
    print('a > 5')
else:
    print('a <= 5')

# if/elif/else
a = 3
if a > 5:
    print('a > 5')
elif a > 0:
    print('a > 0')
else:
    print('a <= 0')

# assignment with if/else - ternary statement
b = 'a is positive' if a >= 0 else 'a is negative'
print(b)
