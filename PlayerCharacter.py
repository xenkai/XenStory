# PlayerCharacter
# Game-Rule Information for the player's "character"
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

import PlayerStats

EquipSlotNames = ['Running Ball', 'Quest Item', 'Name Tag']
SlotTypeName = {3:'Running Ball', 4:'Quest Item', 5:'Name Tag'}

class PlayerCharacter(PlayerStats.PlayerStats):
	
	def __init__(self):
		PlayerStats.PlayerStats.__init__(self)
		self.name = "Player"
		self.ExperiencePoints = 0
		self.Equip = dict()
		self.LevelupFlag = 0
		for x in EquipSlotNames:
			self.Equipment[x] = None
			
	def GetExperience(self):
		return self.ExperiencePoints
		
	def GainExperience(self, amount):
		self.ExperiencePoints += amount
		level = self.Attributes.GetAttribute("Lvl")
		if (level < 10):
			ExpRequired = (((level*level*2+1000)/2) * 100)-100
		else:
			ExpRequired = 75000+(25000 * (level-10))
		if(self.ExperiencePoints >= ExpRequired) and (level < 20):
			self.LevelupFlag = 1
		self.FlagStatChange(1)
