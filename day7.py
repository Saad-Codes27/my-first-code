import random
options = ["rock","paper","scissors"]

while 'true':
     user_choice = input("Enter rock,paper,scissors(or 'quit' to exit): ").lower()

     if user_choice == "quit":
        print("Bye! Thanks for playing!")
        break

     if user_choice not in options:
        print("invalid choice! Try again.")
        continue

     computer_choice = random.choice(options)
     print(f"You chose: {user_choice}")
     print(f"computer chose: {computer_choice}")
 
     if user_choice == computer_choice:
        print("Tie!\n")
 
     elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!\n")

     elif user_choice == "paper" and computer_choice == "rock":
        print("You win!\n")

     elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!\n")

     else:
        print ("Computer Wins!\n")