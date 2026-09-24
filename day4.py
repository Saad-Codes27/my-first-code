import random 

secret = random.randint(1,100)
attempts=0

print("I have picked a number between 1 and 100!")

while 'true':
      guess = int(input("your guess:"))
      attempts=attempts + 1

      if guess == secret: 
         print(f"YES! You guessed it in {attempts} tries")
         break
      elif guess<secret:
          print("Too low! Try higher")
      else:
          print("Too high! Try lower")
