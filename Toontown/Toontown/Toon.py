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

Yippie = Actor({'Torso':'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam', \
             'Legs':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam'}, \
             {'Torso':{'Idle': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam', \
             'TorsoAnim':'phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam'}, \
             'Legs':{'Idle':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam',
             'LegsAnim':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral.bam'}})

Yippie.attach('Torso', 'Legs', 'joint_hips')

#Animations
Yippie.loop('TorsoAnim')
Yippie.loop('LegsAnim')

#Pos, Hpr, Scale, ReparentTo
Yippie.setPos(0, 0, 0)
Yippie.setHpr(0, 0, 0)
Yippie.setScale(1.1)
Yippie.reparentTo(render)

#Head
Head = Actor('phase_3/models/char/mouse-heads-1000.bam',
            {'anim':'phase_3/models/char/tt_a_chr_dgm_skirt_head_neutral.bam'})

Head.setColor(1, 1, 1)
Head.loop('anim')
Head.find('**/ears').setColor(0)
Head.find('**/muzzle').setColor(0.87, 0.65, 0.47)
Top_Head = Head.find('**/head')
Bot_Head = Head.find('**/head-front')

Neck = Yippie.find('**/def_head')
Head.reparentTo(Neck)

#******************************Clothes******************************


#Gloves
Gloves = Yippie.find('**/hands')
Gloves.setColor(0.99, 0.99, 0.99)

#Sleeves
Sleeves = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotCrusher.jpg')
Yippie.find('**/sleeves').setTexture(Sleeves, 1)

#Shirts
Shirt = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirt_sellbotCrusher.jpg')
Yippie.find('**/torso-top').setTexture(Shirt, 1)

#Shorts
Shorts = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg')
Yippie.find('**/torso-bot').setTexture(Shorts, 1)

#Shoes/Boots
Shoes = loader.loadTexture('phase_4/maps/tt_t_chr_avt_acc_sho_athleticBlack.jpg')
Yippie.find('**/shoes').setTexture(Shoes, 1)
Yippie.find('**/boots_long').hide()
Yippie.find('**/boots_short').hide()
Yippie.find('**/feet').hide()

#Glasses
Glasses = loader.loadModel('phase_4/models/accessories/tt_m_chr_avt_acc_msk_3dGlasses.bam')
Glasses.reparentTo(Bot_Head)
Glasses.setZ(0.25)
Glasses.setHpr(180.00, 350.00, 0.00)
Glasses.setScale(0.35)

#Colors
Top_Head.setColor(0.992188, 0.480469, 0.167969, 1.0)
Bot_Head.setColor(0.992188, 0.480469, 0.167969, 1.0)
Yippie.find('**/neck').setColor(0.304688, 0.96875, 0.402344, 1.0)
Yippie.find('**/arms').setColor(0.304688, 0.96875, 0.402344, 1.0)
Yippie.find('**/legs').setColor(0.992188, 0.480469, 0.167969, 1.0)
Yippie.find('**/feet').setColor(0.992188, 0.480469, 0.167969, 1.0)
Hat.setColor(0.99, 0.99, 0.99)
Glasses.setColor(0.99, 0.99, 0.99)

base.oobe()
run()

