#You Got Python
import random

print("""Im thinking of a number between 1-100.
Can you guess what it is?""")

guessCt = 0
numGuess = 0
secretNumber = random.randint(1,100)

while numGuess != secretNumber:
	guessCt += 1
	numGuess = int(input("Is it "))
	if numGuess == secretNumber:
		print("Good-job! You got it!")
		break
	elif numGuess == -1:
		print("The number was " + str(secretNumber) +'.')
		break
	elif (numGuess - secretNumber) > 0 and (numGuess - secretNumber) <= 10 :
		print("You're close! But still too high. Try again.")
	elif (numGuess - secretNumber) <= 0 and (numGuess - secretNumber) >=-10:
		print("You're close! But still too low. Try again.")
	elif numGuess > secretNumber:
		print("You're too high! Try again.")
	elif numGuess < secretNumber:
		print("You're too low! Try again.")
	


	
		