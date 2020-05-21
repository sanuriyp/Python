
print("To encode the message Please enter the e")
print("To quit from the programme enter q")
commands=['e','q',]
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #list of alphabet
Uinput=''

while Uinput!='q': #check until q
    Uinput=input("Enter the command you want to do:") #user input for command
    Uinput=Uinput.lower()#conver command into lowercase
    def encode():#do the encode
        #get the message and key value from the user
        key=1
        msg=str(input("Enter the message:"))#prompt for message
        
        while True:   
          try: #check the input key value is integer
            key=int(input("You have to give key value range in 1-26\nEnter the value of key:"))#prompt for key
            if key>0 and key<26: #check the key between in 1-26
               def ceaserShift(msg): #define function to rotate the characters
                     
                     encoded_message='' #initialize a empty string for add charaters after encode 
                     for ch in msg:     #check until charater in input message
                            if ch in alpha:  #finding character in alphabet
                                #"finding index position of charater in alphabet then add the key value and get the mod ,then get new index position  "  
                               encoded_message+=alpha[(alpha.index(ch)+key)%(len(alpha))]#"and add character related to that index position to encoded_message string" 
                            else:
                               encoded_message+=ch # "if charater not in alpha then add that charater to encoded_message string without change "
                     return encoded_message
               def main(): #user define for output
                 encoded_message=ceaserShift(msg)
                 print("Orginal message:\t",msg)
                 print("Encrypted message:\t",encoded_message)
               main()
               break
            else:
                  print("You entered out of range")
                 
          except:
             print("you entered wrong syntax")
    if Uinput=='e':  #check the command is e
        encode()
    elif Uinput not in commands: #check the command is in commands list
      print("You entered wrong command.Please enter the currect command")
else:
    print("You entered to quit from the programme.")

