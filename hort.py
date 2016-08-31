# Program to flip a coin
# CPS 311 Farroni

import random

flip = random.randint(0,1)

if flip == 0:
	flipWord = "heads"
else:
	flipWord = "tails"

print("The flip: ", flipWord)
