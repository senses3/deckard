#!/usr/bin/env python
"""
randomstuff.py - Random Stuff Module

Don't judge me monkey.

More info:
https://github.com/crispus/deckard/
"""

import random, time
limit = 100

def dou(jenni, input):
		randmsg = random.choice(["dou it up","i dou what i want"])
		jenni.say(randmsg)
dou.commands = ['dou']

def zzz(jenni, input):
		randmsg = random.choice(["zzz","zeeee"])
		jenni.say(randmsg)
zzz.commands = ['zzz']
