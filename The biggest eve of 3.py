x=int(input("type x value "))
y=int(input("type y value "))
z=int(input("type z value "))


if x>y and x>z and x%2==0:
    print(x)
elif y>x and y>z and y%2==0:
    print(y)
elif z>x and z>y and z%2==0:
    print(z)
elif z==x and z==y and x%2==0 and y%2==0 and z%2==0:
    print ("all numberes are equal")
else:
    print ("no one even number entered")