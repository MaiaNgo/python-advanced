# regular while loop
a = 0
while a < 5:
    print(a)
    a += 1

# while/else statement
a = 0
while a < 5:
    print(a)
    a += 1
else:
    print(f'This is when the while loop end. a = {a}')

# sometime, we want to do the loop first at least once before evaluate the condition to exit the loop
a = 0
while True:
    print(a)
    a += 1
    if a >= 5:
        break


