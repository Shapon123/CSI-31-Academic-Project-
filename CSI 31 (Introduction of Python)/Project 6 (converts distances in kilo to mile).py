#CSI31  Sabina Akter  convert.py
#A program to converts distances measured in kilometers to miles

def intro ():
    print("This program converts kilometer to miles.")
    print()
    return

def main():
    intro()
    k = eval(input(" What is the distance in kilometers?"))
    m= 0.62* k
    print()
    print("The distance is ",m,"miles")
        
main()
"""
This program converts kilometer to miles.

 What is the distance in kilometers?200

The distance is  124.0 miles
"""
