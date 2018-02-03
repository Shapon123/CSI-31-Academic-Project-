# CSI 31  Sabina Akter  slope.py
# This program calculates the slpoe of a line through two(non-vertical)points by the user

import math
def main():

    (x1,y1) = eval(input("enter 2 points seperated by commas: "))
    (x2,y2) = eval(input ("enter 2 points seperated by commas: "))
    #y2 = eval(input("enter y2: "))
    #x1 = eval(input("enter x1: "))
    #x2 = eval (input("enter x2: "))
    while x1==x2:
        
        print("Two x points can not be same")
        y1,y2,x1,x2 = eval(input ("enter 2 points seperated by commas: "))

    slope = (y2-y1)/(x2-x1)
    print("slope of the point (",x1,",",y1,")","and (",x2,",",y2,")","is",round(slope,2))

main()
"""
enter 2 points seperated by commas: 4,5,6,7
slope of the point ( 6 , 4 ) and ( 7 , 5 ) is 1.0
"""
    
                    

    
