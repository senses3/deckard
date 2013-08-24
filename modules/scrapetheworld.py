#!/usr/bin/env python
"""
scrapetheworld.py - random scrapes

https://github.com/nickfletcher/deckard/
"""
from bs4 import BeautifulSoup as bs
import urllib2

hdr = { 'User-Agent' : 'rick deckard' }

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
    bullshit = soup.dl.string
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

def rtop(phenny, input):
    url = 'http://reddit.com/r/all'
    req = urllib2.Request(url, headers=hdr)
    data = urllib2.urlopen(req).read()
    soup = bs(data)
    titleString = soup.select(".entry > .title > .title")[0].string
    for link in soup.find_all("a", {"class":"title"})[0:1]:
        href = link['href']
    title = titleString + " (" + href + ")"
    phenny.say(title)
rtop.rule = '(rtop?.)$'
