import random
print("Welcome to number guessing game :")

while True:
    randomnum=random.randint(1,100)
    print("You have only five chance")
    attempt=0
 
    while attempt<5:
       attempt=attempt+1

       guess=int(input("Guess the number : "))
    
       if guess == randomnum:
        print("You guess the number",attempt,"attempt")
        break

       elif guess > randomnum:
        print("Too large,guess lower number")    

       elif guess < randomnum:
        print("Too small,guess higher number")    

    if guess == randomnum:
      print("You win")

    else:
      print("game over")     

    play_again=input("Play agin : ").lower()

    if play_again != "yes":
      print("Thanks for playing")
      break
    



    
