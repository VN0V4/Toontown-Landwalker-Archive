#Heyyy glad you made it this far :D
#So this is the place where you start working with the models by putting them together.
#Before you can do anything you need to copy and paste the code below to your PutYourNameHere.py file.

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
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject

#After that it's time to start coding!
#First we're going to need a terrain and here's how it works.

terrain = loader.loadModel('phase_12/models/bossbotHQ/BanquetInterior_1.bam')
terrain.reparentTo(render)

#The yellow text there is like an instruction for the program to find the right model.
#You can use different models by editing it.
#Be careful though! All the names have to be exact, otherwise it won't find the model.

#The ''terrain'' is the name of the model.
#It has to remain exactly the same for the commands to work.
#If you change it, you'll have to change the other lines too.

#Now let's add a piano to the terrain.

piano = loader.loadModel('phase_5.5/models/estate/Piano.bam')
piano.reparentTo(render)
piano.place()

#piano.place() gives you a panel where you can move the model.

#Before we can run it we need the code below to the end. Deltete the ''#'' for the code to activate.

#base.oobe()
#run()

#base.oobe() let's you move around.
#Click on run and a Placer Panel will appear with the terrain and a piano.
#The piano is out of place so use the Placer Panel to move it where you want.

#After you've found a good place for your piano look at the numbers on Position, Oriantation and Scale Uniform.
#Go back to your piano code and put in this code.

#piano.setZ(6.17)
#Take away the ''#'' this will actiave the code.
#Do the same with the others. For example:

#piano.setX(-1.24)
#piano.setScale(1.77)
#piano.setH(53.13)

#Change the number I have (TheNumber) to the number you have on the Placer Panel.
#After you're done you can delete piano.place() and the placer panel will go away the next time you run it.

#Here are some more models for example.
#You can also run this file to see the result :)

ship = loader.loadModel('phase_5/models/props/ship.bam')
ship.reparentTo(render)
ship.setX(73.54)
ship.setY(337.66)
ship.setH(233.13)
#ship.place()

train = loader.loadModel('phase_5/models/props/train.bam')
train.reparentTo(render)
train.setX(-55.79)
train.setY(355.79)
train.setH(121.76)
#train.place()


base.oobe()
run()

#Have fun!
