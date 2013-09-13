#!/usr/bin/env python
"""
scrapetheworld.py - random scrapes

https://github.com/nickfletcher/deckard/
"""
from bs4 import BeautifulSoup as bs
import urllib2

hdr = { 'User-Agent' : 'rick deckard' }

def commit(deckard, input):
    data = urllib2.urlopen('http://whatthecommit.com').read()
    soup = bs(data)
    whatthe = soup.div.p.string
    deckard.say(whatthe)
commit.rule ='(commit?.)$'

def devex(deckard, input):
    data = urllib2.urlopen('http://developerexcuses.com').read()
    soup = bs(data)
    excuse = soup.a.string
    deckard.say(excuse)
devex.rule ='(devex?.)$'

def dinner(deckard, input):
    data = urllib2.urlopen('http://whatthefuckshouldimakefordinner.com').read()
    soup = bs(data)
    bullshit = soup.dl.string
    meal = soup.a.string
    recipeHref = soup.a['href']
    wtf = bullshit + " " + meal + " " + "(" + recipeHref + ")"
    deckard.say(wtf)
dinner.rule ='(dinner?.)$'

def lhirc(deckard, input):
    data = urllib2.urlopen('http://lhirc.tumblr.com/search/' + input.nick).read()
    soup = bs(data)
    link = soup.h3.a['href']
    deckard.say(link)
lhirc.rule ='(lhirc?.)$'

def zen(deckard, input):
    data = urllib2.urlopen('https://api.github.com/zen').read()
    deckard.say(data)
zen.rule ='(zen?.)$'
