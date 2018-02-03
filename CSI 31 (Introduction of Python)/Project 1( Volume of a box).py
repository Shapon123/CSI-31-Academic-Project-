#CSI 31  Sabina Akter  volume.py
#This program calculates the volume of a box.

def main():
    print("This program calculates the volume of a box.")
    print()
    L,W,H = eval(input("please enter the length,width and height seperated by commas: "))
    print()
    volume = (L * W * H)
    print("The volume of a box having a length,width and height respectively equal to ",L,",",W,"and,,",H, "is", round(volume,4))
main()

"""
This program calculates the volume of a box.

please enter the length,width and height seperated by commas: 10,24,12

The volume of a box having a length,width and height respectively equal to  10 , 24 and,, 12 is 2880
"""
