import random
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors. \n"))
computer_choice=random.randint(0,2)
print(f"computer choose {computer_choice}")
if user_choice>=3 or user_choice<0:
    print("You typed invalied number")    
elif user_choice==0 and computer_choice==2:
    print("you win")
elif user_choice==2 and computer_choice==1:
    print("you lose")
elif computer_choice > user_choice:
    print("You lose")
elif computer_choice < user_choice:
    print("You win")
elif computer_choice == user_choice:
    print("Its a draw")
