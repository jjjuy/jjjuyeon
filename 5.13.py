import math
pi=math.pi

def square(s):
    return s**3

def rectangle(w,h,l):
    return w*h*l

def cone(r,hh):
    return (1/3)*(r**2)*hh*pi

def sphere(rr):
    return (4/3)*pi*(rr**3)

def cylinder(rrr,hhh):
    return pi*(rrr**2)*hhh

print('(1):',square(12))
print('(2):',square(20))
print('(3):',rectangle(3,5,6))
print('(4):',cone(20,10))
print('(5):',sphere(15))
print('(6):',cylinder(20,10))
