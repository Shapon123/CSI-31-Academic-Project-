#CSI31 Sabina.Akter  Uidpassword.py


#This program ask the user for his/her userid and password.
#This program also tests the given userid and passward against a file of userids and passwords up to three attemps to get it correct.

def intro():
    print("This program ask the user for his/her userid and password.")
    print("\nThis program also tests the given userid and passward against a file of userids and passwords up to three attemps to get it correct.")

def getInfo():
    Uid = input("Please enter your user id: ")
    if (len(Uid)) == 0:
        print("Userid is empty: ")
    
    Upass = input("Please enter your password: ")
    if (len(Upass)) == 0:
        print("User password is empty: ")
    

    return Uid, Upass

def checkFile(Uid, Upass):
    infile = open("unames_passwords.txt",'r')   #variable used to access file

    uidupassword = {}
    
    for line in infile:
        eachline = line.split() #splits the line in two by spaces
        key = eachline[0]       #saves the value of Uid
        value = eachline[1]     #saves the value of the Upass

        uidupassword[key]=value
    infile.close()
    if (Uid in uidupassword.keys()):    #checks 
        
        if (uidupassword[Uid] == Upass):
            return True    
            #username and pass are correct according to uidupassword
           

        else:
           
            return False
    else:
        
        return False

    

def main():
    count = 0
    intro()
    while count < 3:    
    
        uid, upassword = getInfo()
        infile = checkFile(uid,upassword)
        if (infile == True):
            print("Welcome' You loged in successfully: ")
            break
        else:
            count = count + 1
            if count <=2:
                print("Your uid or upassword is incorrect, try again: ")
            else:
                print("You tried three times with wrong uid or upassword, So your account is locked, Please ask help from your administrator: ")
            
    
    
    
