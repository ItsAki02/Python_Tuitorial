#import math as m
#from math import cos, sin, pi
'''from math import *

print(cos(3.1))
print(sin(0))
print(pi)'''

#user-defined functions

'''def greet(name,dish):
    print('Good morning,', name)
    print('Please eat',dish)
greet('Akanksha','Pizza')'''

def sum_of_list(a):
    print('Calculating....')
    return sum(a)

marks = [45, 16, 87, 98, 45]
sum_of_marks = sum_of_list(marks)

print('my sum of marks', sum_of_marks)