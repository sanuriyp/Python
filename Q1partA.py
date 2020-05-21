count_1=0   #initialise variable to count marks between 0-29
count_2=0   #initialise variable to count marks between 30-39
count_3=0   #initialise variable to count marks between 40-69
count_4=0   #initialise variable to count marks between 70-100
count=0     #initialise variable to count total marks between 0-100
mark=0      #initialise variable to mark
print("If you want to get the histogram to marks enter negative value")

while mark>=0: #check the mark is negative
  try:
     mark= float(input("Enter a mark:\n")) #get the mark as float
     mark=int(mark) #convert float into intereger
     if mark<=100:  # check the mark below 100
         if mark<=29 and mark>=0: #check the conditions
           #getting the count of this range
            count_1+=1
         elif mark<=39 and mark >=30:
            count_2+=1
         elif mark <=69 and mark>=40:
            count_3+=1
         elif mark>=70 and mark<=100:
            count_4+=1
         
     else:
       print("You exceed the 100") #Output when entered above 100
  
  except:
    print("You entered charater. please enter integer") #Output when  not entered numeric character
  
else:
  print("You entered negative value!....") #output when entered negative value
  print("0-29\t" , "*"*count_1)  #print the stars regarding to relevent count 
  print("30-39\t" , "*"*count_2)
  print("40-69\t" , "*"*count_3)
  print("70-100\t", "*"*count_4)
  count=count_1+count_2+count_3+count_4 #getting the total count
  print("The  number of students in class is : ",count) #print the total students
