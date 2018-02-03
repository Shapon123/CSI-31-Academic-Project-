#CSI 31 Sabina.Akter wc.py
#This program determines the number of lines,words and characters in a file

def main():
    print("This program determines the number of lines,words and characters in a file.") 

    # Count words
    fname = input("Enter file name:")
    infile = open(fname,'r')
    data = infile.read()

    print(data)
    words = data.split()
    length = len(words)
    print(fname, "has",length, "words. ")

    # Count lines
    count = data.splitlines()
    print("This file has",len(count),"lines.")

    # count characters
    characters = len(data)
    print("This file contains",characters,"characters.")

main()
"""
This program determines the number of lines,words and characters in a file.
Enter file name:wc.txt.txt
The Thinker
 
THE HOUSE in which Seth Richmond of Winesburg lived with his mother had been at one time the show place of the town,
 but when young Seth lived there its glory had become somewhat dimmed. The huge brick house which Banker White had 
built on Buckeye Street had overshadowed it. The Richmond place was in a little valley far out at the end of Main 
Street. Farmers coming into town by a dusty road from the south passed by a grove of walnut trees, skirted the Fair 
Ground with its high board fence covered with advertisements, and trotted their horses down through the valley past 
the Richmond place into town. 
wc.txt.txt has 112 words. 
This file has 8 lines.
This file contains 626 characters.
"""
    


   
    
