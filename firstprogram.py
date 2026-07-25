import sys

side1 = int(input("enter the side"))
side2 = int(input("enter the side"))
side3 = int(input("enter the side"))
if side1 == 0 or side2 == 0 or side3 == 0:
    print("does not exist")
    sys.exit()

if side1>side2 and side1>side3:
    greatest=side1
else:
    a = side1

if side2>side1 and side2>side3:
    greatest = side2
else:
    b = side2

if side3>side1 and side3>side2:
    greatest= side3

if side1==greatest:
    a=side3
if side2==greatest:
    b=side3

import sys
if side1==side2==side3:
    print("equivalent triangle")
    sys.exit()
else:
    c=greatest

import sys
if a**2 +b**2==c**2:
    print("right angled triangle")
    sys.exit()
# if a==b==c:
#     print("equivalent triangle")

if a==b!=c:
    print("isoceles triangle")

# if a==0 or b==0 or c==0:     should be in the first
#     print("triangle does not exist")

if a!=b!=c:
    print("triangle exist")