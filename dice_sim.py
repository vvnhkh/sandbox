import random
print("Welcome to the Dice Simulator!\n")

# user input and feedback intended to prevent errors
error_check = 0
while error_check == 0:
	min = int(raw_input("Input minimum number:\n"))
	max = int(raw_input("Input maximum number:\n"))
	if (min < max) and (min > 0):
		error_check = 1
		while error_check == 1:
			dicenumber = int(raw_input("How many dice are you using? \n"))
			if dicenumber > 0:
				print("Number of dice: "), dicenumber
				error_check = 2
			else: print("You cannot play with no dice or a negative number of dice. Please input a postive integer of dice.\n")
	else: print ("Please check to make sure your max value is larger than your minimum value and that all integers are positive.\n")

# actually rolling dice
ans = "y"
while ans == "y":
	i = 0 # resets for future loops in case user wishes to roll again
	def roll_dice():
		for i in range(dicenumber):
			yield random.randint(min, max)
		for random_number in roll_dice():
			print("You rolled... %d." %(random_number))
	ans = input("Roll again? [y/n] \n")
	if ans == "n":
		exit() # quit
