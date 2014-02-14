#coding: utf8
"""
randomstuff.py - Random Stuff Module

Don't judge me monkey.

More info:
https://github.com/nickfletcher/deckard/
"""

import random, time

def bacon(deckard, input):
    deckard.say("Bacon time is NOW!")
bacon.rule ='(bacon|bacon\?)$'

def zee(deckard, input):
    randmsg = random.choice(["zzz", "ill sleep when im dead"])
    deckard.say(randmsg)
zee.rule = '(zee.*)$'

def same(deckard, input):
    randmsg = random.choice(["same", "same.bmp", "same.png", "also, same","same same","same same same same same same same","same same but different"])
    deckard.say(randmsg)
same.rule = '(same)$'

def bro(deckard, input):
    randmsg = random.choice([".chat about jelly bro"])
    deckard.say(randmsg)
bro.rule = '(bro)$'

def hella(deckard, input):
    randmsg = random.choice(["hella jelly bro?","hella yolo swaggins","hella wicked dope yolo swag","hella dope with some wicked yolo swag bitch","hella yeah","hella citronella nutella my salmonella!","thats hella wicked dank bro"])
    deckard.say(randmsg)
hella.rule = '(hella)$'

def naksa(deckard, input):
    randmsg = random.choice(["who let naksa drink","who the hell let naksa drink","who the fuck let naksa drink"])
    deckard.say(randmsg)
naksa.rule = '(naksa\?)$'

def dou(deckard, input):
    randmsg = random.choice(["dou it up","i dou what i want","dou it live","dou it tou it"])
    deckard.say(randmsg)
dou.rule = '(dou|doo)$'

def zzz(deckard, input):
    randmsg = random.choice(["zzz","zeeee"])
    deckard.say(randmsg)
zzz.rule = '(zzz)$'

def good_one(deckard, input):
    randmsg = random.choice(["FOR REAL LOL", "HAH!"])
    deckard.say(randmsg)
    time.sleep(random.randint(0,1))
good_one.rule = '(good one)$'

def beaker(deckard, input):
    if input.nick == "ayashi":
        randmsg = random.choice(["beaker all up ins", "beaker bitch", "beaker beaker ayashi"])
        time.sleep(random.randint(0,1))
        deckard.reply(randmsg)
    else:
        deckard.say("beaker beaker")
beaker.rule = '(:<.*)$'

def zoidberg(deckard, input):
    deckard.say("(V)o,,,o(V) - Why not Zoidberg?")
zoidberg.rule = '(zoidberg\?)$'

def brusque(deckard, input):
    randmsg = random.choice(["stop that"])
    deckard.say(randmsg)
brusque.rule = '(brusque)$'

def dope(deckard, input):
    randmsg = random.choice(["dope like taupe", "the pope smokes dope"])
    deckard.say(randmsg)
dope.rule = '(dope)$'

def fuckworldguest(deckard, input):
    deckard.say(input.nick + "++")
fuckworldguest.rule = '(worldguest--)$'

def badkarma(deckard, input):
    deckard.say(input.nick + "--")
badkarma.rule = '(deckard--)$'

def beaker_face(deckard, input):
    deckard.say(":<")
beaker_face.rule = '(beaker)$'

def sad_beaker(deckard, input):
    deckard.say(":'<")
sad_beaker.rule = '(sad beaker)$'

def birdface_word(deckard, input):
    deckard.say("god damn birdface")
birdface_word.rule = '(:>)$'

def birdface_face(deckard, input):
    deckard.say(":>")
birdface_face.rule = '(birdface)$'

def worldguest(deckard, input):
    deckard.say("who?")
worldguest.rule = '(worldguest\?)$'

def owl(deckard, input):
    deckard.reply('It\'s artificial?')
owl.rule = '(do you like our owl\?)$'

def owl2(deckard, input):
    deckard.reply('Must be expensive.')
owl2.rule = '(of course it is)$'

def tacosnack(deckard, input):
    deckard.reply('I guess it\'s better than eating raw oyster and boiled dog. ;)')
tacosnack.rule = '(tacosnack)$'

def turkey(deckard, input):
    randmsg = random.choice(['do you even praise it?', 'praise the god damn turkey'])
    deckard.say(randmsg)
turkey.rule = '(turkey\?)$'

def baconpancake(deckard, input):
    deckard.say('bacon pancakes, makin bacon pancakes http://www.youtube.com/watch?v=sxVvKb0fGAY')
baconpancake.rule = '(baconpancake)$'

def pizza(deckard, input):
    randmsg = random.choice(["everytime i want that pizza (x6)", "i need some pizza(x6)", "i go to davids pizza", "when i get a serious craving for something i want to eat", "i need some cheese, tomatoes, and olives, and maybe even some meat"])
    deckard.say(randmsg)
pizza.rule = '(pizza\?)$'

def fox(deckard, input):
    randmsg = random.choice(["Ring-ding-ding-ding-dingeringeding!", "Wa-pa-pa-pa-pa-pa-pow!", "Hatee-hatee-hatee-ho!", "Joff-tchoff-tchoffo-tchoffo-tchoff!", "Jacha-chacha-chacha-chow!", "Fraka-kaka-kaka-kaka-kow!", "A-hee-ahee ha-hee!", "A-oo-oo-oo-ooo!"])
    deckard.say(randmsg)
fox.rule = '(what does the fox say\?|what the fox say\?|fox\?)$'

def pig(deckard, input):
    randmsg = random.choice([ "please step out of the vehicle", "licence and registration please" ])
    deckard.say(randmsg)
pig.rule = '(pig\?)$'

def dealwithit(deckard, input):
    deal = '(•_•) , ( •_•)>⌐■-■ , (⌐■_■) deal with it'
    deckard.say(deal)
dealwithit.rule = '(dwi)$'

def tables(deckard, input):
    flip = '(╯°□°）╯︵ ┻━┻)'
    deckard.say(flip)
tables.rule = '(tables\?)$'

def tableflip(deckard, input):
    flip = '(╯°□°）╯︵ ┻━┻)'
    deckard.say(flip)
tableflip.rule = '(flip\!)$'

def tablefix(deckard, input):
    noflip = '┬─┬ノ( º _ ºノ)'
    deckard.say(noflip)
tablefix.rule = '(noflip\!)$'

def disarm_trap(deckard, input):
    # trap = r_rule.match(input.bytes)
    trap = 'wfh'
    deckard.say(trap)
disarm_trap.rule = '(disarm\?)$'

def pot_leaves(deckard, input):
    ten = '[10]'
    deckard.say(ten)
pot_leaves.rule = '(loadPotLeaves)$'

def canada(deckard, input):
    eh = 'AMERICA'
    deckard.say(eh)
canada.rule = '(canada\?)'

# def hearthstone_key(deckard, input):
#     reply = 'yeah i dont have one yet'
#     deckard.say(reply)
# hearthstone_key.rule = '(deckard: do you need a hearthstone key\?)$'

def dutch_crunch(deckard, input):
    deckard.say("OMFGGGGG SOOO GOOOOOODDDDD")
dutch_crunch.rule = '(dutch crunch\?)$'
