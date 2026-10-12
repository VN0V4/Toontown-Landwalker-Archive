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

#Toon Torso
Toon = Actor("Custom Things/tt_a_chr_dgm_shorts_torso_1000")
Toon.reparentTo(render)
Toon.loop('neutral')
#toon head
toonhead = Actor("phase_3\models\char\mouse-heads-1000.bam")
toonhead.reparentTo(Toon.find('***joint_head')
#toon legs
Toonlegs = Actor("phase_3\models\char/tt_a_chr_dgm_shorts_legs_1000.bam")
Toonlegs.reparentTo(Toon.find("***joint_hips"))

run()
base.oobe()
