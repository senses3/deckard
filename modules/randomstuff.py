#!/usr/bin/env python
"""
randomstuff.py - Random Stuff Module

Don't judge me monkey.

More info:
https://github.com/nickfletcher/deckard/
"""

import random, time

def same(phenny, input):
    randmsg = random.choice(["same", "same same","same same but different"])
    phenny.say(randmsg)
same.rule = '(same)$'

def bro(phenny, input):
    randmsg = random.choice(["bro it up bro", "brobox360"])
    phenny.say(randmsg)
bro.rule = '(bro)$'

def dank(phenny, input):
    randmsg = random.choice(["ARMY OF DANKNESS","diggity damn","dank like a skank tank"])
    phenny.say(randmsg)
dank.rule = '(dank)$'

def hella(phenny, input):
    randmsg = random.choice(["hella yolo swaggins","hella wicked dope yolo swag","hella dope with some wicked yolo swag bitch","hella yeah","hella citronella nutella my salmonella!","thats hella wicked dank bro"])
    phenny.say(randmsg)
hella.rule = '(hella)$'

def naksa(phenny, input):
    randmsg = random.choice(["who let naksa drink","who the hell let naksa drink","who the fuck let naksa drink"])
    phenny.say(randmsg)
naksa.rule = '(naksa)$'

def dou(phenny, input):
    randmsg = random.choice(["dou it up","i dou what i want","dou it live"])
    phenny.say(randmsg)
dou.rule = '(dou|doo)$'
# dou.priority = 'high'

def zzz(phenny, input):
    randmsg = random.choice(["zzz","zeeee"])
    phenny.say(randmsg)
zzz.rule = '(zzz)$'
# zzz.priority = 'high'

def good_one(phenny, input):
    randmsg = random.choice(["FOR REAL LOL", "HAH!"])
    phenny.say(randmsg)
    time.sleep(random.randint(0,1))
good_one.rule = '(good one)$'
# good_one.priority = 'high'

def beaker(phenny, input):
    if input.nick == "ayashi":
        randmsg = random.choice(["hey bitch", "beaker bitch", "beaker beaker ayashi"])
        time.sleep(random.randint(0,1))
        phenny.reply(randmsg)
    else:
        phenny.say("beaker beaker")
beaker.rule = '(:<.*)$'
# beaker.priority = 'high'

def zoidberg(phenny, input):
    phenny.say("(V)o,,,o(V) - Why not Zoidberg?")
zoidberg.rule = '(zoidberg)$'
# zoidberg.priority = 'high'

def brusque(phenny, input):
    randmsg = random.choice(["stop that"])
    phenny.say(randmsg)
brusque.rule = '(brusque.*)$'

def dope(phenny, input):
    randmsg = random.choice(["dope like taupe", "the pope smokes dope"])
    phenny.say(randmsg)
dope.rule = '(dope.*)$'

def fuckworldguest(phenny, input): 
    phenny.say(input.nick + "++")
fuckworldguest.rule = '(worldguest--)$'

def badkarma(phenny, input): 
    phenny.say(input.nick + "--")
badkarma.rule = '(deckard--)$'

def hello(phenny, input): 
    greeting = random.choice(('Hi', 'Hey', 'Hello'))
    punctuation = random.choice(('', '!'))
    phenny.say(greeting + ' ' + input.nick + punctuation)
hello.rule = r'(?i)(hi|hello|hey) $nickname[ \t]*$'

def beaker_face(phenny, input):
    phenny.say(":<")
beaker_face.rule = '(beaker)$'

def sad_beaker(phenny, input):
    phenny.say(":'<")
sad_beaker.rule = '(sad beaker)$'
# beaker_face.priority = 'high'

def birdface_word(phenny, input):
    phenny.say("god damn birdface")
birdface_word.rule = '(:>)$'
# birdface_word.priority = 'high'

def birdface_face(phenny, input):
    phenny.say(":>")
birdface_face.rule = '(birdface)$'
# birdface_face.priority = 'high'

def balls(phenny, input):
    phenny.say("worldguest likes balls")
balls.rule = '(balls)$'

def owl(phenny, input):
    phenny.reply('It\'s artificial?')
owl.rule = '(do you like our owl?.*)$'
# owl.priority = 'high'

def owl2(phenny, input):
    phenny.reply('Must be expensive.')
owl2.rule = '(of course it is.*)$'
# owl2.priority = 'high'

def cockboat(phenny, input):
    phenny.reply('septor wanted me to make this command so i made it, there.  Are you happy now?')
cockboat.commands = ['cockboat']

def tacosnack(phenny, input):
    phenny.reply('I guess it\'s better than eating raw oyster and boiled dog. ;)')
tacosnack.commands = ['tacosnack']

def baconpancake(phenny, input):
    phenny.say('bacon pancakes, makin bacon pancakes http://www.youtube.com/watch?v=sxVvKb0fGAY')
baconpancake.rule = '(baconpancake)$'

def cnn(phenny, input):
    phenny.say('cnn is pretty gay')
cnn.rule = '(cnn)$'
