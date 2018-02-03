#CSI31 Sabina Akter convert.py
#A program to convert Celsius temperature to Fahrenheit temperature


def main():
    print("celsius fahrenheit")
    print("------------------")
    for i in range(11):
        celsius = 10*i
        fahrenheit = 9/5 * celsius + 32

        print("{0:10} {1:10}".format(celsius,int(fahrenheit)))
   
main()
"""
celsius fahrenheit
------------------
         0         32
        10         50
        20         68
        30         86
        40        104
        50        122
        60        140
        70        158
        80        176
        90        194
       100        212
"""       
