"""This is a commandline interface to test the Guilty Gear Xrd Character Quiz"""
import main
from CharacterValues import character_list as cl

version = main.version
author = main.author

"""general syntax:
first print the question and get the input 2 lines below
the case variable is just a switch case construct
"""


def firstQ():
    print("Question 1 - What tier of character do you want to play?")
    value = int(input("1:High, 2:Mid, 3:Low, 4:Low+Mid, 5:High+Mid: \n"))
    if value < 4:
        main.upgradeTier(value)
    elif value == 4:
        main.upgradeTier(2)
        main.upgradeTier(3)
    elif value == 5:
        main.upgradeTier(1)
        main.upgradeTier(2)
    else:
        quit()


def secondQ():
    print("Question 2 - What's most important to you?")
    value = input("[S]pecial, [P]repared, [E]motional, [R]ewarding: \n").upper()
    case = {"S": "Special", "P": "Prepared", "E": "Emotional", "R": "Rewarding"}
    main.pickPlaystyle(case[value])


def thirdQ():
    print("Question 3 - What's your current skill level in fighting games?")
    value = input("[N]ew, [M]edium, [H]igh, [U]nimportant: \n").upper()
    if value == "N":
        main.playerSkill("New")
    elif value == "M":
        main.playerSkill("New")
        main.playerSkill("Mid")
    elif value == "H":
        main.playerSkill("New")
        main.playerSkill("High")
        main.playerSkill("Mid")
    else:
        return


def fourthQ():
    pass


def fifthQ():
    print("Question 5 - Who's your favourite character in the story?")
    li = []
    for chars in cl:
        li.append(chars.charname)
        print(chars.charname + " ", end='', flush=True)
    value = input("use above simple charname: \n")
    if value in li:
        main.addEmotion(value)
    else:
        return


def sixthQ():
    print("Question 6 - Which character do you think looks the best?")
    li = []
    for chars in cl:
        li.append(chars.charname)
        print(chars.charname + " ", end='', flush=True)
    value = input("use above simple charname: \n")
    if value in li:
        main.addEmotion(value)
    else:
        return


def seventhQ():
    print("Question 7 - Which character do you relate to the most?")
    li = []
    for chars in cl:
        li.append(chars.charname)
        print(chars.charname + " ", end='', flush=True)
    value = input("use above simple charname: \n")
    if value in li:
        main.addEmotion(value)
    else:
        return


def eighthQ():
    print("Question 8 - Which character do you think looks the worst?")
    li = []
    for chars in cl:
        li.append(chars.charname)
        print(chars.charname + " ", end='', flush=True)
    value = input("use above simple charname: \n")
    if value in li:
        main.hateEmotion(value)
    else:
        return


def ninethQ():
    print("Question 9 - Which character is your least favourite in general?")
    li = []
    for chars in cl:
        li.append(chars.charname)
        print(chars.charname + " ", end='', flush=True)
    value = input("use above simple charname: \n")
    if value in li:
        main.hateEmotion(value)
    else:
        return


def tenthQ():
    print("Question 10 - What sort of moral system do you like in a character?")
    value = input("Goo[d]&Grey, Gre[y], [G]ood, [N]eutral, [E]vil, [U]nimportant \n").upper()
    if value == "D":
        main.playerMoral("Good")
        main.playerMoral("Grey")
    elif value == "Y":
        main.playerMoral("Grey")
    elif value == "G":
        main.playerMoral("Good")
    elif value == "N":
        main.playerMoral("Neutral")
    elif value == "E":
        main.playerMoral("Evil")
    else:
        return


def eleventhQ():
    print("Question 11 - Do you have fun when zoning?")
    value = float(input("High:2, Medium:1, No pref:0, Hell no:-1 \n"))
    main.doZoning(value)


def twelvthQ():
    print("Question 12 - Do you have fun playing with a rushdown playstyle?")
    value = float(input("High:2, Medium:1, No pref:0, Hell no:-1 \n"))
    main.doRushdown(value)


def twelvthandahalfQ():
    print(
        "Question 12.5 - You indicated you like both Rushdown and Zoning. What would you think of a character who does both?")
    value = float(input("Both:1, Either or:0, Only one of them: -1 \n"))
    main.doDoublePlay(value)


def thirdteenthQ():
    print("Question 13 - When in a match, what's your primary focus or favourite thing to do?")
    value = input("[M]ixup, [N]eutral, [C]ondition, C[o]mbos, No of that st[u]ff: \n").upper()
    if value == "U":
        return
    case = {"M": "Mixup", "N": "Neutral", "C": "Condition", "O": "Combos"}
    main.playerFocus(case[value])


def fourteenthQ():
    print("Question 14 - What range are you most comfortable fighting at?")
    value = input("[S]hort, [M]id, [L]ong, [A]ll, [N]o preference \n").upper()
    if value == "N":
        return
    main.playerRange("All")
    if value == "S":
        main.playerRange("Short")
    elif value == "M":
        main.playerRange("Mid")
    elif value == "L":
        main.playerRange("Long")
    else:
        return


def fiveteenthQ():
    print("Question 15 - Do you have a character gender preference?")
    value = input(
        "[M]ale, Strong Male[SM], [F]emale, Strong Female[SF], [S]ubversive roles, [N]o preference \n").upper()
    if value == "S":
        main.playerGender("Other", 2)
    elif value == "SM":
        main.playerGender("Male", 2)
    elif value == "M":
        main.playerGender("Male", 1)
    elif value == "SF":
        main.playerGender("Female", 2)
    elif value == "F":
        main.playerGender("Female", 1)
    else:
        return


def sixteenthQ():
    print("Question 16 - What's the most important or enjoyable quality in a character for you?")
    value = input("[D]amage, [H]P, [M]obility, [U]tility, well [r]rounded \n").upper()
    case = {"M": "Mobility", "U": "Utility", "H": "HP", "D": "Damage", "R": "Rounded"}
    main.playerPriority(case[value])


def seventeenthQ():
    print("Question 17 - Would you feel comfortable managing resources while playing your character?")
    value = input("[V]ery Much, [M]oderate amount, [S]ome is okay, [N]o thanks, [D]oesn't matter \n").upper()
    if value == "V":
        main.playerReliant("Reliant")
    elif value == "M":
        main.playerReliant("Mid")
    elif value == "S":
        main.playerReliant("Mid")
        main.playerReliant("Normal")
    elif value == "N":
        main.playerReliant("Normal")
    else:
        return


def eightteenthQ():
    print("Question 18 - Pick the character resource type that sounds the most fun")
    value = input("[D]ual, [R]esource, [N]ormal, D[o]esn't matter \n").upper()
    if value == "O":
        return
    case = {"D": "Dual", "R": "Resource", "N": "Normal"}
    main.playerResource(case[value])


def nineteenthQ():
    print("Question 19 - Do you want a meterless or metered reversal?")
    value = input("[D]P, [M]eter, [N]o preference \n").upper()
    if value == "N":
        return
    case = {"D": "DP", "M": "Meter"}
    main.playerReversal(case[value])


def tweenteethQ():
    print("Question 20 - Does the idea of stances or multiple movesets in the same character sound appealing?")
    value = input("[Y]es, [N]o, N[o] preference \n").upper()
    if value == "O":
        return
    case = {"Y": "Yes", "N": "No"}
    main.playerStances(case[value])


def twooneQ():
    print("Question 21 - How good do you want your vortex/knockdown pressure to be?")
    value = input("[B]asic, [P]rojectile, [M]illion, [N]o preference \n").upper()
    if value == "N":
        return
    case = {"B": "Basic", "P": "Projectile", "M": "Million"}
    main.playerVortex(case[value])


def twotwoQ():
    print("Question 22 - What is your preferred way of opening people up?")
    value = input("[F]rameTraps, [R]ISC, [C]Grap, [H]ighLow, [L]eftRight, [U]nblockable, [N]o preference \n").upper()
    if value == "N":
        return
    case = {"F": "FrameTraps", "R": "RISC", "C": "CGrab", "H": "HighLow", "L": "LeftRight", "U": "Unblockable"}
    main.playerMixups(case[value])


def twothreeQ():
    pass


def twofourQ():
    print("Question 24 - Do you enjoy playing the one player game?")
    value = input("[Y]es, [K]inda, [N]o, N[o] preference \n").upper()
    if value == "O":
        return
    case = {"Y": "Yes", "N": "No", "K": "Kinda"}
    main.playerOne(case[value])


def twofiveQ():
    print("Question 25- Are you ok with having setplay in your moveset?")
    value = input("[Setplay for Offense and [N]eutral, for [K]nockdown, [M]inimal setplay, N[o] preference \n").upper()
    if value == "O":
        return
    case = {"M": "None", "N": "Neutral", "K": "Knockdown"}
    main.playerSetPlay(case[value])


def twosixQ():
    print("Question 26- Are you ok with charge motions for your special moves?")
    value = input("[L]ots, L[i]ttle, [N]one, N[o] preference \n").upper()
    if value == "O":
        return
    case = {"L": "Lots", "I": "Little", "N": "None"}
    main.playerCharge(case[value])


def twosevenQ():
    print("Question 27- Would you like a projectile?")
    value = input(
        "standard [F]ullscreen, [C]ontrol is enough, [S]pecial is nice, [N]o projectile, N[o] preference \n").upper()
    if value == "O":
        return
    case = {"F": "Standard", "C": "Limited", "S": "Special", "N": "None"}
    main.playerProjectile(case[value])


if __name__ == "__main__":
    print("Oh god, I hope it works")
    firstQ()
    secondQ()
    thirdQ()
    fourthQ()
    fifthQ()
    sixthQ()
    seventhQ()
    eighthQ()
    ninethQ()
    tenthQ()
    eleventhQ()
    twelvthQ()
    if main.doubleplay:
        twelvthandahalfQ()
    thirdteenthQ()
    fourteenthQ()
    fiveteenthQ()
    sixteenthQ()
    seventeenthQ()
    eightteenthQ()
    nineteenthQ()
    tweenteethQ()
    twooneQ()
    twotwoQ()
    twothreeQ()
    twofourQ()
    twofiveQ()
    twosixQ()
    twosevenQ()
    display = main.getResults()
    for str in display:
        print(str)

    main.shoutout()
