#Others
from panda3d.core import loadPrcFile
if __debug__:
    loadPrcFile("Config/Config.prc")

#    from direct.showbase.ShowBase import ShowBase
    
    
from direct.directbase.DirectStart import *
from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import Point3
from pandac.PandaModules import *
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.showbase.Transitions import *
from direct.gui.DirectGui import *
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
from direct.filter.CommonFilters import *
from panda3d.ai import *
import sys

class LOAD:
	def loadGame(self):
		self.TRAINING_GROUND_SKY = loader.loadModel("TT_sky.bam")
		
		self.R3_BGM = loader.loadSfx("phase_4/audio/bgm/tt_s_ara_gen_fireworks_auldLangSyne.mid")
		self.R3_BGM.setLoop(True)
		self.R3_BGM.setVolume(1)



#class Game(ShowBase):
#    def __init__(self):
#        ShowBase.__init__(self)
#        
#        self.loadAudio()
#
#        def loadAudio(self):
#            music = self.loader.loadMusic("phase_4/audio/bgm/tt_s_ara_gen_fireworks_auldLangSyne.mid")
#            music.play()
#            music.setLoop(True)


#Character
from sys import argv
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *

text = ("toon")
textObject = OnscreenText(text=text, pos=(0, 0.2),
                          scale=0.06, fg=(0.1, 0, 0.9, 1), bg=(0.9, 0.9, 0.9, 1), align=TextNode.ACenter, mayChange=1)

title = WindowProperties()
title.setTitle("Toontown Central")
base.win.requestProperties(title)

base.disableMouse()

legsAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand-start.bam',
                'firehose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_firehose.bam',
                'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateL-putt.bam',
                'slip-forward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-forward.bam',
                'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eatnrun.bam',
                'tickle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_tickle.bam',
                'water-gun': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_water-gun.bam',
                'leverNeutral': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverNeutral.bam',
                'swim': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swim.bam',
                'catch-run': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gamerun.bam',
                'sad-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sad-neutral.bam',
                'pet-loop': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petloop.bam',
                'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zstart.bam',
                'wave': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_wave.bam',
                'reel-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelneutral.bam',
                'pole-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_poleneutral.bam',
                'bank': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_jellybeanJar.bam',
                'scientistGame': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistGame.bam',
                'right-hand': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand.bam',
                'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_lookloop-putt.bam',
                'victory': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_victory-dance.bam',
                'lose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_lose.bam',
                'cringe': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_cringe.bam',
                'right': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_right.bam',
                'headdown-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_headdown-putt.bam',
                'conked': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_conked.bam',
                'jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump.bam',
                'into-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_into-putt.bam',
                'fish-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishEND.bam',
                'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zend.bam',
                'shrug': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_shrug.bam',
                'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_sprinkle-dust.bam',
                'hold-bottle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-bottle.bam',
                'takePhone': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_takePhone.bam',
                'melt': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_melt.bam',
                'pet-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petin.bam',
                'look-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_look-putt.bam',
                'loop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_loop-putt.bam',
                'good-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_good-putt.bam',
                'juggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_juggle.bam',
                'run': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_run.bam',
                'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_press-button.bam',
                'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-back-right.bam',
                'water': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_water.bam',
                'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point-start.bam',
                'bad-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_bad-putt.bam',
                'struggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_struggle.bam',
                'running-jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_running-jump.bam',
                'callPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_callPet.bam',
                'throw': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_pie-throw.bam',
                'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eat_neutral.bam',
                'tug-o-war': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_tug-o-war.bam',
                'bow': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bow.bam',
                'swing': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swing.bam',
                'climb': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_climb.bam',
                'scientistWork': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistWork.bam',
                'think': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_think.bam',
                'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameThrow.bam',
                'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_walk.bam',
                'down': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_down.bam',
                'pole': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_pole.bam',
                'periscope': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_periscope.bam',
                'duck': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_duck.bam',
                'curtsy': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_curtsy.bam',
                'jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zend.bam',
                'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_loop_dig.bam',
                'angry': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_angry.bam',
                'bored': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bored.bam',
                'swing-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_swing-putt.bam',
                'pet-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petend.bam',
                'spit': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_spit.bam',
                'right-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point.bam',
                'start-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_into_dig.bam',
                'castlong': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_castlong.bam',
                'confused': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_confused.bam',
                'neutral': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral.bam',
                'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zhang.bam',
                'reel': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reel.bam',
                'slip-backward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-backward.bam',
                'sound': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_shout.bam',
                'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_sidestep-left.bam',
                'up': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_up.bam',
                'fish-again': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishAGAIN.bam',
                'cast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_cast.bam',
                'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneBack.bam',
                'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneNeutral.bam',
                'scientistJealous': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistJealous.bam',
                'battlecast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fish.bam',
                'sit-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_intoSit.bam',
                'toss': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_toss.bam',
                'happy-dance': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_happy-dance.bam',
                'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zstart.bam',
                'teleport': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_teleport.bam',
                'sit': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sit.bam',
                'sad-walk': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_losewalk.bam',
                'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props-start.bam',
                'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_book.bam',
                'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zhang.bam',
                'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistEmcee.bam',
                'leverPull': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverPull.bam',
                'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_tutorial-neutral.bam',
                'badloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_badloop-putt.bam',
                'give-props': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props.bam',
                'hold-magnet': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-magnet.bam',
                'hypnotize': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hypnotize.bam',
                'left-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_left-point.bam',
                'leverReach': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverReach.bam',
                'feedPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_feedPet.bam',
                'reel-H': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelH.bam',
                'applause': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_applause.bam',
                'smooch': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_smooch.bam',
                'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateR-putt.bam',
                'fish-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishneutral.bam',
                'push': 'phase_9/models/char/tt_a_chr_dgs_shorts_legs_push.bam',
                'catch-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameneutral.bam',
                'left': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_left.bam'}

torsoAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-hand-start.bam',
                 'firehose': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_firehose.bam',
                 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_rotateL-putt.bam',
                 'slip-forward': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_slip-forward.bam',
                 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_eatnrun.bam',
                 'tickle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_tickle.bam',
                 'water-gun': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_water-gun.bam',
                 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverNeutral.bam',
                 'swim': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_swim.bam',
                 'catch-run': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gamerun.bam',
                 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sad-neutral.bam',
                 'pet-loop': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petloop.bam',
                 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zstart.bam',
                 'wave': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_wave.bam',
                 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reelneutral.bam',
                 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_poleneutral.bam',
                 'bank': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_jellybeanJar.bam',
                 'scientistGame': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistGame.bam',
                 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-hand.bam',
                 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_lookloop-putt.bam',
                 'victory': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_victory-dance.bam',
                 'lose': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_lose.bam',
                 'cringe': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_cringe.bam',
                 'right': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_right.bam',
                 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_headdown-putt.bam',
                 'conked': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_conked.bam',
                 'jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump.bam',
                 'into-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_into-putt.bam',
                 'fish-end': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishEND.bam',
                 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zend.bam',
                 'shrug': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_shrug.bam',
                 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_sprinkle-dust.bam',
                 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hold-bottle.bam',
                 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_takePhone.bam',
                 'melt': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_melt.bam',
                 'pet-start': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petin.bam',
                 'look-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_look-putt.bam',
                 'loop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_loop-putt.bam',
                 'good-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_good-putt.bam',
                 'juggle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_juggle.bam',
                 'run': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_run.bam',
                 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_press-button.bam',
                 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-back-right.bam',
                 'water': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_water.bam',
                 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-point-start.bam',
                 'bad-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_bad-putt.bam',
                 'struggle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_struggle.bam',
                 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_running-jump.bam',
                 'callPet': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_callPet.bam',
                 'throw': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_pie-throw.bam',
                 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_eat_neutral.bam',
                 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_tug-o-war.bam',
                 'bow': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_bow.bam',
                 'swing': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_swing.bam',
                 'climb': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_climb.bam',
                 'scientistWork': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistWork.bam',
                 'think': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_think.bam',
                 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gameThrow.bam',
                 'walk': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_walk.bam',
                 'down': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_down.bam',
                 'pole': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_pole.bam',
                 'periscope': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_periscope.bam',
                 'duck': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_duck.bam',
                 'curtsy': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_curtsy.bam',
                 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zend.bam',
                 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_loop_dig.bam',
                 'angry': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_angry.bam',
                 'bored': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_bored.bam',
                 'swing-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_swing-putt.bam',
                 'pet-end': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petend.bam',
                 'spit': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_spit.bam',
                 'right-point': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-point.bam',
                 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_into_dig.bam',
                 'castlong': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_castlong.bam',
                 'confused': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_confused.bam',
                 'neutral': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam',
                 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zhang.bam',
                 'reel': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reel.bam',
                 'slip-backward': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_slip-backward.bam',
                 'sound': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_shout.bam',
                 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_sidestep-left.bam',
                 'up': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_up.bam',
                 'fish-again': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishAGAIN.bam',
                 'cast': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_cast.bam',
                 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_phoneBack.bam',
                 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_phoneNeutral.bam',
                 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistJealous.bam',
                 'battlecast': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fish.bam',
                 'sit-start': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_intoSit.bam',
                 'toss': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_toss.bam',
                 'happy-dance': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_happy-dance.bam',
                 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zstart.bam',
                 'teleport': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_teleport.bam',
                 'sit': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sit.bam',
                 'sad-walk': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_losewalk.bam',
                 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_give-props-start.bam',
                 'book': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_book.bam',
                 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zhang.bam',
                 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistEmcee.bam',
                 'leverPull': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverPull.bam',
                 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_tutorial-neutral.bam',
                 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_badloop-putt.bam',
                 'give-props': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_give-props.bam',
                 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hold-magnet.bam',
                 'hypnotize': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hypnotize.bam',
                 'left-point': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_left-point.bam',
                 'leverReach': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverReach.bam',
                 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_feedPet.bam',
                 'reel-H': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reelH.bam',
                 'applause': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_applause.bam',
                 'smooch': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_smooch.bam',
                 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_rotateR-putt.bam',
                 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishneutral.bam',
                 'push': 'phase_9/models/char/tt_a_chr_dgl_shorts_torso_push.bam',
                 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gameneutral.bam',
                 'left': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_left.bam'}

dogHead = loader.loadModel("phase_3/models/char/mouse-heads-500.bam")
dogHead.setX(0)
dogHead.setY(0)
dogHead.setZ(-1)
#dogHead.place()
dogHead.setColor(255, 0, 0)
otherParts = dogHead.findAllMatches('**/*long*')
for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()
ntrlMuzzle = dogHead.find('**/*muzzle*neutral')
otherParts = dogHead.findAllMatches('**/*muzzle*')
for partNum in range(0, otherParts.getNumPaths()):
    part = otherParts.getPath(partNum)
    if part != ntrlMuzzle:
        otherParts.getPath(partNum).removeNode()
dogTorso = loader.loadModel("phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam")
dogLegs = loader.loadModel("phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam")
otherParts = dogLegs.findAllMatches('**/boots*') + dogLegs.findAllMatches('**/shoes')
for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()


#cane2 = loader.loadModel('phase_5\models\props\cane.bam')
#cane2.reparentTo(dogHead.find('**/joint_hips'))
#cane2.setZ(-3)
#cane2.setY(1.30)
#cane2.setX(-1.30)

#hat = loader.loadModel('phase_5/models/props/hat.bam')
#hat.reparentTo(dog.find('**/joint_head'))
#hat.setH(50.19)
#hat.setScale(1.09)
#hat.setX(0.16)
#hat.setY(-0.04)
#hat.setZ(1.64)
#hat.setR(300.96)


dogBody = Actor({'head': dogHead, 'torso': dogTorso, 'legs': dogLegs},
                {'torso': torsoAnimDict, 'legs': legsAnimDict})
dogBody.attach('head', 'torso', 'def_head')
dogBody.attach('torso', 'legs', 'joint_hips')

gloves = dogBody.findAllMatches('**/hands')
ears = dogBody.findAllMatches('**/*ears*')
head = dogBody.findAllMatches('**/head-*')
sleeves = dogBody.findAllMatches('**/sleeves')
shirt = dogBody.findAllMatches('**/torso-top')
shorts = dogBody.findAllMatches('**/torso-bot')
neck = dogBody.findAllMatches('**/neck')
arms = dogBody.findAllMatches('**/arms')
legs = dogBody.findAllMatches('**/legs')
feet = dogBody.findAllMatches('**/feet')

bodyNodes = []
bodyNodes += [gloves]
bodyNodes += [head, ears]
bodyNodes += [sleeves, shirt, shorts]
bodyNodes += [neck, arms, legs, feet]
bodyNodes[0].setColor(255, 255, 255)  # gloves
bodyNodes[1].setColor(128, 255, 0)  # head
bodyNodes[2].setColor(255, 128, 0)  # ears
bodyNodes[3].setColor(0, 255, 0)  # sleves
bodyNodes[4].setColor(0, 255, 0)  # shirt
bodyNodes[5].setColor(0, 0, 255)  # shorts
bodyNodes[6].setColor(255, 128, 0)  # neck
bodyNodes[7].setColor(255, 128, 0)  # arms
bodyNodes[8].setColor(0, 128, 64)  # legs
bodyNodes[9].setColor(0, 128, 64)  # feet

topTex = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirt_sellbotCrusher.jpg')
botTex = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg')
sleeveTex = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotCrusher.jpg')

dogBody.reparentTo(render)
geom = dogBody.getGeomNode()
geom.getChild(0).setSx(0.730000019073)
geom.getChild(0).setSz(0.730000019073)
offset = 3.2375

base.camera.reparentTo(dogBody)
base.camera.setPos(0, -10.0 - offset, offset)
wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()


def getAirborneHeight():
    return offset + 0.025000000000000001


walkControls = GravityWalker(legacyLifter=True)
walkControls.setWallBitMask(wallBitmask)
walkControls.setFloorBitMask(floorBitmask)
walkControls.setWalkSpeed(32.0, 28.0, 16.0, 80.0)
walkControls.initializeCollisions(base.cTrav, dogBody, floorOffset=0.025, reach=4.0)
walkControls.setAirborneHeightFunc(getAirborneHeight)
walkControls.enableAvatarControls()
dogBody.physControls = walkControls


def setWatchKey(key, input, keyMapName):
    def watchKey(active=True):
        if active == True:
            inputState.set(input, True)
            keyMap[keyMapName] = 1
        else:
            inputState.set(input, False)
            keyMap[keyMapName] = 0

    base.accept(key, watchKey, [True])
    base.accept(key + '-up', watchKey, [False])


keyMap = {'left': 0, 'right': 0, 'forward': 0, 'backward': 0, 'control': 0}

setWatchKey('arrow_up', 'forward', 'forward')
setWatchKey('control-arrow_up', 'forward', 'forward')
setWatchKey('alt-arrow_up', 'forward', 'forward')
setWatchKey('shift-arrow_up', 'forward', 'forward')
setWatchKey('arrow_down', 'reverse', 'backward')
setWatchKey('control-arrow_down', 'reverse', 'backward')
setWatchKey('alt-arrow_down', 'reverse', 'backward')
setWatchKey('shift-arrow_down', 'reverse', 'backward')
setWatchKey('arrow_left', 'turnLeft', 'left')
setWatchKey('control-arrow_left', 'turnLeft', 'left')
setWatchKey('alt-arrow_left', 'turnLeft', 'left')
setWatchKey('shift-arrow_left', 'turnLeft', 'left')
setWatchKey('arrow_right', 'turnRight', 'right')
setWatchKey('control-arrow_right', 'turnRight', 'right')
setWatchKey('alt-arrow_right', 'turnRight', 'right')
setWatchKey('shift-arrow_right', 'turnRight', 'right')
setWatchKey('control', 'jump', 'control')

movingNeutral, movingForward = (False, False)
movingRotation, movingBackward = (False, False)
movingJumping = False


def setMovementAnimation(loopName, playRate=1.0):
    global movingNeutral
    global movingForward
    global movingRotation
    global movingBackward
    global movingJumping
    if 'jump' in loopName:
        movingJumping = True
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'run':
        movingJumping = False
        movingForward = True
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'walk':
        movingJumping = False
        movingForward = False
        movingNeutral = False
        if playRate == -1.0:
            movingBackward = True
            movingRotation = False
        else:
            movingBackward = False
            movingRotation = True
    elif loopName == 'neutral':
        movingJumping = False
        movingForward = False
        movingNeutral = True
        movingRotation = False
        movingBackward = False
    else:
        movingJumping = False
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    ActorInterval(dogBody, loopName, playRate=playRate).loop()


def handleMovement(task):
    global movingNeutral, movingForward
    global movingRotation, movingBackward, movingJumping
    if keyMap['control'] == 1:
        if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
            if movingJumping == False:
                if dogBody.physControls.isAirborne:
                    setMovementAnimation('running-jump-idle')
                else:
                    if keyMap['forward']:
                        if movingForward == False:
                            setMovementAnimation('run')
                    elif keyMap['backward']:
                        if movingBackward == False:
                            setMovementAnimation('walk', playRate=-1.0)
                    elif keyMap['left'] or keyMap['right']:
                        if movingRotation == False:
                            setMovementAnimation('walk')
            else:
                if not dogBody.physControls.isAirborne:
                    if keyMap['forward']:
                        if movingForward == False:
                            setMovementAnimation('run')
                    elif keyMap['backward']:
                        if movingBackward == False:
                            setMovementAnimation('walk', playRate=-1.0)
                    elif keyMap['left'] or keyMap['right']:
                        if movingRotation == False:
                            setMovementAnimation('walk')
        else:
            if movingJumping == False:
                if dogBody.physControls.isAirborne:
                    setMovementAnimation('jump-idle')
                else:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
            else:
                if not dogBody.physControls.isAirborne:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
    elif keyMap['forward'] == 1:
        if movingForward == False:
            if not dogBody.physControls.isAirborne:
                setMovementAnimation('run')
    elif keyMap['backward'] == 1:
        if movingBackward == False:
            if not dogBody.physControls.isAirborne:
                setMovementAnimation('walk', playRate=-1.0)
    elif keyMap['left'] or keyMap['right']:
        if movingRotation == False:
            if not dogBody.physControls.isAirborne:
                setMovementAnimation('walk')
    else:
        if not dogBody.physControls.isAirborne:
            if movingNeutral == False:
                setMovementAnimation('neutral')
    return Task.cont


base.taskMgr.add(handleMovement, 'controlManager')

localAvatar = dogBody
base.localAvatar = localAvatar


#Terrain

playgroundarea = loader.loadModel('phase_4/models/neighborhoods/toontown_central.bam')
playgroundarea.reparentTo(render)
playgroundarea.setY(0)
playgroundarea.setX(0)
playgroundarea.setZ(0)

prop1 =loader.loadModel('phase_4/models/modules/gazebo.bam')
prop1.reparentTo(render)
prop1.setX(9.67)
prop1.setY(-60.35)
prop1.setZ(-1.94)
prop1.setH(94.76)

PetShop =loader.loadModel('phase_4/models/modules/PetShopExterior_TT.bam')
PetShop.reparentTo(render)
PetShop.setX(-72.34)
PetShop.setY(-126.02)
PetShop.setZ(0.47)
PetShop.setH(137.73)

Tunnel1 =loader.loadModel('phase_4/models/modules/safe_zone_tunnel_TT.bam')
Tunnel1.reparentTo(render)
Tunnel1.setX(-54.23)
Tunnel1.setY(-242.84)
Tunnel1.setZ(-6.03)
Tunnel1.setH(0)

school =loader.loadModel('phase_4/models/modules/school_house.bam')
school.reparentTo(render)
school.setX(101.42)
school.setY(140.14)
school.setZ(0.00)
school.setH(344.74)

PartyGate =loader.loadModel('phase_4/models/modules/partyGate_TT.bam')
PartyGate.reparentTo(render)
PartyGate.setX(160.99)
PartyGate.setY(90.97)
PartyGate.setZ(2.58)
PartyGate.setH(294.23)

Library =loader.loadModel('phase_4/models/modules/library.bam')
Library.reparentTo(render)
Library.setX(52.11)
Library.setY(89.81)
Library.setZ(3.98)
Library.setH(270.00)

#Cog NPC1
cog1 = Actor("phase_3.5/models/char/suitB-mod.bam", {"smoke":"phase_5/models/char/suitB-magic1.bam", "neutral":"phase_4/models/char/suitB-neutral.bam"})
cog1.reparentTo(render)
cog1.loop('neutral')
cog1.setX(35.42)
cog1.setY(37.38)
cog1.setZ(4.13)
cog1.setH(90.00)
cheese = loader.loadModel("phase_4/models/char/suitB-heads.bam")
jointhd = cog1.find('**/joint_head')
cheese.reparentTo(jointhd)
cog1.find('**/telemarketer').hide()
cog1.find('**/loanshark').hide()
cog1.find('**/beancounter').hide()
cog1.find('**/movershaker').hide()
cog1.find('**/pencilpusher').hide()
texturepls = loader.loadTexture('phase_3.5/maps/l_blazer.jpg')
cog1.findAllMatches('**/torso').setTexture(texturepls, 1)
texturepls2 = loader.loadTexture('phase_3.5/maps/l_leg.jpg')
cog1.findAllMatches('**/legs').setTexture(texturepls2, 1)
texturepls3 = loader.loadTexture('phase_3.5/maps/l_sleeve.jpg')
cog1.findAllMatches('**/arms').setTexture(texturepls3, 1)


#Cog NPC2

cog17 = Actor("phase_3.5/models/char/suitA-mod.bam", {"smoke":"phase_12/models/char/suitA-sit-lose.bam", "neutral":"phase_4/models/char/suitA-neutral.bam"})
cog17.reparentTo(render)
cog17.loop('neutral')
cog17.setX(35.42)
cog17.setY(80.63)
cog17.setZ(4.13)
cog17.setH(90.00)
cheese = loader.loadModel("phase_4/models/char/suitA-heads.bam")
jointhd = cog17.find('**/joint_head')
cheese.reparentTo(jointhd)
cog17.find('**/bigwig').hide()
cog17.find('**/numbercruncher').hide()
cog17.find('**/twoface').hide()
cog17.find('**/backstabber').hide()
cog17.find('**/pennypincher').hide()
cog17.find('**/headhunter').hide()
cog17.find('**/legaleagle').hide()
cog17.find('**/bigcheese').hide()
texturepls = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
cog17.findAllMatches('**/torso').setTexture(texturepls, 1)
texturepls2 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
cog17.findAllMatches('**/legs').setTexture(texturepls2, 1)
texturepls3 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
cog17.findAllMatches('**/arms').setTexture(texturepls3, 1)
cane = loader.loadModel('phase_5\models\props\cane.bam')
cane.reparentTo(cog17.find('**/joint_head'))
cane.setZ(-3)
cane.setY(1.30)
cane.setX(-1.30)
hat = loader.loadModel('phase_5/models/props/hat.bam')
hat.reparentTo(cog17.find('**/joint_head'))
hat.setH(50.19)
hat.setScale(1.09)
hat.setX(0.16)
hat.setY(-0.04)
hat.setZ(1.64)
hat.setR(300.96)


#Objects
can1 = loader.loadModel('phase_12/models/bossbotHQ/canoffood.bam')
can1.reparentTo(render)
can1.find('**/tray').hide()
can1.setX(30.88)
can1.setZ(4.22)
can1.setY(35.46)
can1.setH(272.73)
can1.setScale(0.53)

can2 = loader.loadModel('phase_12/models/bossbotHQ/canoffood.bam')
can2.reparentTo(render)
can2.find('**/tray').hide()
can2.setX(30.88)
can2.setZ(4.22)
can2.setY(37.19)
can2.setH(272.73)
can2.setScale(0.53)

can3 = loader.loadModel('phase_12/models/bossbotHQ/canoffood.bam')
can3.reparentTo(render)
can3.find('**/tray').hide()
can3.setX(30.88)
can3.setZ(4.22)
can3.setY(38.91)
can3.setH(272.73)
can3.setScale(0.53)

sandwitch = loader.loadModel('phase_6/models/golf/picnic_sandwich.bam')
sandwitch.reparentTo(render)
sandwitch.setX(35.50)
sandwitch.setY(36.45)
sandwitch.setZ(6.23)
sandwitch.setScale(1.86)
sandwitch.setP(75.96)

Skybox = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
Skybox.reparentTo(render)
Skybox.setY(0)
Skybox.setX(0)
Skybox.setZ(-165.02)

Music = base.loader.loadSfx("Custom Things/FF_safezone.ogg")
Music.setLoop(True)
Music.play()

#ToonNPC1
Whiskers = Actor({'Torso':'phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam', \
             'Legs':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam'}, \
             {'Torso':{'Idle': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam', \
             'TorsoAnim':'phase_3/models/char/tt_a_chr_dgm_shorts_torso_neutral.bam'}, \
             'Legs':{'Idle':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam',
             'LegsAnim':'phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral.bam'}})

Whiskers.attach('Torso', 'Legs', 'joint_hips')

#Animations
Whiskers.loop('TorsoAnim')
Whiskers.loop('LegsAnim')

#Pos, Hpr, Scale, ReparentTo
Whiskers.setPos(28.18, 37.53, 4.04)
Whiskers.setHpr(0, 0, 0)
Whiskers.setScale(0.90)
Whiskers.reparentTo(render)

#Head
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

#******************************Clothes******************************


#Gloves
Gloves = Whiskers.find('**/hands')
Gloves.setColor(0.99, 0.99, 0.99)

#Sleeves
Sleeves = loader.loadTexture('phase_4/maps/shirt_Sleeve_ghost.jpg')
Whiskers.find('**/sleeves').setTexture(Sleeves, 1)

#Shirts
Shirt = loader.loadTexture('phase_4/maps/shirt_ghost.jpg')
Whiskers.find('**/torso-top').setTexture(Shirt, 1)

#Shorts
Shorts = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shorts_bee.jpg')
Whiskers.find('**/torso-bot').setTexture(Shorts, 1)

#Shoes/Boots
Shoes = loader.loadTexture('phase_4/maps/tt_t_chr_avt_acc_sho_athleticBlack.jpg')
Whiskers.find('**/shoes').setTexture(Shoes, 1)
Whiskers.find('**/shoes').setScale(1.1)
Whiskers.find('**/boots_long').hide()
Whiskers.find('**/boots_short').hide()
Whiskers.find('**/feet').hide()

#Hats
#Hat = loader.loadModel('phase_4/models/accessories/tt_m_chr_avt_acc_hat_topHat.bam')
#Hat.reparentTo(Head.find('**/head-short'))
#Hat.setPos(0, -0.10, 0.75)
#Hat.setHpr(180.00, 350.00, 0)
#Hat.setScale(0.45)

#Glasses
#Glasses = loader.loadModel('phase_4/models/accessories/tt_m_chr_avt_acc_msk_squareRims.bam')
#Glasses.reparentTo(Head.find('**/head-front-short'))
#Glasses.setZ(0.30)
#Glasses.setHpr(180, 350.00, 0)
#Glasses.setScale(0.40)

#Colors
Head.find('**/head-short').setColor(0.23, 0.68, 0.48, 1.0)
Head.find('**/head-front-short').setColor(0.23, 0.68, 0.48, 1.0)
Head.find('**/ears-short').setColor(0.23, 0.68, 0.48, 1.0)
Whiskers.find('**/neck').setColor(0.23, 0.68, 0.48, 1.0)
Whiskers.find('**/arms').setColor(0.23, 0.68, 0.48, 1.0)
Whiskers.find('**/legs').setColor(0.23, 0.68, 0.48, 1.0)
Whiskers.find('**/feet').setColor(0.23, 0.68, 0.48, 1.0)
#Hat.setColor(0.99, 0.99, 0.99)
#Glasses.setColor(0.99, 0.99, 0.99)
Whiskers.setH(270.00)

print 'Welcome To Toontown Central!'
print 'The Happiest Place In The Town'
print 'Mr Hollywood: Do NOT underestimate the power of the Bamboo Cane'

base.run()
