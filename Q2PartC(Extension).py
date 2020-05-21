print("To encode a string input=\t'e'")
print("To decode a string input=\t'd'")
print("To quit input=\t'q'")
print("To analyse a decode string input='a'")
Uinput=''
commands='adeq'
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while Uinput !='q': #check to quit from programme
    Uinput=input("Enter the letter of command do you want to do=\t")#user input
    Uinput=Uinput.lower()#get the command input  as lowercase
    def encode():#do the encode
        key=1
        msg=input("Enter the message to encode:")#prompt for message
        
        while True:   
          try: #check the input key value is integer
            key=int(input("You have to give key value range in 1-26\nEnter the value of key:"))#prompt for key
            if key>0 and key<26: #check the key between in 1-26
               def ceaserShift(msg): # define a function to get the rotation
                     
                     encrypted_message=''
                     for ch in msg:  #get until the last character in msg
                            if ch in alpha:  #check the character in alpha
                               encrypted_message+=alpha[(alpha.index(ch)+key)%(len(alpha))]
                               #add new character after rotation 
                            else:
                               encrypted_message+=ch
                     return encrypted_message
                #user define funtion for display the output    
               def main():
                 encrypted_message=ceaserShift(msg)
                 print("Orginal message:\t",msg)
                 print("Encrypted message:\t",encrypted_message)
               main()
               break
            else:
                  print("You entered out of range")
                 
          except:
             print("you entered wrong syntax")
        
    def decode():
        key=1
        msg=input("Enter the message to decode:")
        
        while True:   
          try:
            key=int(input("You have to give key value range in 1-26\nEnter the value of key:"))
            if key>0 and key<26:
               def ceaserShift(msg): #define a fuction for rotate the character
                     
                     decrypted_message=''
                     for ch in msg:
                            if ch in alpha:
                               decrypted_message+=alpha[(alpha.index(ch)-key)%(len(alpha))]
                            else:
                               decrypted_message+=ch
                     return decrypted_message
                #define fuction for display the output    
               def main():
                 decrypted_message=ceaserShift(msg)
                 print("Orginal message:\t",msg)
                 print("Decrypted message:\t",decrypted_message)
               main()
               break
            else:
                  print("You entered out of range")
                 
          except:
             print("you entered wrong syntax")

    
    if Uinput=='e': #check the coomad is e
        key=encode
        encode()
    elif Uinput=='d': #check the command is d
        decode()
    elif Uinput=='a': #check the command is a
        def decode(m,s):
            decrypted_message=''
            for ch in m:
                if ch in alpha:
                    decrypted_message+=alpha[(alpha.index(ch)-s)%(len(alpha))]
                else:
                    decrypted_message+=ch
            return decrypted_message        
                    
        decode_message=str(input("Enter the decode string:"))
        plain_text=str(input("enter the plain text:"))
        for number in range(1,26): #getting a range between 1-26
            if plain_text in decode(decode_message,number):  #if the resulting decode text in plain text
                x=decode(decode_message,number) 
                print("decode string is:",x) # print the decode string
               
        
    elif Uinput not in commands: #check the command is in commands string
        print("You entered wrong command. Please enter right command ")
else:
    print("You entered quit command.Now you are quit from the progarmme")

    
            

            
