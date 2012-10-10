#!/usr/bin/env python
"""
sandwich.py - Random Sandwich Module

More info:
https://github.com/crispus/deckard/
"""

import random, time

def sandwich(jenni, input):
		randmsg = random.choice(["Here's a fresh BLT!",
			"Have a tasty Chicken Carbonara!",
			"It's dangerous to go alone, take this Pastrami sandwich.",
			"Everyone loves Chicken Parmesan!",
			"I hope you like Reuben sandwiches.",
			"You're a little late, all I have is this PB&J.",
			"Have a Turkey & Swiss!",
			"I made this Tuna Melt for you, with love.",
			"dou told me to give you a Chicken Salad sandwich.",
			"You won a Manwich.",
			"Enjoy this Club sandwich on me!"])
		time.sleep(random.randint(0,1))
		jenni.reply(randmsg)
sandwich.commands = ['sandwich']
