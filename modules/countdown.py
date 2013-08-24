#!/usr/bin/env python
"""
countdown.py - Countdown Module

More info:
https://github.com/nickfletcher/deckard/
"""

import datetime

def paxeast(phenny, input):
    diff = datetime.datetime(2014, 04, 11) - datetime.datetime.now()
    phenny.say("Pax East is " + str(diff.days) + " days, " + str(diff.seconds/60/60) + " hours, and " + str(diff.seconds/60 - diff.seconds/60/60 * 60) + " minutes from now.")
paxeast.rule = '(paxeast?.)$'

def paxprime(phenny, input):
    diff = datetime.datetime(2013, 8, 30) - datetime.datetime.now()
    phenny.say("Pax Prime is " + str(diff.days) + " days, " + str(diff.seconds/60/60) + " hours, and " + str(diff.seconds/60 - diff.seconds/60/60 * 60) + " minutes from now.")
paxprime.rule = '(paxprime?.)$'

def bcon(phenny, input):
    diff = datetime.datetime(2013, 11, 8) - datetime.datetime.now()
    phenny.say("Blizzcon is " + str(diff.days) + " days, " + str(diff.seconds/60/60) + " hours, and " + str(diff.seconds/60 - diff.seconds/60/60 * 60) + " minutes from now.")
bcon.rule = '(bcon?.|blizzcon?.)$'

def simcity(phenny, input):
    diff = datetime.datetime(2013, 03, 5) - datetime.datetime.now()
    phenny.say("SimCity 5 is " + str(diff.days) + " days, " + str(diff.seconds/60/60) + " hours, and " + str(diff.seconds/60 - diff.seconds/60/60 * 60) + " minutes from now pharix! lol.")
simcity.rule = '(simcity?.)$'
