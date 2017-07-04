"""This module provides the all data for the characters. It defines an Interface
in form of a class and creates an instance of the class per character."""
version = '0.1'
author = 'Pride and Prejudice aka PapstJL4U'

_definitions = """
https://docs.google.com/document/d/1CFzF-vIUVmaB2dbSxw8rNvB9ZutIrvwfTBerjzLi0WE

Playstyle
-Prepared [Go in an do yo thang whenever]
-Special [My playstyle is super weird?]
-Rewarding [Patience?]

Skill
-New (Newer to FGs)
-Mid
-Old (Long-time veteran)

SkillGoal
-Low
-Mid
-High

Focus
-Neutral
-Combos
-Mixup
-Condition

Range (Can have multiple)
-Short
-Mid
-Long
-All

Priority
-Rounded
-Mobility
-Utility
-Damage
-HP

Reliance (on Resources)
-Normal
-Mid
-Reliant

Resource [Meter, can have Normal and Resource]
-Normal
-Dual (a whole second meter that may need to be recharged)
-Resource

Moral
-Good
-Grey
-Neutral
-Evil
"""


def shoutout():
    print("Everything is based on /u/superange128 work:\
            http://kalavinka.co.uk/GUILTY/")
    print("more information can be found under: \
            https://www.reddit.com/r/Guiltygear/comments/5vjabg/which_guilty_\
            gear_xrd_revelator_1_character/")


class Character:
    """This class describes a character in GGXrd. Many descriptions are just
    copypasted from the doc or the website quiz
    data example:
    "fullname": "Sol Badguy",
        "charname": "sol",
        "Tier": "High",
        "Playstyle": "Prepared",
        "Skill": "New",
        "Zoning": 0,
        "Rushdown": 1,
        "Focus": "Condition,Damage",
        "Range": "Short,Mid",
        "Gender": "Male",
        "Priority": "Rounded",
        "Reliance":"Normal",
        "Resource":"Normal",
        "Moral":"Grey",
        "Reversal":"DP",
        "Stances":"No",
        "Vortex":"Basic",
        "Mixups":"CGrab,RISC",
        "OnePlayer":"Kinda",
        "SetPlay":"None",
        "Charge":"None",
        "Projectile":"Limited",
        "Points": 0
        """

    def __init__(self, *args, **kwargs):
        if len(kwargs) < 22:
            self._fullname = args[0]
            self._charname = args[1]
            self._tier = args[2]
            self._playstyle = args[3]
            self._skill = args[4]
            self._zoning = args[5]
            self._rushdown = args[6]
            self._focus = args[7]
            self._combat_range = args[8]
            self._gender = args[9]
            self._priority = args[10]
            self._reliance = args[11]
            self._resource = args[12]
            self._moral = args[13]
            self._reversal = args[14]
            self._stances = args[15]
            self._vortex = args[16]
            self._mixups = args[17]
            self._oneplayer = args[18]
            self._setplay = args[19]
            self._charge = args[20]
            self._projectile = args[21]
            self._points = args[22]
        else:
            self._fullname = kwargs["fullname"]
            self._charname = kwargs["charname"]
            self._tier = kwargs["Tier"]
            self._playstyle = kwargs["Playstyle"]
            self._skill = kwargs["Skill"]
            self._zoning = kwargs["Zoning"]
            self._rushdown = kwargs["Rushdown"]
            self._focus = kwargs["Focus"]
            self._combat_range = kwargs["Range"]
            self._gender = kwargs["Gender"]
            self._priority = kwargs["Priority"]
            self._reliance = kwargs["Reliance"]
            self._resource = kwargs["Resource"]
            self._moral = kwargs["Moral"]
            self._reversal = kwargs["Reversal"]
            self._stances = kwargs["Stances"]
            self._vortex = kwargs["Vortex"]
            self._mixups = kwargs["Mixups"]
            self._oneplayer = kwargs["OnePlayer"]
            self._setplay = kwargs["SetPlay"]
            self._charge = kwargs["Charge"]
            self._projectile = kwargs["Projectile"]
            self._points = kwargs["Points"]

    @property
    def fullname(self):
        """This is the characters full ingame name,one value only"""
        return self._fullname

    @property
    def charname(self):
        """This a short, unique handle for the Character,one value only"""
        return self._charname

    @property
    def tier(self):
        """Describes the position within the tier list, one value only"""
        return self._tier

    @property
    def playstyle(self):
        """The playstyle can be, one value only:
        -Prepared [Go in an do yo thang whenever]
        -Special [My playstyle is super weird?]
        -Rewarding [Patience?]"""
        return self._playstyle

    @property
    def skill(self):
        """The skill level can be,one value only:
        -New (Newer to FGs)
        -Mid
        -Old (Long-time veteran)"""
        return self._skill

    @property
    def zoning(self):
        """Describes the zoning potential as a float value 
        between 0(low) and 1(high)"""
        return self._zoning

    @property
    def rushdown(self):
        """Describes the rushdown potential as a float value 
        between 0(low) and 1(high)"""
        return self._rushdown

    @property
    def focus(self):
        """Defines the playstyle more, multiple values:
        -Neutral
        -Combos
        -Mixup
        -Condition"""
        return self._focus

    @property
    def range(self):
        """Range can be, single value:
        -Short
        -Mid
        -Long
        -All"""
        return self._combat_range

    @property
    def gender(self):
        """The gender of the character, single value"""
        return self._gender

    @property
    def priority(self):
        """I have no idea/catch all, but can be the following, multiple values possible:
        -Rounded
        -Mobility
        -Utility
        -Damage
        -HP"""
        return self._priority

    @property
    def reliance(self):
        """Describes the Reliance on Resources, one value only:
        -Normal
        -Mid
        -Reliant"""
        return self._reliance

    @property
    def resource(self):
        """Describes the type of ressource, one value only:
        -Normal
        -Dual (a whole second meter to manage and needs to recharge)
        -Resource"""
        return self._resource

    @property
    def moral(self):
        """Describes the morality of the character,one value only:
        -Good
        -Grey
        -Neutral
        -Evil"""
        return self._moral

    @property
    def reversal(self):
        """Describes the form of reversal,one value only:
        -DP (dragon punch)
        -Meter (needs meter)
        -None (has no, duh)"""
        return self._reversal

    @property
    def stance(self):
        """Does the Character have a stance,one value only:
        -Yes
        -No"""
        return self._stances

    @property
    def vortex(self):
        """Describes the Vortex(?),one value only:
        -Basic
        -Projectile
        -Million (Milia Rage,Zato-1, I-No)"""
        return self._vortex

    @property
    def mixup(self):
        """A closer description of the Mixup, multiple values possible:
        -CGrab (commandgrab)
        -RISC
        -FrameTraps
        -HighLow
        -Unblockable
        -LeftRight"""
        return self._mixups

    @property
    def oneplayer(self):
        """Describe if the playstyle of the character is one-sided, when active, one value only:
        -Kinda
        -No
        -Yes"""
        return self._oneplayer

    @property
    def setplay(self):
        """Describes the type of setplay for the character, multiple values possible:
        -None
        -Knockdown
        -Neutral
        -Basic"""
        return self._setplay

    @property
    def charge(self):
        """Describes the amount of Charge Moves and importance, one value only:
        -None
        -Lots
        -Little (Leo only)"""
        return self._charge

    @property
    def projectile(self):
        """the amount of projectiles the character has, multiple values possible:
        -Limited
        -Standard
        -Special
        -None"""
        return self._projectile

    @property
    def points(self):
        """is a float value"""
        return self._points

    @points.setter
    def points(self, value):
        self._points += value


if __name__ == "__main__":
    print("debug run - This is for testing purpose only. This modul should\
            be imported")
    shoutout()
