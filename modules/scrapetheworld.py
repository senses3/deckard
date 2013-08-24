#!/usr/bin/env python
"""
scrapetheworld.py - random scrapes

https://github.com/nickfletcher/deckard/
"""
from BeautifulSoup import BeautifulSoup as bs
import urllib2

def commit(phenny, input):
    data = urllib2.urlopen('http://whatthecommit.com').read()
    soup = bs(data)
    whatthe = soup.div.p.string
    phenny.say(whatthe)
commit.rule ='(commit?.)$'

def devex(phenny, input):
    data = urllib2.urlopen('http://developerexcuses.com').read()
    soup = bs(data)
    excuse = soup.a.string
    phenny.say(excuse)
devex.rule ='(devex?.)$'

def dinner(phenny, input):
    data = urllib2.urlopen('http://whatthefuckshouldimakefordinner.com').read()
    soup = bs(data)
    bullshit = soup.dt.dl.string
    meal = soup.a.string
    recipeHref = soup.a['href']
    wtf = bullshit + " " + meal + " " + "(" + recipeHref + ")"
    phenny.say(wtf)
dinner.rule ='(dinner?.)$'

def lhirc(phenny, input):
    data = urllib2.urlopen('http://lhirc.tumblr.com/search/' + input.nick).read()
    soup = bs(data)
    link = soup.h3.a['href']
    phenny.say(link)
lhirc.rule ='(lhirc?.)$'

def zen(phenny, input):
    data = urllib2.urlopen('https://api.github.com/zen').read()
    phenny.say(data)
zen.rule ='(zen?.)$'
