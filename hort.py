# Program to flip a coin
# CPS 311 Farroni

import random

numFlips = int(input("How many times do you want to flip? "))

count = 0

while count < numFlips:
	flip = random.randint(0,1)
	if flip == 0:
		flipWord = "heads"
	else:
		flipWord = "tails"

	count += 1

	print("The flip: ", flipWord)
