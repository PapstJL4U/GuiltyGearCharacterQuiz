"""In this modul, we put the actual values of the characters into the 
class instances. I hope it is better for readability."""
version = 'rev2-0.1'
author = 'Pride and Prejudice aka PapstJL4U'

from CharacterData import Character

_default = Character(fullname="", charname="", Tier="",
                     Playstyle="", Skill="", Zoning=0.0,
                     Rushdown=1.0, Focus="",
                     Range="", Gender="", Priority="",
                     Reliance="", Resource="", Moral="",
                     Reversal="", Stances="", Vortex="",
                     Mixups="", OnePlayer="", SetPlay="",
                     Charge="", Projectile="", Points=0.0)

sol = Character(fullname="Sol Badguy", charname="sol", Tier="High",
                Playstyle="Prepared", Skill="New", Zoning=0.0,
                Rushdown=1.0, Focus="Condition, Damage",
                Range="Short, Mid", Gender="Male", Priority="Rounded",
                Reliance="Normal", Resource="Normal", Moral="Grey",
                Reversal="DP", Stances="No", Vortex="Basic",
                Mixups="CGrab, RISC", OnePlayer="Kinda", SetPlay="None",
                Charge="None", Projectile="Limited", Points=0.0)

ky = Character(fullname="Ky Kiske", charname="ky", Tier="High",
               Playstyle="Prepared", Skill="New", Zoning=0.5,
               Rushdown=0.5, Focus="Neutral, Condition",
               Range="All", Gender="Male", Priority="Rounded",
               Reliance="Mid", Resource="Resource", Moral="Good",
               Reversal="DP", Stances="No", Vortex="Projectile",
               Mixups="FrameTraps", OnePlayer="No", SetPlay="Knockdown",
               Charge="None", Projectile="Standard", Points=0.0)

may = Character(fullname="May", charname="may", Tier="Mid",
                Playstyle="Prepared", Skill="Mid", Zoning=0.25,
                Rushdown=0.75, Focus="Combos",
                Range="Mid", Gender="Female", Priority="Utility, Mobility",
                Reliance="Reliant", Resource="Resource", Moral="Neutral",
                Reversal="Meter", Stances="No", Vortex="Projectile",
                Mixups="CGrab, HighLow", OnePlayer="No", SetPlay="Neutral, Knockdown",
                Charge="Lots", Projectile="Limited, Special", Points=0.0)

faust = Character(fullname="Faust", charname="faust", Tier="Mid",
                  Playstyle="Special", Skill="new", Zoning=1.0,
                  Rushdown=0.0, Focus="Neutral",
                  Range="Mid, Long", Gender="Male", Priority="Utility",
                  Reliance="Reliant", Resource="Resource", Moral="Neutral",
                  Reversal="Meter", Stances="No", Vortex="Basic",
                  Mixups="Unblockable", OnePlayer="No", SetPlay="Neutral",
                  Charge="None", Projectile="Limited, Special", Points=0.0)

millia = Character(fullname="Millia Rage", charname="millia", Tier="High",
                   Playstyle="Special", Skill="Mid", Zoning=0.0,
                   Rushdown=1.0, Focus="Mixup, Neutral",
                   Range="Mid, Short", Gender="Female", Priority="Mobility, Utility",
                   Reliance="Mid", Resource="Resource", Moral="Grey",
                   Reversal="Meter", Stances="No", Vortex="Million",
                   Mixups="HighLow", OnePlayer="Yes", SetPlay="Knockdown",
                   Charge="None", Projectile="Special, Limited", Points=0.0)

chipp = Character(fullname="Chipp Zanuff", charname="chipp", Tier="Mid",
                  Playstyle="Prepared", Skill="Old", Zoning=0.5,
                  Rushdown=0.5, Focus="Condition, Neutral",
                  Range="Short", Gender="Male", Priority="Mobility, Utility",
                  Reliance="Normal", Resource="Normal", Moral="Good",
                  Reversal="DP", Stances="No", Vortex="Basic",
                  Mixups="LeftRight, HighLow", OnePlayer="Kinda", SetPlay="Basic",
                  Charge="None", Projectile="Limited", Points=0.0)

ino = Character(fullname="I-No", charname="ino", Tier="Mid",
                Playstyle="Rewarding", Skill="Old", Zoning=0.0,
                Rushdown=1.0, Focus="Mixup, Damage",
                Range="Short", Gender="Female", Priority="Mobility",
                Reliance="Mid", Resource="Normal", Moral="Evil",
                Reversal="Meter", Stances="No", Vortex="Million",
                Mixups="HighLow", OnePlayer="Yes", SetPlay="Neutral",
                Charge="None", Projectile="Special", Points=0.0)

axl = Character(fullname="Axl Low", charname="axl", Tier="Mid",
                Playstyle="Special", Skill="Mid", Zoning=1.0,
                Rushdown=0.0, Focus="Neutral, Condition",
                Range="Mid, Long", Gender="Male", Priority="Rounded",
                Reliance="Normal", Resource="Normal", Moral="Neutral",
                Reversal="DP", Stances="Yes", Vortex="Basic",
                Mixups="FrameTraps, RISC", OnePlayer="Kinda", SetPlay="None",
                Charge="Lots", Projectile="None", Points=0.0)

venom = Character(fullname="Venom", charname="venom", Tier="Mid",
                  Playstyle="Rewarding", Skill="Old", Zoning=0.75,
                  Rushdown=0.25, Focus="Neutral",
                  Range="Mid, Long", Gender="Male", Priority="Utility",
                  Reliance="Reliant", Resource="Resource", Moral="Neutral",
                  Reversal="None", Stances="No", Vortex="Projectile",
                  Mixups="RISC", OnePlayer="Kinda", SetPlay="Neutral",
                  Charge="Lots", Projectile="Standard, Special", Points=0.0)

zato = Character(fullname="Zato=1", charname="zato", Tier="High",
                 Playstyle="Special", Skill="Old", Zoning=0.25,
                 Rushdown=0.75, Focus="Combos, Mixup",
                 Range="All", Gender="Male", Priority="Utility, Damage",
                 Reliance="Reliant", Resource="Dual", Moral="Neutral",
                 Reversal="Meter", Stances="Yes", Vortex="Million",
                 Mixups="Unblockable, CGrab, RISC", OnePlayer="Yes", SetPlay="Neutral",
                 Charge="None", Projectile="Special", Points=0.0)

slayer = Character(fullname="Slayer", charname="slayer", Tier="Low",
                   Playstyle="Rewarding", Skill="Old", Zoning=0.0,
                   Rushdown=1.0, Focus="Combos",
                   Range="Short", Gender="Male", Priority="Damage, Mobility",
                   Reliance="Normal", Resource="Normal", Moral="Grey",
                   Reversal="Meter", Stances="No", Vortex="Basic",
                   Mixups="LeftRight, FrameTrap", OnePlayer="No", SetPlay="None",
                   Charge="None", Projectile="None", Points=0.0)

potemkin = Character(fullname="Potemkin", charname="potemkin", Tier="Low",
                     Playstyle="Rewarding", Skill="Old", Zoning=0.0,
                     Rushdown=0.0, Focus="Condition",
                     Range="Short", Gender="Male", Priority="HP, Damage",
                     Reliance="Normal", Resource="Normal", Moral="Neutral",
                     Reversal="Meter", Stances="No", Vortex="Basic",
                     Mixups="CGrab", OnePlayer="No", SetPlay="None",
                     Charge="Lots", Projectile="None", Points=0.0)

ram = Character(fullname="Ramlethal Valentine", charname="ram", Tier="Low",
                Playstyle="Rewarding", Skill="Mid", Zoning=0.25,
                Rushdown=0.75, Focus="Mixup",
                Range="Mid", Gender="Female", Priority="Utility",
                Reliance="Reliant", Resource="Resource", Moral="Neutral",
                Reversal="Meter", Stances="Yes", Vortex="Projectile",
                Mixups="HighLow, CGrab", OnePlayer="Yes", SetPlay="Knockdown",
                Charge="None", Projectile="Limited", Points=0.0)

bedman = Character(fullname="Bedman", charname="bedman", Tier="Mid",
                   Playstyle="Special", Skill="Mid", Zoning=0.25,
                   Rushdown=0.75, Focus="Neutral",
                   Range="All", Gender="Male", Priority="Utility, Mobility, HP",
                   Reliance="Reliant", Resource="Dual", Moral="Evil",
                   Reversal="Meter", Stances="No", Vortex="Projectile",
                   Mixups="LeftRight, HighLow, RISC", OnePlayer="Kinda", SetPlay="Neutral, Knockdown",
                   Charge="Nine", Projectile="Standard", Points=0.0)

sin = Character(fullname="Sin Kiske", charname="sin", Tier="High",
                Playstyle="Prepared", Skill="New", Zoning=0.0,
                Rushdown=1.0, Focus="Neutral, Combos",
                Range="Mid", Gender="Male", Priority="Damage",
                Reliance="Reliant", Resource="Dual", Moral="Good",
                Reversal="DP", Stances="No", Vortex="Basic",
                Mixups="FrameTraps, RISC", OnePlayer="Kinda", SetPlay="Knockdown",
                Charge="None", Projectile="Special", Points=0.0)

elphelt = Character(fullname="Elphelt Valentine", charname="elphelt", Tier="High",
                    Playstyle="Prepared", Skill="Mid", Zoning=0.25,
                    Rushdown=0.75, Focus="Neutral, Combos",
                    Range="All", Gender="Female", Priority="Damage, Utility, Rounded",
                    Reliance="Mid", Resource="Normal", Moral="Good",
                    Reversal="Meter", Stances="Yes", Vortex="Basic",
                    Mixups="RISC, FrameTrap, Unblockable", OnePlayer="Kinda", SetPlay="Knockdown",
                    Charge="None", Projectile="Special", Points=0.0)

leo = Character(fullname="Leo Whitefang", charname="leo", Tier="Low",
                Playstyle="Rewarding", Skill="New", Zoning=0.0,
                Rushdown=1.0, Focus="Combos, Mixup",
                Range="Short", Gender="Male", Priority="Damage,HP",
                Reliance="Normal", Resource="Normal", Moral="Good",
                Reversal="DP", Stances="Yes", Vortex="Basic",
                Mixups="RISC, LeftRight, HighLow", OnePlayer="No", SetPlay="None",
                Charge="Little", Projectile="Standard", Points=0.0)

jacko = Character(fullname="Jack-O Valentine", charname="jacko", Tier="Mid",
                  Playstyle="Special", Skill="New", Zoning=1.0,
                  Rushdown=0.0, Focus="Mixup",
                  Range="All", Gender="Female", Priority="Utility",
                  Reliance="Reliant", Resource="Dual", Moral="Evil",
                  Reversal="DP", Stances="No", Vortex="Basic",
                  Mixups="RISC, HighLow", OnePlayer="Yes", SetPlay="Neutral",
                  Charge="None", Projectile="Limited", Points=0.0)

jam = Character(fullname="Jam Kuradoberi", charname="jam", Tier="Low",
                Playstyle="Rewarding", Skill="Mid", Zoning=0.0,
                Rushdown=1.0, Focus="Combos",
                Range="Short", Gender="Female", Priority="Damage, Mobility",
                Reliance="Mid", Resource="Resource", Moral="Neutral",
                Reversal="DP", Stances="No", Vortex="Basic",
                Mixups="FrameTraps, RISC", OnePlayer="No", SetPlay="None",
                Charge="None", Projectile="None", Points=0.0)

johnny = Character(fullname="Johnny Sfondi", charname="johnny", Tier="High",
                   Playstyle="Special", Skill="Old", Zoning=0.0,
                   Rushdown=1.0, Focus="Combos",
                   Range="Mid", Gender="Male", Priority="Damage",
                   Reliance="Mid", Resource="Dual", Moral="Good",
                   Reversal="Meter", Stances="Yes", Vortex="Basic",
                   Mixups="Unblockable, RISC, FrameTraps", OnePlayer="Kinda", SetPlay="Knockdown",
                   Charge="None", Projectile="Limited", Points=0.0)

kum = Character(fullname="Kum Haehyun", charname="kum", Tier="Low",
                Playstyle="Prepared", Skill="Mid", Zoning=0.25,
                Rushdown=0.75, Focus="Combos, Mixup",
                Range="All", Gender="Female", Priority="Damage, HP, Rounded",
                Reliance="Normal", Resource="Normal", Moral="Good",
                Reversal="Meter", Stances="No", Vortex="Projectile",
                Mixups="HighLow", OnePlayer="No", SetPlay="Knockdown",
                Charge="None", Projectile="Standard", Points=0.0)

raven = Character(fullname="Raven", charname="raven", Tier="High",
                  Playstyle="Prepared", Skill="New", Zoning=0.5,
                  Rushdown=0.5, Focus="Neutral",
                  Range="All", Gender="Male", Priority="Rounded",
                  Reliance="Normal", Resource="Normal", Moral="Evil",
                  Reversal="Meter", Stances="Yes", Vortex="Projectile",
                  Mixups="CGrab, HighLow", OnePlayer="No", SetPlay="Knockdown",
                  Charge="None", Projectile="Standard", Points=0.0)

dizzy = Character(fullname="Dizzy", charname="dizzy", Tier="Low",
                  Playstyle="Special", Skill="Mid", Zoning=0.75,
                  Rushdown=0.25, Focus="Mixup, Combos",
                  Range="Long", Gender="Female", Priority="Utility",
                  Reliance="Reliant", Resource="Resource", Moral="Good",
                  Reversal="Meter", Stances="No", Vortex="Projectile",
                  Mixups="HighLow", OnePlayer="Kinda", SetPlay="Neutral",
                  Charge="None", Projectile="Special", Points=0.0)

_baiken = Character(fullname="Baiken", charname="baiken", Tier="Low",
                    Playstyle="Rewarding", Skill="Mid", Zoning=0.15,
                    Rushdown=0.50, Focus="Neutral",
                    Range="Short", Gender="Female", Priority="Damage, Utility",
                    Reliance="Normal", Resource="Normal", Moral="Grey",
                    Reversal="Meter", Stances="Yes", Vortex="Basic",
                    Mixups="LeftRight, CGrab, HighLow", OnePlayer="No", SetPlay="Knockdown",
                    Charge="None", Projectile="Limited", Points=0.0)

_answer = Character(fullname="Answer", charname="answer", Tier="Low",
                    Playstyle="Special", Skill="Old", Zoning=0.5,
                    Rushdown=0.5, Focus="Combos, Neutral ",
                    Range="All", Gender="Male", Priority="Utility",
                    Reliance="Reliant", Resource="Resource", Moral="Good",
                    Reversal="?", Stances="Yes", Vortex="Projectile",
                    Mixups="HighLow, LeftRight", OnePlayer="No", SetPlay="Knockdown",
                    Charge="None", Projectile="Limited, Special", Points=0.0)

character_list = (sol, ky, may, faust, millia, chipp, ino, axl, venom, zato,
                  slayer, potemkin, ram, bedman, sin, elphelt, leo, jacko, jam,
                  johnny, kum, raven, dizzy)

character_list_beta = (sol, ky, may, faust, millia, chipp, ino, axl, venom, zato,
                       slayer, potemkin, ram, bedman, sin, elphelt, leo, jacko, jam,
                       johnny, kum, raven, dizzy, _baiken, _answer)


if __name__ == "__main__":
    print("Possible Error, This is an import only modul")
