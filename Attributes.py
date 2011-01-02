# Attributes.py
# Stats for Player
#
# (c) 2011 Xenlus Group
#
# This software is provided as-is, with GNU GPLv3 License attached. You are
# required to retain a full copyright and the attached License if you released
# or modified any of the code.
#
# Permission is granted to use this software for any legal purpose, provided
# you give copyright to Xenlus and retain the attached License file.
# If you do manage to construct something for distribution with this code, it
# would be nice (but not required) to include a link back to
# http://www.xenlus.com

AttributeNames = ["Level", "Health", "PDamage", "PDefence", "Speed"]
# Abbreviations means shorten therefore this variable is just to
# shorten the AttributeNames.
AttributeAbbreviations = ["Lvl", "Hp", "PDmg", "PDef", "Spd"]
# Temporary idea for skills
Ability = ["Cunning", "Negotiate", "Bully", "Flame"]

class Attributes:
    def __init__(self):
    	# Pre-defined Stats. Fetching player stats from somewhere(database or text file)
        self.Stats = [0,0,0,0,0]
        self.Abilities = dict()

    def IncreaseAttribute(self,attrName,amount):
        try:
            attrIndex = AttributeAbbreviations.index(attrName)
        except:
            try:
                attrIndex = AttributeNames.index(attrName)
            except:
                attrIndex = 0
        self.Stats[attrIndex] += amount

    # Fetch Attribute Positioning and return it
    def GetAttribute(self, attrName):
        try:
            attrIndex = AttributeAbbreviations.index(attrName)
        except:
            try:
                attrIndex = AttributeNames.index(attrName)
            except:
                return 0
        return self.Stats[attrIndex]
        
    def IncreaseAbility(self, abiliName2, amount):
    	abiliName = abiliName2.capitalize()
    	if(self.Abilities.has_key(abiliName)):
    		self.Abilities[abiliName] += amount
    	else:
    		self.Abilities[abiliName] = amount
