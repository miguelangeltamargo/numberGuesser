#You Got Python
#The user will select a range of numbers, and then enter the secretnumber. 
#The machine will use quick sort? method to try and find the secretnumber.

print("""This program is going to find your secret,
given a range of numbers selected by the user and a number within that range,
I the program will find your number.""")

#come back to range to be able to take format of xxx-xxx
rLow = int(input("Enter the low end: "))
rHigh = int(input("Enter the high end: "))
secretNum = int(input("Enter your secretNumber: "))
guessCount = 0
mid = 0

while True:
	guessCount += 1
	mid = (rHigh + rLow)//2
	if mid == secretNum:
		print("I found it!\nYou chose "+str(mid)+".")
		print("Number of guesses: "+str(guessCount))
		
		break
#	if guessCount == 15:
#		print("Number of guesses: "+str(guessCount))
#		break
	elif mid > secretNum:
		rHigh = mid
		#print("Too high. It's not "+str(mid)+'.')
		#print("\t\tHigh is " + str(rHigh) + ", Low is " + str(rLow))
		
	elif mid < secretNum:
		rLow = mid
		#print("Too low. It's not "+str(mid)+'.')
		#print("\t\tHigh is " + str(rHigh) + ", Low is " + str(rLow))
		
	

	