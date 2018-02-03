#CSI 31  Sabina Akter  Avg.py
#This program calculates the average of n integers
def main():
    print( "This program computes the average of n integers. ")
    print()
    n = eval(input("How many? "))
    sum = 0
    for i in range(n):
        a = eval(input("Enter a number? "))
        sum = sum + a

    avg = sum/n
    print()
    
    print("The average is", round(avg,4))

main()
"""
This program computes the average of n integers. 

How many? 4
Enter a number? 10
Enter a number? 2
Enter a number? 3
Enter a number? 5

The average is 5.0
"""

