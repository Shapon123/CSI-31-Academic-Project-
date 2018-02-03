#CSI31 Sabina Akter convert.py
#A program to convert Celsius temps to Fahrenheit

def intro ():
    print("This program converts Celsius tempurature to fahrenheit tempurature.")
    print()
    return

def main():
    intro()
    for i in range(5):
        celsius= eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        print()

        main()
        """
 This program converts Celsius tempurature to fahrenheit tempurature.

What is the Celsius temperature? 10
The temperature is 50.0 degrees Fahrenheit.

What is the Celsius temperature? 20
The temperature is 68.0 degrees Fahrenheit.

What is the Celsius temperature? 30
The temperature is 86.0 degrees Fahrenheit.

What is the Celsius temperature? 40
The temperature is 104.0 degrees Fahrenheit.

What is the Celsius temperature? 50
The temperature is 122.0 degrees Fahrenheit.

"""
