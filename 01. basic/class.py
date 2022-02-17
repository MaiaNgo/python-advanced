# define a class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(10, 5)
print(r.width, r.height)
print(r.area())

# if we try to convert an object to string
print(str(r))

# we need to implement the dunder str method (__str__)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Rectangle: W={self.width} - W={self.height}'

r = Rectangle(2, 3)
print(str(r))

# compare objects
r1 = Rectangle(2, 4)
r2 = Rectangle(2, 4)

if r1 is not r2:
    print(f'{r1} and {r2} -> are not the same')
else:
    print(f'{r1} and {r2} -> are the same')

if r1 == r2:
    print(f'{r1} and {r2} -> are equal')
else:
    print(f'{r1} and {r2} -> are not equal')

# notice that they are not considered equal even through they have same value in all their properties
# which doesn't make sense
# we fix this my implemnt the __eq__ method
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Rectangle: W={self.width} - W={self.height}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

# compare objects again
r1 = Rectangle(2, 4)
r2 = Rectangle(2, 4)

if r1 is not r2:
    print(f'{r1} and {r2} -> are not the same')
else:
    print(f'{r1} and {r2} -> are the same')

if r1 == r2:
    print(f'{r1} and {r2} -> are equal')
else:
    print(f'{r1} and {r2} -> are not equal')

# now they are equal, but how about other comparision operators like < or >

# There are other dunder methods we need to implement: __lt__ , __gt__
