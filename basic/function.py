# built-in functions are functions already inclluded in Python standard library
l = len('This is a built-in function in Python')
print(l)

print(type(l))

print(sorted([1, 3,2, 5,8,6,9,0]))

# user-defined functions are functions that are not built-in in Python standard library

# when a function is defined, Python just only create the metadata for the function,
# it has NOT validate or execute the function yet until the function is actually called/ or executed
def func_1():
    print('This is from inside func_1')
    # call func_2, even func_2 hs NOT been defined yet
    func_2()

def func_2():
    print('This is from inside func_2')

# until we call func_1, then anything iside func_1 will be evaluated and executed
# in this case, all's good
func_1()

# but if we call a function before it is defined, Python will throw exception
def func_3():
    print('This is func_3')
    func_4()

# we got error: NameError: name 'func_4' is not defined if we call func_3 here (before func_4 is defined)
#func_3()

def func_4():
    print('This is func_4')


# very important - function is just an object like any other object in Python
# in fact, any function is just an object of class 'function'
print(type(func_1))

# we can assign/store the function itself to a variable like other objects like string or integer
f = func_1

# then, we can call func_1 by calling variable f
f()


# lambda functions are just normal function, but is defined very condensed in single logical line and has no name
# lambda function takes an input and return an output
# in the lambda function below, it takes x param as input and return x * x
square = lambda x : x*x

# it's just a function like any other function
print(type(square))

# execute it
print(square(3))