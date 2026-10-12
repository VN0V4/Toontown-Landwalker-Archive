# Others
from panda3d.core import loadPrcFile

if __debug__:
	loadPrcFile("Config/Config.prc")


from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from pandac.PandaModules import Point3
from pandac.PandaModules import *

import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import Vec3, Vec4, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject


class Window(ShowBase):

	def __init__(self):
		self.loadToon()
		
	def loadToon(self):
		legs = Actor("phase_3\models\char/tt_a_chr_dgm_shorts_legs_1000.bam")
		torso = Actor("phase_3\models\char/tt_a_chr_dgm_shorts_torso_1000.bam")
		head = Actor("phase_3\models\char\mouse-heads-1000.bam")
		self.body = Actor({'legs': legs, 'torso': torso, 'head': head},
					{"legs": {"neutral":"phase_3\models\char\mouseHeads.bam"},
					'torso': {"neutral":"phase_3\models\char\tt_a_chr_dgm_shorts_torso_neutral.bam"},
					'head': {"neutral":"phase_3\models\char\tt_a_chr_dgm_shorts_head_neutral.bam"}},
	self.body.attach("torso", "legs", 'joint_hips'),
	self.body.attach("head", 'torso', 'def_head'),
	self.body.reparentTo(self.render),
	self.body.loop('neutral'))

base.run()
base.oobe()
