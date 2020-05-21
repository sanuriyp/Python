print("To encode a string input=\t'e'")
print("To decode a string input=\t'd'")
print("To quit input=\t'q'")
Uinput=''
commands=['e','d','q']
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while Uinput !='q': #check to quit from programme
    Uinput=input("Enter the letter of command do you want to do=\t")#user input
    Uinput=Uinput.lower()#get the command input  as lowercase
    def encode():#do the encode
        key=1
        msg=str(input("Enter the message to encode:"))#prompt for message
        
        while True:   
          try: #check the input key value is integer
            key=int(input("You have to give key value range in 1-26\nEnter the value of key:"))#prompt for key
            if key>0 and key<26: #check the key between in 1-26
               def ceaserShift(msg): #difine fuction to rotate the character in message
                     
                     encoded_message='' #initialize a empty string for add character after encode
                     for ch in msg:     #check until charaters in input message
                            if ch in alpha:   #find charater in alphabet
                               encoded_message+=alpha[(alpha.index(ch)+key)%(len(alpha))]
                            else:
                               encoded_message+=ch
                     return encoded_message
                    #user difine function to print output
               def main():
                 encoded_message=ceaserShift(msg)
                 print("Orginal message:\t",msg)
                 print("Encrypted message:\t",encoded_message)
               main()
               break
            else:
                  print("You entered out of range")
                 
          except:
             print("you entered wrong syntax")
    #user define to decode    
    def decode():
        key=1
        msg=str(input("Enter the message to decode:")) #get the input string to decode
        
        while True:   
          try:
            key=int(input("You have to give key value range in 1-26\nEnter the value of key:"))
            if key>0 and key<26:
               def ceaserShift(msg): #define function to rotate the character
                     
                     decoded_message='' 
                     for ch in msg:   #get until the last character in msg(user input)
                            if ch in alpha:
                               decoded_message+=alpha[(alpha.index(ch)-key)%(len(alpha))]
                               #'find index position of charater in alpha by subtract the key value and get the mod by length of alpha'
                               #'get new index position and add charater related to that new index position to decoded_message string'
                            else:
                               decoded_message+=ch
                     return decoded_message
                    
                    #user define for output
               def main():
                 decoded_message=ceaserShift(msg)
                 print("Message to decode:\t",msg)
                 print("Decrypted message:\t",decoded_message)
               main()
               break
            else:
                  print("You entered out of range")
                 
          except:
             print("you entered wrong syntax")

    
    if Uinput=='e': #check the command is e
        key=encode
        encode() #call the encode user define function
    elif Uinput=='d':
        decode() #call the decode user define function
    elif Uinput not in commands:
        print("You entered wrong command. Please enter right command ")
else:
    print("You entered quit command.Now you  quit from the progarmme")

    
            

            
