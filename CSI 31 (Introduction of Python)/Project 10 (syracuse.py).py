#CSI31 Sabina.Akter  Syracuse.py
#This program print out the Syracuse sequence for any natural number.

def main():
    print("This program print out the Syracuse sequence for any natural number.")
    x = eval(input("Please enter any natural number."))
    print("Syracuse starting with 5 is: ")
    print("5")
    while x != 1:
             
        if x%2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        print(int(x))
  
        
main()
"""
This program print out the Syracuse sequence for any natural number.
Please enter any natural number.5
Syracuse starting with 5 is: 
5
16
8
4
2
1
"""

    
    













    

    
