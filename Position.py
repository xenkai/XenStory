# Position Information
# Position set within a place
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

class Position:
	
	def __init__(self):
		self.containerType = 0
		self.containerID = 0 	# ContainerID = 0 means nowhere
		self.roomID = 0 		# Room 0 is always the default - The starting room
		self.X = 0
		self.Y = 0
		
	def SetPosition(self,x,y):
		self.X = x
		self.Y = y
		return
		
	def PutInContainer(self, id, type=0):
		self.containerID = id
		self.containerType = type
		
	def MovetoRoom(self, roomId):
		self.roomID = roomId
		
	def GetContainer():
		return self.containerID
	
	def GetContainerType():
		return self.containerType
		
	def GetRoomID():
		return self.roomID
		
	def GetPosition():
		return (x,y)
