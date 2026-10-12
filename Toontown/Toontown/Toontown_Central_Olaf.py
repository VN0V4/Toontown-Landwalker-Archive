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
from direct.showbase import DirectObject
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker

from panda3d.core import *

base.disableMouse()

legsAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_legs_right-hand-start.bam',
                'firehose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_firehose.bam',
                'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateL-putt.bam',
                'slip-forward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-forward.bam',
                'Catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eatnrun.bam',
                'tickle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_tickle.bam',
                'water-gun': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_water-gun.bam',
                'leverNeutral': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverNeutral.bam',
                'swim': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swim.bam',
                'Catch-run': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gamerun.bam',
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
                'Catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eat_neutral.bam',
                'tug-o-war': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_tug-o-war.bam',
                'bow': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bow.bam',
                'swing': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swing.bam',
                'climb': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_climb.bam',
                'scientistWork': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistWork.bam',
                'think': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_think.bam',
                'Catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameThrow.bam',
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
                'Catch-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameneutral.bam',
                'left': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_left.bam'}

torsoAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_right-hand-start.bam',
                 'firehose': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_firehose.bam',
                 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_rotateL-putt.bam',
                 'slip-forward': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_slip-forward.bam',
                 'Catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_eatnrun.bam',
                 'tickle': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_tickle.bam',
                 'water-gun': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_water-gun.bam',
                 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgm_shorts_torso_leverNeutral.bam',
                 'swim': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_swim.bam',
                 'Catch-run': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_gamerun.bam',
                 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_sad-neutral.bam',
                 'pet-loop': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_petloop.bam',
                 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_jump-zstart.bam',
                 'wave': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_wave.bam',
                 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_reelneutral.bam',
                 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_poleneutral.bam',
                 'bank': 'phase_5.5/models/char/tt_a_chr_dgm_shorts_torso_jellybeanJar.bam',
                 'scientistGame': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_scientistGame.bam',
                 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_right-hand.bam',
                 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_lookloop-putt.bam',
                 'victory': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_victory-dance.bam',
                 'lose': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_lose.bam',
                 'cringe': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_cringe.bam',
                 'right': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_right.bam',
                 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_headdown-putt.bam',
                 'conked': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_conked.bam',
                 'jump': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_jump.bam',
                 'into-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_into-putt.bam',
                 'fish-end': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_fishEND.bam',
                 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_leap_zend.bam',
                 'shrug': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_shrug.bam',
                 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_sprinkle-dust.bam',
                 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_hold-bottle.bam',
                 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgm_shorts_torso_takePhone.bam',
                 'melt': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_melt.bam',
                 'pet-start': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_petin.bam',
                 'look-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_look-putt.bam',
                 'loop-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_loop-putt.bam',
                 'good-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_good-putt.bam',
                 'juggle': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_juggle.bam',
                 'run': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_run.bam',
                 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_press-button.bam',
                 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_jump-back-right.bam',
                 'water': 'phase_5.5/models/char/tt_a_chr_dgm_shorts_torso_water.bam',
                 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_right-point-start.bam',
                 'bad-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_bad-putt.bam',
                 'struggle': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_struggle.bam',
                 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_running-jump.bam',
                 'callPet': 'phase_5.5/models/char/tt_a_chr_dgm_shorts_torso_callPet.bam',
                 'throw': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_pie-throw.bam',
                 'Catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_eat_neutral.bam',
                 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_tug-o-war.bam',
                 'bow': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_bow.bam',
                 'swing': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_swing.bam',
                 'climb': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_climb.bam',
                 'scientistWork': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_scientistWork.bam',
                 'think': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_think.bam',
                 'Catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_gameThrow.bam',
                 'walk': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_walk.bam',
                 'down': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_down.bam',
                 'pole': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_pole.bam',
                 'periscope': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_periscope.bam',
                 'duck': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_duck.bam',
                 'curtsy': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_curtsy.bam',
                 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_jump-zend.bam',
                 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgm_shorts_torso_loop_dig.bam',
                 'angry': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_angry.bam',
                 'bored': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_bored.bam',
                 'swing-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_swing-putt.bam',
                 'pet-end': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_petend.bam',
                 'spit': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_spit.bam',
                 'right-point': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_right-point.bam',
                 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgm_shorts_torso_into_dig.bam',
                 'castlong': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_castlong.bam',
                 'confused': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_confused.bam',
                 'neutral': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_neutral.bam',
                 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_jump-zhang.bam',
                 'reel': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_reel.bam',
                 'slip-backward': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_slip-backward.bam',
                 'sound': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_shout.bam',
                 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_sidestep-left.bam',
                 'up': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_up.bam',
                 'fish-again': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_fishAGAIN.bam',
                 'cast': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_cast.bam',
                 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgm_shorts_torso_phoneBack.bam',
                 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgm_shorts_torso_phoneNeutral.bam',
                 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_scientistJealous.bam',
                 'battlecast': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_fish.bam',
                 'sit-start': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_intoSit.bam',
                 'toss': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_toss.bam',
                 'happy-dance': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_happy-dance.bam',
                 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_leap_zstart.bam',
                 'teleport': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_teleport.bam',
                 'sit': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_sit.bam',
                 'sad-walk': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_losewalk.bam',
                 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_give-props-start.bam',
                 'book': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_book.bam',
                 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_leap_zhang.bam',
                 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_scientistEmcee.bam',
                 'leverPull': 'phase_10/models/char/tt_a_chr_dgm_shorts_torso_leverPull.bam',
                 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_tutorial-neutral.bam',
                 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_badloop-putt.bam',
                 'give-props': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_give-props.bam',
                 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_hold-magnet.bam',
                 'hypnotize': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_hypnotize.bam',
                 'left-point': 'phase_3.5/models/char/tt_a_chr_dgm_shorts_torso_left-point.bam',
                 'leverReach': 'phase_10/models/char/tt_a_chr_dgm_shorts_torso_leverReach.bam',
                 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgm_shorts_torso_feedPet.bam',
                 'reel-H': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_reelH.bam',
                 'applause': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_applause.bam',
                 'smooch': 'phase_5/models/char/tt_a_chr_dgm_shorts_torso_smooch.bam',
                 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgm_shorts_torso_rotateR-putt.bam',
                 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_fishneutral.bam',
                 'push': 'phase_9/models/char/tt_a_chr_dgm_shorts_torso_push.bam',
                 'Catch-neutral': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_gameneutral.bam',
                 'left': 'phase_4/models/char/tt_a_chr_dgm_shorts_torso_left.bam'}

DuckHead = loader.loadModel('Custom Things/OlafHead9_temp.bam')
otherParts = DuckHead.findAllMatches('**/*long*')

for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()
ntrlMuzzle = DuckHead.find('**/*muzzle*neutral')
otherParts = DuckHead.findAllMatches('**/*muzzle*')

for partNum in range(0, otherParts.getNumPaths()):
    part = otherParts.getPath(partNum)
    if part != ntrlMuzzle:
        otherParts.getPath(partNum).removeNode()
DuckTorso = loader.loadModel('phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam')
DuckLegs = loader.loadModel('phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam')
otherParts = DuckLegs.findAllMatches('**/boots*') + DuckLegs.findAllMatches('**/shoes')

for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()

DuckBody = Actor({'head': DuckHead, 'torso': DuckTorso, 'legs': DuckLegs},
                 {'torso': torsoAnimDict, 'legs': legsAnimDict})
DuckBody.attach('head', 'torso', 'def_head')
DuckBody.attach('torso', 'legs', 'joint_hips')

gloves = DuckBody.findAllMatches('**/hands')
ears = DuckBody.findAllMatches('**/*ears*')
head = DuckBody.findAllMatches('**/head-*')
sleeves = DuckBody.findAllMatches('**/sleeves')
shirt = DuckBody.findAllMatches('**/torso-top')
shorts = DuckBody.findAllMatches('**/torso-bot')
neck = DuckBody.findAllMatches('**/neck')
arms = DuckBody.findAllMatches('**/arms')
legs = DuckBody.findAllMatches('**/legs')
feet = DuckBody.findAllMatches('**/feet')

bodyNodes = []
bodyNodes += [gloves]
bodyNodes += [head, ears]
bodyNodes += [sleeves, shirt, shorts]
bodyNodes += [neck, arms, legs, feet]
bodyNodes[0].setColor(1, 1, 1, 1)
bodyNodes[1].setColor(0.30, 0.84, 0.94, 1)
bodyNodes[2].setColor(0.30, 0.84, 0.94, 1)
bodyNodes[3].setColor(0.10, 0.34, 0.29, 1)
bodyNodes[4].setColor(0.56, 0.84, 0.33, 1)
bodyNodes[5].setColor(0.56, 0.84, 0.33, 1)
bodyNodes[6].setColor(0.40, 0.84, 0.76, 1)
bodyNodes[7].setColor(0.40, 0.84, 0.76, 1)
bodyNodes[8].setColor(0.18, 0.54, 0.73, 1)
bodyNodes[9].setColor(0.18, 0.54, 0.73, 1)

topTex = loader.loadTexture('phase_3/maps/desat_shirt_19.jpg')
botTex = loader.loadTexture('phase_3/maps/desat_shorts_6.jpg')
sleeveTex = loader.loadTexture('phase_3/maps/desat_sleeve_1.jpg')

bodyNodes[3].setTexture(sleeveTex, 1)
bodyNodes[4].setTexture(topTex, 1)
bodyNodes[5].setTexture(botTex, 1)

DuckBody.reparentTo(render)

geom = DuckBody.getGeomNode()
geom.getChild(0).setSx(0.730000019073)
geom.getChild(0).setSz(0.730000019073)

offset = 3.2375

base.camera.reparentTo(DuckBody)
base.camera.setPos(0, -20.0 - offset, offset)
wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()
base.camera.hide()


def getAirborneHeight():
    return offset + 0.025000000000000001


walkControls = GravityWalker(legacyLifter=True)
walkControls.setWallBitMask(wallBitmask)
walkControls.setFloorBitMask(floorBitmask)
walkControls.setWalkSpeed(50.0, 50.0, 50.0, 50.0)
walkControls.initializeCollisions(base.cTrav, DuckBody, floorOffset=0.025, reach=4.0)
walkControls.setAirborneHeightFunc(getAirborneHeight)
walkControls.enableAvatarControls()
DuckBody.physControls = walkControls


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
    ActorInterval(DuckBody, loopName, playRate=playRate).loop()


def handleMovement(task):
    global movingNeutral, movingForward
    global movingRotation, movingBackward, movingJumping
    if keyMap['control'] == 1:
        if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
            if movingJumping == False:
                if DuckBody.physControls.isAirborne:
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
                if not DuckBody.physControls.isAirborne:
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
                if DuckBody.physControls.isAirborne:
                    setMovementAnimation('jump-idle')
                else:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
            else:
                if not DuckBody.physControls.isAirborne:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
                        fsrun.stop()
    elif keyMap['forward'] == 1:
        if movingForward == False:
            if not DuckBody.physControls.isAirborne:
                setMovementAnimation('run')
    elif keyMap['backward'] == 1:
        if movingBackward == False:
            if not DuckBody.physControls.isAirborne:
                setMovementAnimation('walk', playRate=-1.0)
    elif keyMap['left'] or keyMap['right']:
        if movingRotation == False:
            if not DuckBody.physControls.isAirborne:
                setMovementAnimation('walk')
                fswalk = loader.loadSfx('phase_3.5/audio/sfx/AV_footstep_walkloop.wav')
    else:
        if not DuckBody.physControls.isAirborne:
            if movingNeutral == False:
                setMovementAnimation('neutral')
    return Task.cont


base.taskMgr.add(handleMovement, 'controlManager')


def collisionsOn():
    DuckBody.physControls.setCollisionsActive(True)
    DuckBody.physControls.isAirborne = True


def collisionsOff():
    DuckBody.physControls.setCollisionsActive(False)
    DuckBody.physControls.isAirborne = True


def toggleCollisions():
    if DuckBody.physControls.getCollisionsActive():
        DuckBody.physControls.setCollisionsActive(False)
        DuckBody.physControls.isAirborne = True
    else:
        DuckBody.physControls.setCollisionsActive(True)
        DuckBody.physControls.isAirborne = True


base.accept('f1', toggleCollisions)
DuckBody.collisionsOn = collisionsOn
DuckBody.collisionsOff = collisionsOff
DuckBody.toggleCollisions = toggleCollisions

fsrun = loader.loadSfx('phase_4/audio/bgm/new_years_firework_music.MID')
fsrun.setLoop(True)
fsrun.play()

localAvatar = DuckBody
base.localAvatar = localAvatar
localAvatar.physControls.placeOnFloor()

onScreenDebug.enabled = False


def updateOnScreenDebug(task):
    onScreenDebug.add('Avatar Position', localAvatar.getPos())
    onScreenDebug.add('Avatar Angle', localAvatar.getHpr())

    return Task.cont


# Font
MickeyFont = loader.loadFont("phase_3/models/fonts/MickeyFont.bam")


class EnvironmentTTC():

    def __init__(self):
        # Create the dictionary for all the models
        self.modeldict = {}
        self.LoadTTC()

    def LoadTTC(self):
        # Sky
        self.modelloader("Sky", "phase_3.5/models/props/TT_sky.bam", render, 0, 0, 0, 0, 0, 0, 5, 5, 5)
        Clouds1 = self.modeldict["Sky"].find("**/cloud1")
        Clouds2 = self.modeldict["Sky"].find("**/cloud2")
        Clouds1.setScale(0.6, 0.6, 0.6)
        Clouds2.setScale(0.9, 0.9, 0.9)
        Clouds1Spin = Clouds1.hprInterval(360, Vec3(60, 0, 0))
        Clouds1Spin.loop()
        Clouds2Spin = Clouds2.hprInterval(360, Vec3(-60, 0, 0))
        Clouds2Spin.loop()

        # The order for using modelloader is as follows ( nodename, filepath, parent, x, y, z, h, p, r, scale1, scale2, scale3 )

        # Load the TTC model
        self.modelloader("TTC", "phase_4/models/neighborhoods/toontown_central.bam", render, 0, 0, 0, -90, 0, 0, 1, 1,
                         1)
        self.modeldict["TTC"].setTransparency(TransparencyAttrib.MBinary, 1)

        # Buildings
        self.modelloader("ToonHQ", "phase_3.5/models/modules/hqTT.bam", render, 24.6425, 24.8587, 4.00001, 135, 0, 0, 1,
                         1, 1)
        self.modeldict["ToonHQ"].find("**/doorFrameHoleRight_0").hide()
        self.modeldict["ToonHQ"].find("**/doorFrameHoleLeft_0").hide()
        self.modeldict["ToonHQ"].find("**/doorFrameHoleRight_1").hide()
        self.modeldict["ToonHQ"].find("**/doorFrameHoleLeft_1").hide()

        self.modelloader("Cogbuilding", "phase_4/models/modules/suit_landmark_legal.bam", render, -123, -83, 0.5, 128,
                         0, 0, 1, 1, 1)

        self.modelloader("Partygate", "phase_4/models/modules/partyGate_TT.bam", render, 77.935, -159.939, 2.70141, 195,
                         0, 0, 1, 1, 1)

        self.modelloader("Petshop", "phase_4/models/modules/PetShopExterior_TT.bam", render, -124.375, 74.3749, 0.5, 49,
                         0, 0, 1, 1, 1)
        self.modelloaderanimate("PetshopFish", "phase_4/models/props/exteriorfish-zero.bam",
                                "phase_4/models/props/exteriorfish-swim.bam", self.modeldict["Petshop"], 0, 0, 0, 0, 0,
                                0, 1, 1, 1, "swim")
        Petsign1 = self.modeldict["Petshop"].find("**/sign_origin")
        self.textloader("Pettext2", "Pettextnode2", "Pettextname2", "Pet Shop", MickeyFont, Petsign1, -5, -0.2, 0.2, 0,
                        0, 0, 2, 2, 2, 0.9, 0.88, 0.1)
        Petdoor = self.modeldict["Petshop"].find("**/door_origin")
        self.modelloadercopyto("Door1", "phase_3.5/models/modules/doors_practical.bam", "door_double_round_ur", Petdoor,
                               0, -0.1, 0, 0, 0, 0, 1, 1, 1);
        self.modeldict["Door1"].setColor(1, 0.87, 0.38)

        self.modelloader("Clothingshop", "phase_4/models/modules/clothshopTT.bam", render, 106.265, 160.831, 3, -30, 0,
                         0, 1, 1, 1)
        Clothingsign1 = self.modeldict["Clothingshop"].find("**/sign_origin")
        self.textloader("Clothingtext2", "Clothingtextnode2", "Clothingtextname2", "Clothing Shop", MickeyFont,
                        Clothingsign1, -6.7, -0.2, 0.1, 0, 0, 0, 1.5, 1.5, 1.5, 0.88, 0.45, 0.38)
        Clothingdoor = self.modeldict["Clothingshop"].find("**/door_origin")
        self.modelloadercopyto("Door2", "phase_3.5/models/modules/doors_practical.bam", "door_double_clothshop",
                               Clothingdoor, 0, -0.1, 0, 0, 0, 0, 1, 1, 1);
        self.modeldict["Door2"].setColor(0.88, 0.45, 0.38)

        self.modelloader("Toonhall", "phase_4/models/modules/toonhall.bam", render, 116.66, 24.29, 4, -90, 0, 0, 1, 1,
                         1)
        Hallsign = self.modeldict["Toonhall"].find("**/sign_origin")
        self.textloader("Halltext1", "Halltextnode1", "Halltextname1", "Mickey", MickeyFont, Hallsign, -5, -0.2, -0.5,
                        0, 0, 0, 2.5, 2.5, 2.5, 0.9, 0.88, 0.1)
        self.textloader("Halltext2", "Halltextnode2", "Halltextname2", "Toon Hall", MickeyFont, Hallsign, -7, -0.2, -3,
                        0, 0, 0, 2.5, 2.5, 2.5, 0.9, 0.88, 0.1)
        Halldoor = self.modeldict["Toonhall"].find("**/toonhall_door_origin")
        self.modelloadercopyto("Door3", "phase_3.5/models/modules/doors_practical.bam", "door_double_round_ur",
                               Halldoor, 0, -0.1, 0, 0, 0, 0, 1, 1, 1);
        self.modeldict["Door3"].setColor(0.88, 0.45, 0.38)

        self.modelloader("Schoolhouse", "phase_4/models/modules/school_house.bam", render, 129.919, -138.445, 2.4997,
                         -140, 0, 0, 1, 1, 1)
        Schoolsign = self.modeldict["Schoolhouse"].find("**/sign_origin")
        self.modelloadercopyto("Schoolsign", "phase_4/models/props/signs_TTC.bam", "TTC_sign3", Schoolsign, 1, -0.05,
                               3.7, 0, 0, 0, 1, 1, 1)
        self.textloader("Schooltext1", "Schooltextnode1", "Schooltextname1", "Toontown", MickeyFont, Schoolsign, -2.5,
                        -0.07, 4.8, 0, 0, 0, 1, 1, 1, 0.9, 0.88, 0.4)
        self.textloader("Schooltext2", "Schooltextnode2", "Schooltextname2", "School House", MickeyFont, Schoolsign,
                        -4.8, -0.07, 3, 0, 0, 0, 1.4, 1.4, 1.4, 0.9, 0.5, 0.1)
        Schooldoor = self.modeldict["Schoolhouse"].find("**/school_door_origin")
        self.modelloadercopyto("Door4", "phase_3.5/models/modules/doors_practical.bam", "door_double_square_ul",
                               Schooldoor, 0, -0.1, 0, 0, 0, 0, 1, 1, 1);
        self.modeldict["Door4"].setColor(1, 0.63, 0.38)

        self.modelloader("Bank", "phase_4/models/modules/bank.bam", render, 57.1796, 38.6656, 4, 0, 0, 0, 1, 1, 1)
        Banksign = self.modeldict["Bank"].find("**/sign_origin")
        self.textloader("Banktext1", "Banktextnode1", "Banktextname1", "Bank", MickeyFont, Banksign, -3.1, -0.2, -1, 0,
                        0, 0, 2.5, 2.5, 2.5, 0.9, 0.6, 0.1)
        Bankdoor = self.modeldict["Bank"].find("**/bank_door_origin")
        self.modelloadercopyto("Door5", "phase_3.5/models/modules/doors_practical.bam", "door_double_round_ur",
                               Bankdoor, 0, -0.1, 0, 0, 0, 0, 1, 1, 1);
        self.modeldict["Door5"].setColor(0.88, 0.45, 0.38)

        self.modelloader("Library", "phase_4/models/modules/library.bam", render, 91.4475, -44.9255, 4, 180, 0, 0, 1, 1,
                         1)
        Librarysign = self.modeldict["Library"].find("**/sign_origin")
        self.modelloadercopyto("Librarysign", "phase_4/models/props/signs_TTC.bam", "TTC_sign3", Librarysign, 1.7,
                               -0.05, 3.7, 0, 0, 0, 1, 1, 1)
        self.textloader("Librarytext1", "Librarytextnode1", "Librarytextname1", "Toontown", MickeyFont, Librarysign,
                        -1.5, -0.07, 4.8, 0, 0, 0, 1, 1, 1, 0.9, 0.88, 0.4)
        self.textloader("Librarytext2", "Librarytextnode2", "Librarytextname2", "Library", MickeyFont, Librarysign,
                        -2.8, -0.07, 3, 0, 0, 0, 1.9, 1.9, 1.9, 0.9, 0.5, 0.1)
        Librarydoor = self.modeldict["Library"].find("**/library_door_origin")
        self.modelloadercopyto("Door6", "phase_3.5/models/modules/doors_practical.bam", "door_double_round_ur",
                               Librarydoor, 0, 0, 0, 0, 0, 0, 1, 1, 1);
        self.modeldict["Door6"].setColor(0.88, 0.45, 0.38)

        self.modelloader("Gagshop", "phase_4/models/modules/gagShop_TT.bam", render, -86.6848, -90.5693, 0.500015, 0, 0,
                         0, 1, 1, 1)
        Gagdoor = self.modeldict["Gagshop"].find("**/building_front")
        self.modelloadercopyto("Door7", "phase_3.5/models/modules/doors_practical.bam", "door_double_square_ur",
                               Gagdoor, 3, 0.1, 0, 180, 0, 0, 1, 1, 1);
        self.modeldict["Door7"].setColor(1, 0.63, 0.38)

        # Tunnels
        self.modelloader("GoofyTunnel", "phase_4/models/modules/Speedway_Tunnel.bam", render, 20.9205, 172.683, 3.24925,
                         -150, -0.083787, 0.0101321, 1, 1, 1)
        Goofysign = self.modeldict["GoofyTunnel"].find("**/sign_origin")
        self.textloader("Goofytext1", "Goofytextnode1", "Goofytextname1", "Goofy", MickeyFont, Goofysign, -2, -0.07,
                        0.7, 0, 0, 0, 2.2, 2.2, 2.2, 0.1, 0.1, 0.7)
        self.textloader("Goofytext2", "Goofytextnode2", "Goofytextname2", "Speed Way", MickeyFont, Goofysign, -6.1,
                        -0.07, -2.8, 0, 0, 0, 2.6, 2.6, 2.6, 0.9, 0.5, 0.1)

        self.modelloader("FirstTunnel", "phase_4/models/modules/safe_zone_tunnel_TT.bam", render, -239.67, 64.08, -6.18,
                         -90, 0, 0, 1, 1, 1)
        SignOrigin1 = self.modeldict["FirstTunnel"].find("**/sign_origin")
        self.modelloader("Orangesign1", "phase_3.5/models/props/tunnel_sign_orange.bam", SignOrigin1, 0, -0.05, 0, 0, 0,
                         0, 1.5, 1.5, 1.5)
        self.textloader("Tunnel1text1", "Tunnel1textnode1", "Tunnel1textname1", "Loopy Lane", MickeyFont, SignOrigin1,
                        -5.5, -0.07, -1.8, 0, 0, 0, 1.6, 1.6, 1.6, 0.0, 0.6, 0.1)
        self.textloader("Tunnel1text2", "Tunnel1textnode2", "Tunnel1textname2", "Toontown Central", MickeyFont,
                        SignOrigin1, -5.7, -0.7, -2.9, 0, 0, 0, 1, 1, 1, 0.0, 0.6, 0.0)
        self.modelloader("MickeyLogo1", "phase_3.5/models/props/mickeySZ.bam", SignOrigin1, 0, -0.07, 2, 0, 0, 0, 4.5,
                         4.5, 4.5)

        self.modelloader("SecondTunnel", "phase_4/models/modules/safe_zone_tunnel_TT.bam", render, -68.38, -202.64,
                         -3.58, -31, 0, 0, 1, 1, 1)
        SignOrigin2 = self.modeldict["SecondTunnel"].find("**/sign_origin")
        self.textloader("Tunnel2text1", "Tunnel2textnode1", "Tunnel2textname1", "Silly Street", MickeyFont, SignOrigin2,
                        -5.9, -0.07, -1.8, 0, 0, 0, 1.6, 1.6, 1.6, 0.0, 0.6, 0.1)
        self.textloader("Tunnel2text2", "Tunnel2textnode2", "Tunnel2textname2", "Toontown Central", MickeyFont,
                        SignOrigin2, -5.7, -0.7, -2.9, 0, 0, 0, 1, 1, 1, 0.0, 0.6, 0.0)
        self.modelloader("Orangesign2", "phase_3.5/models/props/tunnel_sign_orange.bam", SignOrigin2, 0, -0.05, 0, 0, 0,
                         0, 1.5, 1.5, 1.5)
        self.modelloader("MickeyLogo2", "phase_3.5/models/props/mickeySZ.bam", SignOrigin2, 0, -0.07, 2, 0, 0, 0, 4.5,
                         4.5, 4.5)

        self.modelloader("ThirdTunnel", "phase_4/models/modules/safe_zone_tunnel_TT.bam", render, 27.6402, 176.475,
                         -6.18, 171, 0, 0, 1, 1, 1)
        SignOrigin3 = self.modeldict["ThirdTunnel"].find("**/sign_origin")
        self.textloader("Tunnel3text1", "Tunnel3textnode1", "Tunnel3textname1", "Punchline Place", MickeyFont,
                        SignOrigin3, -7.7, -0.07, -1.8, 0, 0, 0, 1.6, 1.6, 1.6, 0.0, 0.6, 0.1)
        self.textloader("Tunnel3text2", "Tunnel3textnode2", "Tunnel3textname2", "Toontown Central", MickeyFont,
                        SignOrigin3, -5.7, -0.7, -2.9, 0, 0, 0, 1, 1, 1, 0.0, 0.6, 0.0)
        self.modelloader("Orangesign3", "phase_3.5/models/props/tunnel_sign_orange.bam", SignOrigin3, 0, -0.05, 0, 0, 0,
                         0, 1.5, 1.5, 1.5)
        self.modelloader("MickeyLogo3", "phase_3.5/models/props/mickeySZ.bam", SignOrigin3, 0, -0.07, 2, 0, 0, 0, 4.5,
                         4.5, 4.5)

        # Props
        self.modelloader("Fishingdock1", "phase_4/models/props/piers_tt.bam", render, -63.5335, 41.648, -3.36708, 120,
                         0, 0, 1, 1, 1)
        self.modelloader("Fishingdock2", "phase_4/models/props/piers_tt.bam", render, -90.2253, 42.5202, -3.3105, -135,
                         0, 0, 1, 1, 1)
        self.modelloader("Fishingdock3", "phase_4/models/props/piers_tt.bam", render, -94.9218, 31.4153, -3.20083, -105,
                         0, 0, 1, 1, 1)
        self.modelloader("Fishingdock4", "phase_4/models/props/piers_tt.bam", render, -77.5199, 46.9817, -3.28456, -180,
                         0, 0, 1, 1, 1)

        self.modelloader("DDSign1", "phase_4/models/props/neighborhood_sign_DD.bam", render, -59.1768, 92.9836,
                         0.499824, -9, 0, 0, 1, 1, 1)
        self.modelloader("DDSign2", "phase_4/models/props/neighborhood_sign_DD.bam", render, -33.749, 88.9499, 0.499825,
                         170, 0, 0, 1, 1, 1)
        self.modelloader("MMSign1", "phase_4/models/props/neighborhood_sign_MM.bam", render, -143.503, -8.9528,
                         0.499987, 90, 0, 0, 1, 1, 1)
        self.modelloader("MMSign2", "phase_4/models/props/neighborhood_sign_MM.bam", render, -143.242, 16.9541,
                         0.499977, -90, 0, 0, 1, 1, 1)
        self.modelloader("DGSign1", "phase_4/models/props/neighborhood_sign_DG.bam", render, 21.3941, -144.665, 2.99998,
                         -30, 0, 0, 1, 1, 1)
        self.modelloader("DGSign2", "phase_4/models/props/neighborhood_sign_DG.bam", render, 44.1038, -157.906, 2.99998,
                         148, 0, 0, 1, 1, 1)

        self.modelloader("Gazebo", "phase_4/models/modules/gazebo.bam", render, -60.44, -11.4, -2, -178, 0, 0, 1, 1, 1)
        self.modelloader("Fountain", "phase_4/models/props/toontown_central_fountain.bam", render, 93.2057, -106.482,
                         2.50002, 0, 0, 0, 1, 1, 1)
        self.modelloader("Mickeyhorse", "phase_4/models/props/mickey_on_horse.bam", render, 73.6829, 121.026, 2.49996,
                         0, 0, 0, 1, 1, 1)
        self.modelloader("Cogdoor", "phase_4/models/modules/elevator.bam", render, -128, -67.99, 0.5, 128, 0, 0, 1, 1,
                         1)
        self.modelloader("FlowerPlant1", "phase_3.5/models/props/big_planter.bam", render, 18.9496, -48.977, 4.95856,
                         135, 0, 0, 1, 1, 1)
        self.modelloader("FlowerPlant2", "phase_3.5/models/props/big_planter.bam", render, 19.2327, 52.5553, 4.95837,
                         -135, 0, 0, 1, 1, 1)

        # Walls
        self.modelloadercopyto("Wall1", "phase_5/models/modules/suit_walls.bam", "wall_suit_build1_ur", render, -150,
                               -35, 0, 90, 0, 0, 22, 22, 22)
        self.modelloadercopyto("Wall2", "phase_5/models/modules/suit_walls.bam", "wall_suit_build1_ur", render, -141,
                               -58, 0, 111, 0, 0, 27, 27, 22)
        self.modelloadercopyto("Wall3", "phase_5/models/modules/suit_walls.bam", "wall_suit_build1_ur", render, -103,
                               -94, 0, 150, 0, 0, 22, 22, 22)
        self.modelloadercopyto("Wall4", "phase_5/models/modules/suit_walls.bam", "wall_suit_build1_ur", render, -95,
                               -95, 0, 180, 0, 0, 22, 22, 22)

        # Fencing
        self.modelloader("Fence1", "phase_3.5/models/modules/wood_fence.bam", render, -148, -23, 0.5, 90, 0, 0, 1, 1, 1)
        self.modelloader("Fence2", "phase_3.5/models/modules/wood_fence.bam", render, -147, -32.8, 0.5, 96, 0, 0, 1, 1,
                         1)
        self.modelloader("Fence3", "phase_3.5/models/modules/wood_fence.bam", render, -144.1, -41.9, 0.5, 107, 0, 0, 1,
                         1, 1)
        self.modelloader("Fence4", "phase_3.5/models/modules/wood_fence.bam", render, -95, -95.5, 0.5, 160, 0, 0, 1, 1,
                         1)
        self.modelloader("Fence5", "phase_3.5/models/modules/wood_fence.bam", render, -104, -92.2, 0.5, 150, 0, 0, 1, 1,
                         1)
        self.modelloader("Fence6", "phase_3.5/models/modules/wood_fence.bam", render, -112.5, -87.3, 0.5, 148, 0, -0, 1,
                         1, 1)
        self.modelloader("Fence7", "phase_3.5/models/modules/wood_fence.bam", render, -140.73, -53, 0.5, 107, 0, 0,
                         1.16, 1, 1.0)

        # Streetlights
        self.modelloaderstreetlight("Streetlight1", "phase_3.5/models/props/streetlight_TT.bam", render, -125, 60, 0.5,
                                    1500, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight2", "phase_3.5/models/props/streetlight_TT.bam", render, 58.8, 93.6, 3,
                                    -90, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight3", "phase_3.5/models/props/streetlight_TT.bam", render, 95, 93.6, 3,
                                    -90, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight4", "phase_3.5/models/props/streetlight_TT.bam", render, 134, -126, 3,
                                    -130, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight5", "phase_3.5/models/props/streetlight_TT.bam", render, 108, -28, 4,
                                    -90, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight6", "phase_3.5/models/props/streetlight_TT.bam", render, 108, 32, 4,
                                    -90, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight7", "phase_3.5/models/props/streetlight_TT.bam", render, 32, 61, 4, -90,
                                    0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight8", "phase_3.5/models/props/streetlight_TT.bam", render, 28, -57, 4,
                                    -90, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight9", "phase_3.5/models/props/streetlight_TT.bam", render, -101, -70, 0.5,
                                    80, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight10", "phase_3.5/models/props/streetlight_TT.bam", render, -129, -42.5,
                                    0.5, 90, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight11", "phase_3.5/models/props/streetlight_TT.bam", render, 3.8, 118, 3,
                                    -110, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight12", "phase_3.5/models/props/streetlight_TT.bam", render, 116, 146, 3,
                                    145, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight13", "phase_3.5/models/props/streetlight_TT.bam", render, 86, 164, 3,
                                    -95, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight14", "phase_3.5/models/props/streetlight_TT.bam", render, 45.5, -88, 3,
                                    -2, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight15", "phase_3.5/models/props/streetlight_TT.bam", render, 78.3, -88, 3,
                                    -2, 0, 0, 1, 1, 1)
        self.modelloaderstreetlight("Streetlight16", "phase_3.5/models/props/streetlight_TT.bam", render, 100, -157, 3,
                                    30, 0, 0, 1, 1, 1)

        # Trees
        self.modelloadercopyto("Tree1", "phase_3.5/models/props/trees.bam", "prop_tree_large_no_box_ul", render,
                               -80.9143, 79.7948, 0.2, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree2", "phase_3.5/models/props/trees.bam", "prop_tree_large_no_box_ul", render,
                               -26.1169, 73.7975, 0.2, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree3", "phase_3.5/models/props/trees.bam", "prop_tree_fat_no_box_ul", render, 7.14367,
                               100.346, 2.725, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree4", "phase_3.5/models/props/trees.bam", "prop_tree_fat_no_box_ul", render, 55.8308,
                               153.977, 2.725, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree5", "phase_3.5/models/props/trees.bam", "prop_tree_fat_no_box_ul", render, 102.359,
                               81.1646, 2.725, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree6", "phase_3.5/models/props/trees.bam", "prop_tree_fat_no_box_ul", render, 114.09,
                               57.3141, 2.725, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree7", "phase_3.5/models/props/trees.bam", "prop_tree_fat_no_box_ul", render, 143.598,
                               110.178, 2.725, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree8", "phase_3.5/models/props/trees.bam", "prop_tree_large_no_box_ul", render,
                               -128.41, 32.9562, 0.2, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree9", "phase_3.5/models/props/trees.bam", "prop_tree_large_no_box_ul", render,
                               -128.708, -23.9096, 0.2, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree10", "phase_3.5/models/props/trees.bam", "prop_tree_large_no_box_ul", render,
                               -52.4323, -73.2793, 0.2, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree11", "phase_3.5/models/props/trees.bam", "prop_tree_fat_no_box_ul", render, 7.00708,
                               -99.2181, 2.725, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree12", "phase_3.5/models/props/trees.bam", "prop_tree_small_no_box_ul", render,
                               96.5467, -145.522, 2.725, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree13", "phase_3.5/models/props/trees.bam", "prop_tree_small_no_box_ul", render,
                               119.57, -127.05, 2.725, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree14", "phase_3.5/models/props/trees.bam", "prop_tree_small_no_box_ul", render,
                               128.064, -60.4145, 2.725, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree15", "phase_3.5/models/props/trees.bam", "prop_tree_small_no_box_ul", render,
                               121.146, -45.0892, 2.725, 1, 1, 1, 1, 1, 1)
        self.modelloadercopyto("Tree16", "phase_3.5/models/props/trees.bam", "prop_tree_small_no_box_ul", render,
                               113.503, -57.8055, 2.725, 1, 1, 1, 1, 1, 1)

    def modelloader(self, nodename, modelpath, renderparent, x, y, z, h, p, r, scale1, scale2, scale3):
        self.modeldict[nodename] = loader.loadModel(modelpath)
        self.modeldict[nodename].reparentTo(renderparent)
        self.modeldict[nodename].setPos(x, y, z)
        self.modeldict[nodename].setHpr(h, p, r)
        self.modeldict[nodename].setScale(scale1, scale2, scale3)

    def modelloadercopyto(self, nodename, modelpath, findmodel, renderparent, x, y, z, h, p, r, scale1, scale2, scale3):
        self.modeldict[nodename] = loader.loadModel(modelpath)
        self.modeldict[nodename] = self.modeldict[nodename].find('**/' + findmodel).copyTo(renderparent)
        self.modeldict[nodename].setPos(x, y, z)
        self.modeldict[nodename].setHpr(h, p, r)
        self.modeldict[nodename].setScale(scale1, scale2, scale3)

    def modelloaderanimate(self, nodename, modelpath, animatepath, renderparent, x, y, z, h, p, r, scale1, scale2,
                           scale3, animation):
        self.modeldict[nodename] = Actor(modelpath, {animation: animatepath})
        self.modeldict[nodename].reparentTo(renderparent)
        self.modeldict[nodename].setPos(x, y, z)
        self.modeldict[nodename].setHpr(h, p, r)
        self.modeldict[nodename].setScale(scale1, scale2, scale3)
        self.modeldict[nodename].loop(animation)

    def textloader(self, nodename, Textnodename, Textname, Textdata, Fonttype, renderparent, x, y, z, h, p, r, scale1,
                   scale2, scale3, color1, color2, color3):
        Textname = TextNode(Textnodename)
        Textname.setText(Textdata)
        Textname.setFont(Fonttype)
        self.modeldict[nodename] = renderparent.attachNewNode(Textname)
        self.modeldict[nodename].setPos(x, y, z)
        self.modeldict[nodename].setHpr(h, p, r)
        self.modeldict[nodename].setScale(scale1, scale2, scale3)
        self.modeldict[nodename].setColor(color1, color2, color3)

    def modelloaderstreetlight(self, nodename, modelpath, renderparent, x, y, z, h, p, r, scale1, scale2, scale3):
        self.modeldict[nodename] = loader.loadModel(modelpath)
        self.modeldict[nodename].reparentTo(renderparent)
        self.modeldict[nodename].setPos(x, y, z)
        self.modeldict[nodename].setHpr(h, p, r)
        self.modeldict[nodename].setScale(scale1, scale2, scale3)
        self.modeldict[nodename].find('**/prop_post_light_base').hide();
        self.modeldict[nodename].find('**/p1').hide()
        self.modeldict[nodename].find('**/prop_post_one_light').hide();
        self.modeldict[nodename].find('**/p13').hide()


environ = EnvironmentTTC()
base.taskMgr.add(updateOnScreenDebug, 'UpdateOSD')

#Terrain

#playgroundarea = loader.loadModel('phase_4/models/neighborhoods/toontown_central.bam')
#playgroundarea.reparentTo(render)
#playgroundarea.setY(0)
#playgroundarea.setX(0)
#playgroundarea.setZ(0)

#prop1 =loader.loadModel('phase_4/models/modules/gazebo.bam')
#prop1.reparentTo(render)
#prop1.setX(9.67)
#prop1.setY(-60.35)
#rop1.setZ(-1.94)
#prop1.setH(94.76)

#PetShop =loader.loadModel('phase_4/models/modules/PetShopExterior_TT.bam')
#PetShop.reparentTo(render)
#PetShop.setX(-72.34)
#PetShop.setY(-126.02)
#PetShop.setZ(0.47)
#PetShop.setH(137.73)

#Tunnel1 =loader.loadModel('phase_4/models/modules/safe_zone_tunnel_TT.bam')
#Tunnel1.reparentTo(render)
#Tunnel1.setX(-54.23)
#Tunnel1.setY(-242.84)
#Tunnel1.setZ(-6.03)
#Tunnel1.setH(0)

#school =loader.loadModel('phase_4/models/modules/school_house.bam')
#school.reparentTo(render)
#school.setX(101.42)
#school.setY(140.14)
#school.setZ(0.00)
#school.setH(344.74)

#PartyGate =loader.loadModel('phase_4/models/modules/partyGate_TT.bam')
#PartyGate.reparentTo(render)
#PartyGate.setX(160.99)
#PartyGate.setY(90.97)
#PartyGate.setZ(2.58)
#PartyGate.setH(294.23)

#Library =loader.loadModel('phase_4/models/modules/library.bam')
#Library.reparentTo(render)
#Library.setX(52.11)
#Library.setY(89.81)
#Library.setZ(3.98)
#Library.setH(270.00)

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
cog17.setX(45.42)
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
hat.setH(45.19)
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

base.oobe()
base.run()
