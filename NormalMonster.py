# Monster Information
# Stats for normal monster
#
# (c) 2010 Xenlus Group
#
# This software is provided as-is, with GNU GPLv3 License attached. You are
# required to give a full copyright and the attached License if you released
# or modified any of the code.
#
# Permission is granted to use this software for any legal purpose, provided
# you give copyright to Xenlus and retain the attached License file.
# If you do manage to construct something for distribution with this code, it
# would be nice (but not required) to include a link back to
# http://www.xenlus.com

import Attributes

class Monster():
    def __init__(self):
        self.Stats = [4,4,4,4,4]
        self.Skills = dict()
        self.Level = 0

    def GetLevel(self):
