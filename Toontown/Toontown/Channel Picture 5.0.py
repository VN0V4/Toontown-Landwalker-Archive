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

Whiskers = Actor({'Torso': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam', \
                  'Legs': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam'}, \
                 {'Torso': {'Idle': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam', \
                            'TorsoAnim': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_neutral.bam'}, \
                  'Legs': {'Idle': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam',
                           'LegsAnim': 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral.bam'}})

Whiskers.attach('Torso', 'Legs', 'joint_hips')

# Animations
Whiskers.loop('TorsoAnim')
Whiskers.loop('LegsAnim')

# Pos, Hpr, Scale, ReparentTo
Whiskers.setPos(0, 0, 0)
Whiskers.setHpr(0, 0, 0)
Whiskers.setScale(0.90)
Whiskers.reparentTo(render)

# Head
Head = loader.loadModel('phase_3/models/char/mouse-heads-1000.bam')
Head.find('**/muzzle-short-surprise').hide()
Head.find('**/muzzle-short-sad').hide()
Head.find('**/muzzle-short-smile').hide()
Head.find('**/muzzle-short-angry').hide()
Head.find('**/muzzle-short-laugh').hide()
Head.find('**/head-long').hide()
Head.find('**/head-front-long').hide()
Head.find('**/eyes-long').hide()
Head.find('**/joint_pupilL_long').hide()
Head.find('**/joint_pupilR_long').hide()
Head.find('**/ears-long').hide()

Neck = Whiskers.find('**/def_head')
Head.reparentTo(Neck)

# ******************************Clothes******************************


# Gloves
Gloves = Whiskers.find('**/hands')
Gloves.setColor(0.99, 0.99, 0.99)

# Sleeves
Sleeves = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotCrusher.jpg')
Whiskers.find('**/sleeves').setTexture(Sleeves, 1)

# Shirts
Shirt = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirt_sellbotCrusher.jpg')
Whiskers.find('**/torso-top').setTexture(Shirt, 1)

# Shorts
Shorts = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg')
Whiskers.find('**/torso-bot').setTexture(Shorts, 1)

# Shoes/Boots
Shoes = loader.loadTexture('phase_4/maps/tt_t_chr_avt_acc_sho_athleticBlack.jpg')
Whiskers.find('**/shoes').setTexture(Shoes, 1)
Whiskers.find('**/shoes').setScale(1.1)
Whiskers.find('**/boots_long').hide()
Whiskers.find('**/boots_short').hide()
Whiskers.find('**/feet').hide()

# Hats
# Hat = loader.loadModel('phase_4/models/accessories/tt_m_chr_avt_acc_hat_topHat.bam')
# Hat.reparentTo(Head.find('**/head-short'))
# Hat.setPos(0, -0.10, 0.75)
# Hat.setHpr(180.00, 350.00, 0)
# Hat.setScale(0.45)

# Glasses
#Glasses = loader.loadModel('phase_4/models/accessories/tt_m_chr_avt_acc_msk_3dGlasses.bam')
#Glasses.reparentTo(Head.find('**/head-front-short'))
#Glasses.setZ(0.30)
#Glasses.setHpr(180, 350.00, 0)
#Glasses.setScale(0.40)

# Colors
Head.find('**/head-short').setColor(0.25, 0.52, 0.99, 1.0)
Head.find('**/head-front-short').setColor(0.25, 0.52, 0.99, 1.0)
Head.find('**/ears-short').setColor(0.25, 0.52, 0.99, 1.0)
Whiskers.find('**/neck').setColor(0.25, 0.52, 0.99, 1.0)
Whiskers.find('**/arms').setColor(0.25, 0.52, 0.99, 1.0)
Whiskers.find('**/legs').setColor(0.25, 0.52, 0.99, 1.0)
Whiskers.find('**/feet').setColor(0.25, 0.52, 0.99, 1.0)
# Hat.setColor(0.99, 0.99, 0.99)
#Glasses.setColor(0.99, 0.99, 0.99)

base.oobe()
run()

