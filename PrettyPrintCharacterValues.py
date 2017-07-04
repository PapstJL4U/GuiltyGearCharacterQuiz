"""This module just prints the Character Values in a nice format"""
import CharacterValues as CV

version = 'rev2-0.1'
author = 'Pride and Prejudice aka PapstJL4U'

"""
_default = Character(fullname="", charname="", Tier="",
                     Playstyle="", Skill="", Zoning=0.0,
                     Rushdown=1.0, Focus="",
                     Range="", Gender="", Priority="",
                     Reliance="", Resource="", Moral="",
                     Reversal="", Stances="", Vortex="",
                     Mixups="", OnePlayer="", SetPlay="",
                     Charge="", Projectile="", Points=0.0)
"""


def showstuff(char):
    """Prints all attributes of char. Char is a GG Char as defined in CharacterData.py"""
    line1 = "The fullname is: " + char.fullname
    line2 = "charname: " + char.charname
    line3 = "Tier:" + char.tier + "  Playstyle:" + char.playstyle + "  Skilllevel:" + char.skill
    line4 = "Zoning:" + str(char.zoning) + "  Rushdown:" + str(char.rushdown) + "  Focus:" + char.focus
    line5 = "Range:" + char.range + "  Gender:" + char.gender + "  Priority:" + char.priority
    line6 = "Reliance:" + char.reliance + "  Resource:" + char.reliance + "  Moral:" + char.moral
    line7 = "Reversaltype:" + char.reversal + "  Stance:" + char.stance + "  Vortex:" + char.vortex
    line8 = "Mixuptypes:" + char.mixup + "  1-P Game:" + char.oneplayer + "  and has SetPlay:" + char.setplay
    line9 = "Chargemoves:" + char.charge + "  Tyes of Projectiles:" + char.projectile + "  default Points(0):" + str(
        char.points)
    lines = (line1, line2, line3, line4, line5, line6, line7, line8, line9)
    return lines


def showstufflong(char):
    locallist = [char.fullname]
    dic = vars(char)
    for attribute in dic:
        locallist.append(str(attribute).lstrip('_') + ':' + str(dic[attribute]))
    return locallist


def printtoconsole(long):
    for char in CV.character_list_beta:
        if long:
            printme = showstufflong(char)
        else:
            printme = showstuff(char)
        for line in printme:
            print(line)
        print("=" * 80)


def generatetextfile(long):
    if long:
        file = open("genfiles/longCharacterData.txt", mode='w')
    else:
        file = open("genfiles/shortCharacterData.txt", mode='w')

    for char in CV.character_list_beta:
        if long:
            printme = showstufflong(char)
        else:
            printme = showstuff(char)
        for line in printme:
            file.write(line + '\n')
        file.write("=" * 80 + '\n')
    file.close()


if __name__ == "__main__":
    printtoconsole(True)
    generatetextfile(True)
