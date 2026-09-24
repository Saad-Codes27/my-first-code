import random 

secret = random.randint(1,100)
print("I have picked a number between 1 and 100!")

while 'true':
      guess = int(input("your guess:"))

      if guess == secret: 
         print(f"BOOM! You guessed it! the number was {secret}")
         break
      elif guess<secret:
          print("Too low! Try higher")
      else:
          print("Too high! Try lower")