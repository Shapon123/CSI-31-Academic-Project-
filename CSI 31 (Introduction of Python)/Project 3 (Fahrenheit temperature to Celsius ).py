#CSI31 Sabina Akter convert.py
#A program to convert Fahrenheit temperature to Celsius temperature

def intro ():
    print("This program convert fahrenheit tempurature to Celsius temperature.")
    print()
    return

def main():
    intro()
    for i in range(5):
        fahrenheit = eval(input("What is the Fahrenheit temperature? "))
        Celsius =(fahrenheit-32)*5/9
        print("The temperature is", Celsius, "degrees Celsius.")
        print()

main()
"""
This program converts fahrenheit temperature to Celsius temperature.

What is the farenheit temperature? 33
The temperature is 0.5555555555555556 degrees Celsius.

What is the Fahrenheit temperature? 45
The temperature is 7.222222222222222 degrees Celsius.

What is the Fahrenheit temperature? 66
The temperature is 18.88888888888889 degrees Celsius.

What is the Fahrengeit temperature? 89
The temperature is 31.666666666666668 degrees Celsius.

What is the Fahrenheit temperature? 212
The temperature is 100.0 degrees Celsius.

"""

        
