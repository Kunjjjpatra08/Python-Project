import random
print("Welcome to Rock,Paper,Scissors game :- ")

user_score=0
computer_score=0

while True:
    computer=random.choice(["Rock","Papper","Scissors"])
    print("\nYour score = ",user_score)
    print("Computer score = ",computer_score)
         
    user=str(input("\nEnter Rock,Paper,Scissors or Quit : "))

    if user=="Quit":
        break

    print("Computer choice : ",computer)

    if user==computer:
        print("Equal")

    elif (user=="Rock") and (computer=="Scissors"):
        print("You got 1 point")
        user_score+=1    

    elif (computer=="Rock") and (user=="Scissors"):
        print("Computer got 1 point")  
        computer_score+=1 

    elif (user=="Papper") and (computer=="Rock"):
        print("You got 1 point")
        user_score+=1

    elif (computer=="Papper") and (user=="Rock"):
        print("Computer got 1 point")
        computer_score+=1

    elif (user=="Scissors") and (computer=="Papper"):
        print("You got 1 point")  
        user_score+=1  

    elif (computer=="Scissors") and (user=="Papper"):
        print("Computer got 1 point")
        computer_score+=1

    elif (user=="Scissors") and (computer=="Rock"):
        print("Computer got 1 point")
        computer_score+=1

    elif (computer=="Scissors") and (user=="Rock"):
        print("You got 1 point")       
        user_score+=1 

    else:
        print("Oops! you enter wrong option.Please enter right option")               
 
print("You final score : ",user_score)
print("Computer final score : ",computer_score) 
print("Thank you for play this game") 