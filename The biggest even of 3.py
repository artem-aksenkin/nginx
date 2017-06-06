# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x=int(input("type x value "))
y=int(input("type y value "))
z=int(input("type z value "))

if x%2==0:
    if y%2==0:
        if z%2==0:
            if x>y and x>z:
                print(x)
            elif y>z and y>x: 
                print(y)
            elif z>x and z>y:
                print(z)
        else: 
            print("z is not even number")
            if x>y:
                print(x)
    else:
        print ("y is not even number")
        if x>z:
            print(x)
else:
    print("x is not even number")
    if y>z:
            print(y)


