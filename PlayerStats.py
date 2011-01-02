# Player Information
# Stats for player
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

import Attributes


# This are basic fetching stats for Player, in time there will be different
# types of monster and the handling will need to be changed to something else
# to cover all the stats from each player.
# This is to be done when the game is ready to be Multiplayer.
class Player():
    def __init__(self):
        self.Attributes = Attributes.Attributes()

    def SetHp(self):
        return self.Attributes.IncreaseAttribute("Hp", 100)
    
    def SetPDmg(self):
        return self.Attributes.IncreaseAttribute("PDmg", 10)

    def SetPDef(self):
        return self.Attributes.IncreaseAttribute("PDef", 10)

    def SetSpd(self):
        return self.Attributes.IncreaseAttribute("Spd", 1)

    def GetAttributes(self):
        return self.Attributes
