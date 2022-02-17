# regular try/except
# anything in try block is executed until any Exception occurs
# then that exception will be catched in one of the except blocks
try:
    a = input('Enter a number: ')
    b = input('Enter a number: ')
    
    c = int(int(a) / int(b))

    print(f'{a}/{b}={c}')
except ZeroDivisionError as ex:
    print(f'Cannot devide by {b}')
except ValueError as ex:
    print(f'Cannot convert entered value {a} or {b} to number')
finally:
    print('This is the end of the statement')

# the finally block is always executed weather or not the try block has exception
# even if in a loop and we put a break or continue when an exception is caught
while True:
    try:
        a = input('Enter a number: ')
        b = input('Enter a number: ')
        
        c = int(int(a) / int(b))

        print(f'{a}/{b}={c}')
    except ZeroDivisionError as ex:
        print(f'Cannot devide by {b}')
        continue
    except ValueError as ex:
        print(f'Cannot convert entered value {a} or {b} to number')
        break
    finally:
        print('This is the end of the statement')
