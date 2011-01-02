# GameObject
# This defines a very basic Game Object. This object has a type, and ID, and
# contents (every object is a potential container).
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

import Position

class cObjectIDMaster:
	
	def __init__(self):
		self.Reset()
		
	def GetUniqueID(self):
		p = self.nextUniqueID
		self.nextUniqueID += 1
		return p
		
	def Reset(self):
		self.nextUniqueID = 1
		
	def DeclareObject(self, objectID):
		self.nextUniqueID = objectID + 1
		
# Global Warning
ObjectIDMaster = cObjectIDMaster()

class GameObject:
	def __init__(self):
		self.position = Position.Position()
		self.ID = ObjectIDMaster.GetUniqueID() # -1 means no ID assigned
		self.type = 0 # Type 0 means nothing
		self.contents = [] # Contents is what this object contains
		
	def GetType(self):
		return self.type
		
	def SetType(self, type):
		self.type = type
		
	def GetID(self):
		# Assign ID if we do not have an ID yet
		if(self.ID < 0):
			self.ID = ObjectIDMaster.GetUniqueID()
		return self.ID
		
	def Position(self):
		return self.position
		
	def SetPosition(self, posX, posY):
		self.Position.X = posX
		self.Position.Y = posY
		
	def GetContents(self):
		return self.contents
		
	def Display(self, offsetX, offsetY, displayInfo, graphicsData):
		pass
