count_1=0     #initialise variable to count marks between 0-29
count_2=0     #initialise variable to count marks between 30-39
count_3=0     #initialise variable to count marks between 40-69
count_4=0     #initialise variable to count marks between 70-100
count=0       #initialise variable to count marks between 0-100
mark=0
sum=0         #initialise varable to total of marks
markslist=[]  # make a list of valid marks


while mark>=0 :  #check the input mark is not a negative value
    try:
        mark=float(input("Enter a mark:")) #get the user input
        mark=int(mark) #ignore the floating points 
        if mark<=29 and mark>=0:   #check the mark
            #getting total count of this range
            count_1+=1
        elif mark<=39 and mark>=30:
            count_2+=1
        elif mark <=69 and mark>=40:
            count_3+=1
        elif mark>=70 and mark<=100:
            count_4+=1
       
        
        if mark>=0 and mark<=100:  # validate the input mark is between(0-100)
         sum=sum+mark  #calculate the total marks
         markslist.append(mark) #add elments(mark) into list(markslist)
         high=max(markslist)#check the maximum value 
         low=min(markslist)#check the minimum value
         count+=1
        elif mark>100:
            print("Your entered mark is greater than 100.Please enter mark again")#print when you entered above 100
    except ValueError:
        print("You entered character.please enter a integer value") #print when you not entered integer
else:
  print("You entered negative value to print the Output")  
  print("0-29\t","*"*count_1)#output print stars to particular range of marks
  print("30-39\t","*"*count_2)
  print("40-69\t","*"*count_3)
  print("70-100\t","*"*count_4)
  
  print("The students in class is:",count)
  average=sum/count # calculate the average 
  print("The average is:",average) #print average
  print("The highest mark is:",high) #print highest mark
  print("The lowest mark is:",low)  #print lowest mark
  pass_students=count_3+count_4 # calculate the number of pass students 
  print("Number of students with a pass mark :",pass_students)
