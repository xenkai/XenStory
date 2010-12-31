# Monster Information
# Stats for normal monster
#
# (c) 2010 Xenlus Group
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

import Attributes


# This are basic fetching stats from Monster, in time there will be different
# types of monster and the handling will need to be changed to XML to cover
# all the stats from each monster.
class Monster():
    def __init__(self):
        self.Attributes = Attributes.Attributes()

    def SetLevel(self):
        return self.Attributes.AdjustLevel(1)
    
    def GetLevel(self):
        return self.Attributes.GetLevel()

    def SetHp(self):
        return self.Attributes.IncreaseAttribute("Hp", 100)
    
    def SetPDmg(self):
        return self.Attributes.IncreaseAttribute("PDmg", 10)

    def SetPDef(self):
        return self.Attributes.IncreaseAttribute("PDef", 10)

    def SetMDmg(self):
        return self.Attributes.IncreaseAttribute("MDmg", 10)

    def SetMDef(self):
        return self.Attributes.IncreaseAttribute("MDef", 10)

    def SetSpd(self):
        return self.Attributes.IncreaseAttribute("Spd", 1)

    def GetAttributes(self):
        return self.Attributes
