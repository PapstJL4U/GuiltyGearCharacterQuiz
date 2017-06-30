"""This is the main modul for the Guilty Gear Xrd Character Quiz"""
version = '0.1'
author = 'Pride and Prejudice aka PapstJL4U'
from CharacterData import shoutout
import CharacterValues as cv

#Multiplier for how much emotional/subjective qualities affect results -
#becomes 1.5 if player specifies this is important to him or her"""
_emotemultiplier = 1
#Value for double playstyle. To be given 0.5 if zoning or rushdown are given
#a positive value. If it's 1, the doubleplay question is revealed."""
_doubleplay = 0

def addEmotion(name):
    """ 'like' question will use this method to increase the rating of a character"""
    global _emotemultiplier
    for char in cv.character_list:
        if name == char.charname:
            char.points = char.points+(1*_emotemultiplier)
        
def hateEmotion(name):
    """ 'dislike/hate'  question use this method to decrease the rating of a character"""
    global _emotemultiplier
    for char in cv.character_list:
        if name == char.charname:
            char.points = char.points-(1*_emotemultiplier)

def upgradeTier(tier):
    """Every character with the respective tier gets one point"""
    for char in cv.character_list:
        if char.tier == tier:
            char.points += 1

def pickPlaystyle(playstyle):
    """Every character with the respective playstyle gets one point, emo playstyle increase emotemultiplier for whatever reason"""
    global _emotemultiplier
    if playstyle == "Emotional":
        _emotemultiplier = 1.5
    
    for char in cv.character_list:
        if char.playstyle == playstyle:
            char.points += 1

def playerSkill(skill):
    """Every character with the respective skill level gets one point, high should increase all levels, medium should
    increase low and medium"""
    for char in cv.character_list:
        if char.skill == skill:
            char.points += 1
            
def playerGoal(goal):
    """unused in the original quiz, included for possible future usage"""
    pass

def playPriority():
    """A a helper fuction to decide between zoning and rushdown"""
    global _doubleplay
    _doubleplay += 0.5
    if _doubleplay == 1.0:
        return True #do doubleplay question aka rushdown and zoning
    """
    <div class="question" id="doubleplay">
<h2>Question 12.5 - You indicated you like both Rushdown and Zoning. What would you think of a character who does both?</h2>

<ul>
	<li><a href="javascript:void(0)" onclick="doDoublePlay(1);">I'd like that. Please make it a priority.</a></li>
	<li><a href="javascript:void(0)" onclick="doDoublePlay(0);">Fine by me if I get one.</a></li>
	<li><a href="javascript:void(0)" onclick="doDoublePlay(-1);">No. I'd prefer playing one or the other.</a></li>
</ul>
</div>
    """
    
def doZoning(factor):
    """Every character with the respective zoning gets one point increased by its factor"""
    if factor>0:
        playPriority()
    for char in cv.character_list:
        char.points = char.points + factor * char.zoning

def doRushdown(factor):
    """Every character with the respective rushdown gets one point increased by its factor"""
    if factor>0:
        playPriority()
    for char in cv.character_list:
        char.points = char.points + factor * char.rushdown

def doDoublePlay(factor):
    for char in cv.character_list:
        if((char.zoning>0) and (char.zoning<1) and (char.rushdown>0) and (char.rushdown<1)):
            char.points = char.points + (char.zoning*factor) + (char.rushdown*factor)

def playerFocus(focus):
    """checks if focus is in the list of focuses of each character"""
    for char in cv.character_list:
        if focus in char.focus.split(","):
            char.points+=1

def playerRange(range):
    """Every character with the respective ranges gets one point, chars can have more than one range"""
    for char in cv.character_list:
        if range in char.range.split(","):
            char.points+=1

def playerGender(gender, factor):
    """Every character with the respective gender gets one point increased by a factor between 0 and 2"""
    for char in cv.character_list:
        if gender in char.gender.split(","):
            char.points = char.points + factor

def playerCharge(charge):
    """Every character with the respective charge usage gets one point"""
    for char in cv.character_list:
        if charge in char.charname.split(","):
            char.points+=1

def playerGimmick(gimmick):
    """unused function from the original"""
    pass

def playerMixups(mixup):
    """Every character with the respective mix gets one point, chars can have more than one mixup type"""
    for char in cv.character_list:
        if mixup in char.mixup.split(","):
            char.points+=1

def playerMoral(moral):
    """Every character with the respective moral gets one point influence by the emotemultiplier"""
    for char in cv.character_list:
        if moral == char.moral:
            char.points = char.points + _emotemultiplier

def playerOne(oneplayer):
    """Every character with the respective playstyle gets one point"""
    for char in cv.character_list:
        if oneplayer == char.oneplayer:
            char.points+=1

def playerPriority(priority):
    """Every character with the respective priority (like damage, utility, mobility,...) gets one point"""
    for char in cv.character_list:
        if priority in char.priority.split(","):
            char.points+=1

def playerProjectile(projectile):
    """Every character with the respective projectil playstyle gets one point"""
    for char in cv.character_list:
        if projectile in char.projectile.split(","):
            char.points+=1

def playerReliant(reliance):
    """Every character with the respective reliance on resources gets one point"""
    for char in cv.character_list:
        if reliance == char.reliance:
            char.points+=1

def playerResource(resource):
    """Every character with the respective type of resource gets one point"""
    for char in cv.character_list:
        if resource == char.resource:
            char.points+=1

def playerReversal(reversal):
    """Every character with the respective reversl style gets one point"""
    for char in cv.character_list:
        if reversal == char.reversal:
            char.points+=1

def playerSetPlay(setplay):
    """Every character with the respective setply type gets one point"""
    for char in cv.character_list:
        if setplay in char.setplay.split(","):
            char.points+=1

def playerStances(stance):
    """Every character with stances gets one point"""
    for char in cv.character_list:
        if stance == char.stance:
            char.points+=1

def playerVortex(vortex):
    """I have no idea, what vortex means in this context ._."""
    for char in cv.character_list:
        if vortex == char.vortex:
            char.points+=1

def getResults():
    """At last we do all the fine math, hopefully all goes right"""
    arr = []
    results = [""]
    results2 = [""]
    runner = [""]
    runner2 = [""]
    inc = 0
    cre = 0

    for char in cv.character_list:
        arr.append(char.points)

    for char in cv.character_list:
        if(char.points == max(arr)):
            results[inc] = char.fullname
            results2[inc] = char.charname
        elif ((char.points < max(arr)) and (char.points >= (max(arr)-1))):
            runner[cre] = char.fullname
            runner2[cre] = char.charname

    title = "Your top result is "+results[0]+"!"
    img = results2[0]+".png"
    other = ""
    runners = ""
    if len(results)>1:
        other = "Other characters you tied for:"
        for char in results:
            other = other+" "+char
    if len(runner)>0:
        runners = "Close second characters:"
        for char in runner:
            runners = runners + " " + char

    completeResult = []
    completeResult.append(title)
    completeResult.append(img)
    completeResult.append(other)
    completeResult.append(runners)

    return completeResult

if __name__ == "__main__":
    """Despite the classic ideas, the main.py is not really the entrance to the programm. Use the right *ui.oy to have 
    interactivity"""
    print("No gui yet")