# CSI 31  Sabina.Akter  Quadratic.py
# This program solves any quadratic in standard form

import math
def intro():
    print("This program solves any quadratic in standard form")
    print("ax^2+bx+c = 0")

def getInput():
    a,b,c = eval(input("Enter the values of a, b, c = "))
    while a == 0:
        print(" a can not be zero")
        a = eval(input("a = "))
    return a,b,c

def main():
    intro()
    a,b,c = getInput()
    print()
    print("a = ",a,"b = ",b,"c = ",c)

# Compute the discriminant
    disc = b**2 - 4*a*c
    if disc>=0:

        root1 = (-b + math.sqrt(b**2-4*a*c))/2*a
        root2 = (-b - math.sqrt(b**2-4*a*c))/2*a
        
        print ("\nThe solutions are", round(root1,3),"and",round(root2,3),".")
    
    else:
        print("The solutions of your equation are complex numbers.")

main()
"""
This program solves any quadratic in standard form
ax^2+bx+c = 0
Enter the values of a, b, c = 100,200,300

a =  100 b =  200 c =  300
The solutions of your equation are complex numbers.
"""

