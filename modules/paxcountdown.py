#!/usr/bin/env python
"""
paxcountdown.py - Pax Countdown Module

More info:
https://github.com/crispus/deckard/
"""

import datetime

def pax_east(jenni, input):
	diff = datetime.datetime(2013, 03, 22) - datetime.datetime.now()
	jenni.say("Pax East is " + str(diff.days) + " days, " + str(diff.seconds/60/60) + " hours, and " + str(diff.seconds/60 - diff.seconds/60/60 * 60) + " minutes from now.")
pax_east.commands = ['paxeast']
