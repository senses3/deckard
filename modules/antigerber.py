#!/usr/bin/env python
"""
antigerber.py - Anti Gerberboyprime Module

More info:
https://github.com/nickfletcher/deckard/
"""

import random, time

def antigerber(phenny, input):
	if input.nick == "gerberboyprime":
		randmsg = random.choice([
			"Do you ever shut the fuck up?",
			"Nobody cares!",
			"I hope someone pulls the plug on you.",
			"Dude.. No!",
			"Don't make me say it again.",
			"Mlue doesn't even love you.",
			"Seriously, my dick, your mouth.",
			"I WILL win the spam battle!",
			"I WILL FUCKING KILL YOU",
			"If I had ops I'd kick you.",
			"You're so god damn annoying.",
			"What did I *JUST* say motherfucker?",
			"Shut the god damn fuck up already."])
		time.sleep(random.randint(0,2))
		phenny.reply(randmsg)
antigerber.rule = '.*'
