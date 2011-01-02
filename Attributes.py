# Attributes.py
# Stats for all
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

AttributeNames = ["Health", "PDamage", "PDefence", "Speed"]
AttributeAbbreviations = ["Hp", "PDmg","PDef", "Spd"]

class Attributes:
    def __init__(self):
        self.Stats = [0,0,0,0]

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
