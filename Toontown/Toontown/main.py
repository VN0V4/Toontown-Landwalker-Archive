# NOTE: I GENUINELY DON'T KNOW WHO WROTE THIS. IT DATES BACK TO 2014 AND I MADE THIS
# PROJECT BACK IN 2018.
# IF SOMEONE COULD HELP ME FIGURE OUT THE AUTHOR OF THIS LANDWALKER THAT'D BE COOL!
# -- Luca

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

base.disableMouse()

toonmono = Filename("phase_3/models/gui/toonmono.cur")
wp = WindowProperties()
wp.setCursorFilename(toonmono)
wp.setTitle("Cog Training")
base.win.requestProperties(wp)

class LOAD:
	def loadGame(self):
		self.TRAINING_GROUND = loader.loadModel("phase_5.5/models/estate/terrain.bam")
		self.TRAINING_GROUND_SKY = loader.loadModel("phase_3.5/models/props/TT_sky.bam")

		self.FEATHER = Actor("phase_5/models/props/feather-mod.bam",
							{"chan": "phase_5/models/props/feather-chan.bam"})

		self.TICKLE_SFX = loader.loadSfx("phase_5/audio/sfx/AA_heal_tickle.mp3")

		self.FWD = loader.loadSfx("phase_3/audio/sfx/GUI_create_toon_fwd.mp3")
		self.RLVR = loader.loadSfx("phase_3/audio/sfx/GUI_rollover.mp3")

		self.DIALOG_BOX = loader.loadModel("phase_3/models/gui/dialog_box_gui.bam")
		self.DB_BTNS = loader.loadModel("phase_3/models/gui/dialog_box_buttons_gui.bam")
		self.GENBTN = loader.loadModel("phase_3/models/gui/quit_button.bam")
		self.ARROWS = loader.loadModel("phase_3/models/gui/create_a_toon_gui.bam")
		## WHY DON'T I HAVE THIS FILE?!
		#self.WEAPON_ICONS = loader.loadModel("phase_3/models/gui/weapon_icons.bam")

		self.FONT3 = loader.loadFont("phase_3/models/fonts/MickeyFont.bam")
		self.B_CAKE = loader.loadModel("phase_5/models/props/birthday-cake-mod.bam")
		self.C_CAKE = loader.loadModel("phase_6/models/golf/picnic_cupcake.bam")
		self.C_CAKE.setTwoSided(True)
		self.C_CAKE.setScale(3)

		self.AVA_SHIRT = loader.loadTexture("phase_4/maps/tt_t_chr_avt_shirt_cogbuster.jpg")
		self.AVA_SLEEVE = loader.loadTexture("phase_4/maps/tt_t_chr_avt_shirtSleeve_cogbuster.jpg")
		self.AVA_SHORTS = loader.loadTexture("phase_4/maps/tt_t_chr_avt_shorts_cogbuster.jpg")

		self.WEAPON_SELECT = loader.loadSfx("phase_3/audio/sfx/GUI_weapon_select.wav")


		self.COACH_SHIRT = loader.loadTexture("phase_4/maps/tt_t_chr_avt_shirt_sellbotCrusher.jpg")
		self.COACH_SLEEVE = loader.loadTexture("phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotCrusher.jpg")
		self.COACH_SHORTS = loader.loadTexture("phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg")

		self.LOSE_SFX = loader.loadSfx("phase_5/audio/sfx/ENC_Lose.mp3")


		self.MC_HELP1 = loader.loadSfx("phase_9/audio/sfx/morsecode_signal_help_01.wav")

		self.VD_SFX = loader.loadSfx("phase_3.5/audio/sfx/ENC_Win.mp3")

		self.PROP = Actor("phase_4/models/props/propeller-mod.bam",
							{"spin": "phase_4/models/props/propeller-chan.bam"})
		self.PROP_SFX = loader.loadSfx("phase_5/audio/sfx/ENC_propeller_in.mp3")
		self.PROP_SFX.setVolume(2.0)
		self.PROP_IDLE = loader.loadSfx("phase_4/audio/sfx/TB_propeller_1.5.wav")
		self.PROP_IDLE.setVolume(2.0)

		self.KNIFE = loader.loadModel("phase_5/models/props/dagger.bam")

		self.COG_STATEMENT = loader.loadSfx("phase_3.5/audio/dial/COG_VO_statement.mp3")
		self.COG_GRUNT = loader.loadSfx("phase_3.5/audio/dial/COG_VO_grunt.mp3")

		self.BOSS_STATEMENT = loader.loadSfx("phase_9/audio/sfx/Boss_COG_VO_statement.mp3")
		self.BOSS_GRUNT = loader.loadSfx("phase_9/audio/sfx/Boss_COG_VO_grunt.mp3")

		self.AVA_TS = loader.loadTexture("phase_4/maps/tt_t_chr_avt_acc_sho_tennisShoesGreen.jpg")

		self.RUN_LOOP = loader.loadSfx("phase_3.5/audio/sfx/AV_footstep_runloop.wav")
		self.RUN_LOOP.setLoop(True)
		self.WLK_LOOP = loader.loadSfx("phase_3.5/audio/sfx/AV_footstep_walkloop.wav")
		self.WLK_LOOP.setLoop(True)

		self.R3_BGM = loader.loadSfx("phase_12/audio/bgm/BossBot_CEO_v2.mid")
		self.R3_BGM.setLoop(True)
		self.R3_BGM.setVolume(1)

		self.COG_DIE_SFX = loader.loadSfx("phase_3.5/audio/sfx/Cog_Death.mp3")

		self.PIE = loader.loadModel("phase_3.5/models/props/tart.bam")
		self.TIE = loader.loadModel("phase_5/models/props/power-tie.bam")
		self.TIE.setBillboardAxis()
		self.TIE.setScale(2.0)

		self.COG_2_LOSE = Actor("phase_3.5/models/char/suitC-lose-mod.bam",
								{"lose": "phase_3.5/models/char/suitC-lose.bam"})

		self.COG_HEAD2 = loader.loadModel("phase_3.5/models/char/suitC-heads.bam")
		self.TW_HEAD = self.COG_HEAD2.find('**/tightwad')

		self.COG_2 = Actor("phase_3.5/models/char/suitC-mod.bam",
							{"walk": "phase_3.5/models/char/suitC-walk.bam",
							"neutral": "phase_3.5/models/char/suitC-neutral.bam",
							"land": "phase_3.5/models/char/suitC-landing.bam",
							"throw": "phase_3.5/models/char/suitC-throw-paper.bam",
							"pie": "phase_3.5/models/char/suitC-pie-small.bam",
							"dial": "phase_3.5/models/char/suitC-phone.bam",
							"knife": "phase_3.5/models/char/suitC-glower.bam"})

		#self.COG_2.reparentTo(render)
		self.TW_HEAD.reparentTo(self.COG_2.find('**/joint_head'))


		self.COG_MUSIC = loader.loadSfx("phase_7/audio/bgm/encntr_suit_winning_indoor.mid")
		self.COG_MUSIC.setLoop(True)
		self.COG_MUSIC.setVolume(0.5)

		self.COG_LOSE = Actor("phase_4/models/char/suitB-lose-mod.bam",
							{"lose": "phase_4/models/char/suitB-lose.bam"})

		self.JUMP_START_SFX = loader.loadSfx("phase_5/audio/sfx/General_throw_miss.wav")
		self.JUMP_END_SFX = loader.loadSfx("phase_3.5/audio/sfx/ENC_cogfall_apart.wav")

		self.FONT2 = loader.loadFont("phase_3/models/fonts/vtRemingtonPortable.ttf")

		self.AVATAR_HEAD = Actor("phase_3/models/char/tt_a_chr_dgm_skirt_head_1000.bam",
								{"neutral": "phase_3/models/char/tt_a_chr_dgm_skirt_head_neutral.bam",
								"run": "phase_3/models/char/tt_a_chr_dgm_skirt_head_run.bam",
								"walk": "phase_3/models/char/tt_a_chr_dgm_skirt_head_walk.bam",
								"pie": "phase_3/models/char/tt_a_chr_dgm_skirt_head_pie-throw.bam",
								"jump": "phase_3/models/char/tt_a_chr_dgm_skirt_head_jump.bam",
								"slipf": "phase_3/models/char/tt_a_chr_dgm_skirt_head_slip-forward.bam",
								"slipb": "phase_3/models/char/tt_a_chr_dgm_skirt_head_slip-backward.bam",
								"lose": "phase_3/models/char/tt_a_chr_dgm_skirt_head_lose.bam",
								"vd": "phase_3/models/char/tt_a_chr_dgm_skirt_head_victory-dance.bam",
								"cringe": "phase_3/models/char/tt_a_chr_dgm_skirt_head_cringe.bam"})

		self.AVATAR_TORSO = Actor("phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam",
								{"neutral": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam",
								"run": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_run.bam",
								"walk": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_walk.bam",
								"pie": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_pie-throw.bam",
								"jump": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_jump.bam",
								"slipf": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_slip-forward.bam",
								"slipb": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_slip-backward.bam",
								"lose": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_lose.bam",
								"vd": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_victory-dance.bam",
								"cringe": "phase_3/models/char/tt_a_chr_dgl_shorts_torso_cringe.bam"})

		self.AVATAR_LEGS = Actor("phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam",
								{"neutral": "phase_3/models/char/tt_a_chr_dgm_shorts_legs_neutral.bam",
								"run": "phase_3/models/char/tt_a_chr_dgm_shorts_legs_run.bam",
								"walk": "phase_3/models/char/tt_a_chr_dgm_shorts_legs_walk.bam",
								"pie": "phase_3/models/char/tt_a_chr_dgm_shorts_legs_pie-throw.bam",
								"jump": "phase_3/models/char/tt_a_chr_dgm_shorts_legs_jump.bam",
								"slipf": "phase_3/models/char/tt_a_chr_dgm_shorts_legs_slip-forward.bam",
								"slipb": "phase_3/models/char/tt_a_chr_dgm_shorts_legs_slip-backward.bam",
								"lose": "phase_3/models/char/tt_a_chr_dgm_shorts_legs_lose.bam",
								"vd": "phase_3/models/char/tt_a_chr_dgm_shorts_legs_victory-dance.bam",
								"cringe": "phase_3/models/char/tt_a_chr_dgm_shorts_legs_cringe.bam"})

		self.AVATAR_LEGS.find('**/shoes').setTexture(self.AVA_TS, 1)

		self.COACH_HEAD = loader.loadModel("phase_3/models/char/pig-heads-1000.bam")
		self.COACH_TORSO = Actor("phase_3/models/char/tt_a_chr_dgs_shorts_torso_1000.bam",
											{"neutral": "phase_3/models/char/tt_a_chr_dgs_shorts_torso_neutral.bam",
											"run": "phase_3/models/char/tt_a_chr_dgs_shorts_torso_run.bam",
											"walk": "phase_3/models/char/tt_a_chr_dgs_shorts_torso_walk.bam",
											"tickle": "phase_3/models/char/tt_a_chr_dgs_shorts_torso_tickle.bam"})

		self.COACH_LEGS = Actor("phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam",
											{"neutral": "phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral.bam",
											"run": "phase_3/models/char/tt_a_chr_dgs_shorts_legs_run.bam",
											"walk": "phase_3/models/char/tt_a_chr_dgs_shorts_legs_walk.bam",
											"tickle": "phase_3/models/char/tt_a_chr_dgs_shorts_legs_tickle.bam"})

		self.FONT1 = loader.loadFont("phase_3/models/fonts/ImpressBT.ttf")

		self.COACH_DIAL = loader.loadSfx("phase_3.5/audio/dial/coach.wav")

		self.BOX = loader.loadModel("phase_3/models/props/chatbox.bam")

		self.COG_1 = Actor("phase_3.5/models/char/suitB-mod.bam",
						{"walk": "phase_3.5/models/char/suitB-walk.bam",
						"neutral": "phase_3.5/models/char/suitB-neutral.bam",
						"land": "phase_3.5/models/char/suitB-landing.bam",
						"throw": "phase_3.5/models/char/suitB-throw-object.bam",
						"throwp": "phase_3.5/models/char/suitB-throw-paper.bam",
						"jump": "phase_3.5/models/char/suitB-jump.bam",
						"pie": "phase_3.5/models/char/suitB-pie-small.bam",
						"dial": "phase_3.5/models/char/suitB-phone.bam"})


		self.COG_1_HEAD = loader.loadModel("phase_4/models/char/suitB-heads.bam")

		self.SHADOW_AVATAR = loader.loadModel("phase_3/models/props/drop_shadow.bam")
		self.SAVNP = NodePath("avatar shadow")
		self.SHADOW_AVATAR.reparentTo(self.SAVNP)
		self.SHADOW_COG = loader.loadModel("phase_3/models/props/drop_shadow.bam")
		self.SCONP = NodePath("cog shadow")
		self.SHADOW_COG.reparentTo(self.SCONP)
		self.SHADOW_COACH = loader.loadModel("phase_3/models/props/drop_shadow.bam")
		self.SCNP = NodePath("coach shadow")
		self.SHADOW_COACH.reparentTo(self.SCNP)

		self.PIE_SPLAT_SFX = loader.loadSfx("phase_4/audio/sfx/AA_wholepie_only.mp3")
		self.PIE_THROW_SFX = loader.loadSfx("phase_3.5/audio/sfx/AA_pie_throw_only.mp3")

		self.SPLAT = Actor("phase_3.5/models/props/splat-mod.bam",
							{"chan": "phase_3.5/models/props/splat-chan.bam"})
		self.SPLAT.setColor(0.996094, 0.898438, 0.320312, 1.0)

		self.COG_CHECKPOINT1 = TextNode("Cog checkpoint 1")
		## WHY IS THIS COMMENTED?!
		#self.COG_CHECKPOINT1.setText("Checkpoint1")
		self.COG_CHECKPOINT1.setAlign(TextNode.ACenter)
		self.COG_CP1_NP = render.attachNewNode(self.COG_CHECKPOINT1)
		self.COG_CP1_NP.reparentTo(render)
		self.COG_CP1_NP.setBillboardAxis()
		self.COG_CP1_NP.setPos(49.03, -7.05, 8)

		self.COG_CHECKPOINT2 = TextNode("Cog checkpoint 2")
		#self.COG_CHECKPOINT2.setText("Checkpoint2")
		self.COG_CHECKPOINT2.setAlign(TextNode.ACenter)
		self.COG_CP2_NP = render.attachNewNode(self.COG_CHECKPOINT2)
		self.COG_CP2_NP.reparentTo(render)
		self.COG_CP2_NP.setBillboardAxis()
		self.COG_CP2_NP.setPos(40.47, 59.09, 1.00)

		self.COG_CHECKPOINT3 = TextNode("Cog checkpoint 3")
		#self.COG_CHECKPOINT3.setText("Checkpoint3")
		self.COG_CHECKPOINT3.setAlign(TextNode.ACenter)
		self.COG_CP3_NP = render.attachNewNode(self.COG_CHECKPOINT3)
		self.COG_CP3_NP.reparentTo(render)
		self.COG_CP3_NP.setBillboardAxis()
		self.COG_CP3_NP.setPos(-22.18, 71.07, 0)

		self.COG_CHECKPOINT4 = TextNode("Cog checkpoint 4")
		#self.COG_CHECKPOINT4.setText("Checkpoint4")
		self.COG_CHECKPOINT4.setAlign(TextNode.ACenter)
		self.COG_CP4_NP = render.attachNewNode(self.COG_CHECKPOINT4)
		self.COG_CP4_NP.reparentTo(render)
		self.COG_CP4_NP.setBillboardAxis()
		self.COG_CP4_NP.setPos(-26.85, 29.85, 3.00)

		self.COG_CHECKPOINT5 = TextNode("Cog checkpoint 5")
		#self.COG_CHECKPOINT5.setText("Checkpoint5")
		self.COG_CHECKPOINT5.setAlign(TextNode.ACenter)
		self.COG_CP5_NP = render.attachNewNode(self.COG_CHECKPOINT5)
		self.COG_CP5_NP.reparentTo(render)
		self.COG_CP5_NP.setBillboardAxis()
		self.COG_CP5_NP.setPos(-88.57, 27.09, 1.00)

		self.COG_CHECKPOINT6 = TextNode("Cog checkpoint 6")
		#self.COG_CHECKPOINT6.setText("Checkpoint6")
		self.COG_CHECKPOINT6.setAlign(TextNode.ACenter)
		self.COG_CP6_NP = render.attachNewNode(self.COG_CHECKPOINT6)
		self.COG_CP6_NP.reparentTo(render)
		self.COG_CP6_NP.setBillboardAxis()
		self.COG_CP6_NP.setPos(-44.92, -45.81, 5.00)

		self.COG_CHECKPOINT7 = TextNode("Cog checkpoint 7")
		#self.COG_CHECKPOINT7.setText("Checkpoint7")
		self.COG_CHECKPOINT7.setAlign(TextNode.ACenter)
		self.COG_CP7_NP = render.attachNewNode(self.COG_CHECKPOINT7)
		self.COG_CP7_NP.reparentTo(render)
		self.COG_CP7_NP.setBillboardAxis()
		self.COG_CP7_NP.setPos(23.12, -58.39, 1.00)

		self.COG_CHECKPOINT8 = TextNode("Cog checkpoint 8")
		#self.COG_CHECKPOINT8.setText("Checkpoint8")
		self.COG_CHECKPOINT8.setAlign(TextNode.ACenter)
		self.COG_CP8_NP = render.attachNewNode(self.COG_CHECKPOINT8)
		self.COG_CP8_NP.reparentTo(render)
		self.COG_CP8_NP.setBillboardAxis()
		self.COG_CP8_NP.setPos(67.51, -26.35, 9.00)
class SCENE:
	def enterFullscreen(self):
		base.accept('alt-enter', self.exitFullscreen)
		wp.setFullscreen(True)
		wp.setSize(1366, 768)
		base.win.requestProperties(wp)
	def exitFullscreen(self):
		base.accept('alt-enter', self.enterFullscreen)
		wp.setFullscreen(False)
		wp.setSize(800, 600)
		base.win.requestProperties(wp)
	def initScene(self):
		self.ROUND = 0
		base.accept('alt-enter', self.enterFullscreen)
		L.AVATAR_HEAD.loop("neutral")
		L.AVATAR_TORSO.loop("neutral")
		L.AVATAR_LEGS.loop("neutral")
		L.TRAINING_GROUND.reparentTo(render)
		L.TRAINING_GROUND.setTwoSided(True)
		L.TRAINING_GROUND.setTransparency(TransparencyAttrib.MBinary, 1)

		L.TRAINING_GROUND_SKY.reparentTo(render)

		L.COACH_LEGS.reparentTo(render)
		L.COACH_LEGS.setPos(-84.00, 52.02, 0.00)
		L.COACH_LEGS.setH(206.57)
		L.COACH_LEGS.find('**/legs').setColor(0.304688, 0.96875, 0.402344, 1.0)
		L.COACH_LEGS.find('**/feet').setColor(0.304688, 0.96875, 0.402344, 1.0)
		L.COACH_LEGS.find('**/boots_long').hide()
		L.COACH_LEGS.find('**/boots_short').hide()
		L.COACH_LEGS.find('**/shoes').hide()

		L.COACH_TORSO.reparentTo(L.COACH_LEGS.find('**/joint_hips'))
		L.COACH_TORSO.find('**/arms').setColor(0.304688, 0.96875, 0.402344, 1.0)
		L.COACH_TORSO.find('**/neck').setColor(0.304688, 0.96875, 0.402344, 1.0)
		L.COACH_TORSO.find('**/hands').setColor(1.0, 1.0, 1.0, 1.0)
		L.COACH_TORSO.find('**/torso-top').setTexture(L.COACH_SHIRT, 1)
		L.COACH_TORSO.find('**/torso-bot').setTexture(L.COACH_SHORTS, 1)
		L.COACH_TORSO.find('**/sleeves').setTexture(L.COACH_SLEEVE, 1)

		L.COACH_HEAD.reparentTo(L.COACH_TORSO.find('**/def_head'))
		L.COACH_HEAD.find('**/head-front-long').setColor(0.304688, 0.96875, 0.402344, 1.0)
		L.COACH_HEAD.find('**/head-long').setColor(0.304688, 0.96875, 0.402344, 1.0)
		L.COACH_HEAD.find('**/ears-long').setColor(0.304688, 0.96875, 0.402344, 1.0)
		L.COACH_HEAD.find('**/joint_pupilR_short').hide()
		L.COACH_HEAD.find('**/joint_pupilL_short').hide()
		L.COACH_HEAD.find('**/eyes-short').hide()
		L.COACH_HEAD.find('**/ears-short').hide()
		L.COACH_HEAD.find('**/head-front-short').hide()
		L.COACH_HEAD.find('**/head-short').hide()
		L.COACH_HEAD.find('**/muzzle-long-laugh').hide()
		L.COACH_HEAD.find('**/muzzle-long-angry').hide()
		L.COACH_HEAD.find('**/muzzle-long-smile').hide()
		L.COACH_HEAD.find('**/muzzle-long-sad').hide()
		L.COACH_HEAD.find('**/muzzle-long-surprise').hide()
		L.COACH_HEAD.find('**/muzzle-short-neutral').hide()
		L.COACH_HEAD.find('**/muzzle-short-laugh').hide()
		L.COACH_HEAD.find('**/muzzle-short-smile').hide()
		L.COACH_HEAD.find('**/muzzle-short-sad').hide()
		L.COACH_HEAD.find('**/muzzle-short-surprise').hide()
		L.COACH_HEAD.find('**/muzzle-short-angry').hide()

		L.COG_1.reparentTo(render)
		L.COG_1.setPos(68.30, 53.08, 15.00)
		self.MS = L.COG_1_HEAD.find('**/movershaker')
		self.MS.reparentTo(L.COG_1.find('**/joint_head'))
		L.COG_1.hide()
		#L.COG_1.place()

		L.COACH_LEGS.loop("neutral")
		L.COACH_TORSO.loop("neutral")

		L.AVATAR_LEGS.reparentTo(render)
		L.AVATAR_LEGS.find('**/legs').setColor(0.191406, 0.5625, 0.773438, 1.0)
		L.AVATAR_LEGS.find('**/feet').setColor(0.191406, 0.5625, 0.773438, 1.0)
		L.AVATAR_LEGS.find('**/boots_long').hide()
		L.AVATAR_LEGS.find('**/boots_short').hide()
		L.AVATAR_LEGS.find('**/shoes').hide()

		L.AVATAR_TORSO.reparentTo(L.AVATAR_LEGS.find('**/joint_hips'))
		L.AVATAR_TORSO.find('**/arms').setColor(0.191406, 0.5625, 0.773438, 1.0)
		L.AVATAR_TORSO.find('**/neck').setColor(0.191406, 0.5625, 0.773438, 1.0)
		L.AVATAR_TORSO.find('**/torso-top').setTexture(L.AVA_SHIRT, 1)
		L.AVATAR_TORSO.find('**/torso-bot').setTexture(L.AVA_SHORTS, 1)
		L.AVATAR_TORSO.find('**/sleeves').setTexture(L.AVA_SLEEVE, 1)

		L.AVATAR_HEAD.reparentTo(L.AVATAR_TORSO.find('**/def_head'))
		L.AVATAR_HEAD.find('**/head-front').setColor(0.191406, 0.5625, 0.773438, 1.0)
		L.AVATAR_HEAD.find('**/head').setColor(0.191406, 0.5625, 0.773438, 1.0)

		self.COACH_TN = TextNode("Coach nametag")
		self.COACH_TN.setText("Coach")
		self.COACH_NT_NP = render.attachNewNode(self.COACH_TN)
		self.COACH_NT_NP.reparentTo(L.COACH_LEGS.find('**/joint_nameTag'))
		self.COACH_NT_NP.setBillboardAxis()
		self.COACH_NT_NP.setZ(4.5)
		self.COACH_TN.setAlign(TextNode.ACenter)
		self.COACH_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		self.COACH_TN.setCardAsMargin(0,0,0,-0.2 )
		self.COACH_TN.setCardDecal(True)
		self.COACH_TN.setTextColor(0.6, 0.4, 0.2, 1.0)
		self.COACH_NT_NP.setScale(0.4)
		self.COACH_TN.setFont(L.FONT1)

		self.AVA_TN = TextNode("Avatar nametag")
		self.AVA_TN.setText("Student")
		self.AVA_NT_NP = render.attachNewNode(self.AVA_TN)
		self.AVA_NT_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
		self.AVA_NT_NP.setBillboardAxis()
		self.AVA_NT_NP.setZ(5.3)
		self.AVA_TN.setAlign(TextNode.ACenter)
		self.AVA_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		self.AVA_TN.setCardAsMargin(0,0,0,-0.2 )
		self.AVA_TN.setCardDecal(True)
		self.AVA_TN.setTextColor(0.3254901960784314, 0.3215686274509804, 0.6823529411764706, 1.0)
		self.AVA_NT_NP.setScale(0.35, 1, 0.3)
		self.AVA_TN.setFont(L.FONT1)

		self.COG_TN = TextNode("m&s nametag")
		self.COG_TN.setText("Mover &\nShaker\nSellbot\nLevel 5")
		self.COG_NT_NP = render.attachNewNode(self.COG_TN)
		self.COG_NT_NP.reparentTo(L.COG_1.find('**/joint_nameTag'))
		self.COG_NT_NP.setBillboardAxis()
		self.COG_NT_NP.setZ(9)
		self.COG_TN.setAlign(TextNode.ACenter)
		self.COG_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		self.COG_TN.setCardAsMargin(0.1,0,0,-0.2 )
		self.COG_TN.setCardDecal(True)
		self.COG_TN.setTextColor(0,0,0,1.0)
		self.COG_NT_NP.setScale(0.35)
		self.COG_TN.setFont(L.FONT2)
		self.collisions()
	def collisions(self):
		self.keyMap = {"left":0, "right":0, "forward":0, "backward":0}
		self.COG2_HITS = 0
		self.COG1_HITS = 0
		self.isMoving_forward = False
		self.isMoving_side = False
		base.cTrav = CollisionTraverser()

		self.colEV = CollisionHandlerEvent()
		self.groundHandler = CollisionHandlerFloor()
		self.wallHandler = CollisionHandlerPusher()

		self.FLOOR_MASK=BitMask32.bit(1)

		self.WALL_MASK=BitMask32.bit(2)

		self.TRIGGER_MASK=BitMask32.bit(3)

		self.HITBOX_MASK=BitMask32.bit(4)
		self.HITBOX2_MASK=BitMask32.bit(5)

		self.COACH_MASK=BitMask32.bit(6)

		L.AVATAR_LEGS.setCollideMask(BitMask32.allOff())
		self.LEGSNP = NodePath('toonlegsnp')
		self.LEGSNP.reparentTo(L.AVATAR_LEGS)
		self.LEGSNP.setZ(5)
		self.avatarCollider = L.AVATAR_LEGS.attachNewNode(CollisionNode('LEGSCNODE'))
		self.avatarCollider.node().addSolid(CollisionSphere(0,0,0,1))
		self.avatarCollider.node().setFromCollideMask(self.WALL_MASK)
		self.avatarCollider.node().setIntoCollideMask(BitMask32.allOff())
		self.avatarCollider.setSz(5)
		self.avatarCollider2 = L.AVATAR_LEGS.attachNewNode(CollisionNode('LEGSCHIT'))
		self.avatarCollider2.node().addSolid(CollisionSphere(0,0,0,1))
		self.avatarCollider2.node().setFromCollideMask(BitMask32.allOff())
		self.avatarCollider2.node().setIntoCollideMask(self.HITBOX_MASK)
		self.avatarCollider2.setSz(6)
		self.avatarCollider3 = L.AVATAR_LEGS.attachNewNode(CollisionNode('LEGSCHIT2'))
		self.avatarCollider3.node().addSolid(CollisionSphere(0,0,0,1))
		self.avatarCollider3.node().setFromCollideMask(BitMask32.allOff())
		self.avatarCollider3.node().setIntoCollideMask(self.HITBOX2_MASK)
		self.avatarCollider3.setSz(6)
		self.avatarSensor = L.AVATAR_LEGS.attachNewNode(CollisionNode('avatarSensor'))
		self.avatarSensor.node().addSolid(CollisionSphere(0,0,0,1.2))
		self.avatarSensor.node().setFromCollideMask(self.WALL_MASK|self.TRIGGER_MASK)
		self.avatarSensor.node().setIntoCollideMask(BitMask32.allOff())
		self.avatarSensorCoach = L.AVATAR_LEGS.attachNewNode(CollisionNode('avatarSensorCoach'))
		self.avatarSensorCoach.node().addSolid(CollisionSphere(0,0,0,1.2))
		self.avatarSensorCoach.node().setFromCollideMask(self.COACH_MASK)
		self.avatarSensorCoach.node().setIntoCollideMask(BitMask32.allOff())
		self.raygeometry = CollisionRay(0, 0, 2, 0, 0, -1)
		self.avatarRay = self.LEGSNP.attachNewNode(CollisionNode('avatarRay'))
		self.avatarRay.node().addSolid(self.raygeometry)
		self.avatarRay.node().setFromCollideMask(self.FLOOR_MASK)
		self.avatarRay.node().setIntoCollideMask(BitMask32.allOff())

		self.CLEGSNP = NodePath('Ctoonlegsnp')
		self.CLEGSNP.reparentTo(L.COACH_LEGS)
		self.CLEGSNP.setZ(5.8)
		self.CavatarCollider = L.COACH_LEGS.attachNewNode(CollisionNode('CLEGSCNODE'))
		self.CavatarCollider.node().addSolid(CollisionSphere(0,0,0,1))
		self.CavatarCollider.node().setFromCollideMask(BitMask32.allOff())
		self.CavatarCollider.node().setIntoCollideMask(self.WALL_MASK|self.COACH_MASK)
		self.CavatarSensor = L.COACH_LEGS.attachNewNode(CollisionNode('CavatarSensor'))
		self.CavatarSensor.node().addSolid(CollisionSphere(0,0,0,1.2))
		self.CavatarSensor.node().setFromCollideMask(self.WALL_MASK|self.TRIGGER_MASK)
		self.CavatarSensor.node().setIntoCollideMask(BitMask32.allOff())
		self.Craygeometry = CollisionRay(0, 0, 2, 0, 0, -1)
		self.CavatarRay = self.CLEGSNP.attachNewNode(CollisionNode('CavatarRay'))
		self.CavatarRay.node().addSolid(self.raygeometry)
		self.CavatarRay.node().setFromCollideMask(self.FLOOR_MASK)
		self.CavatarRay.node().setIntoCollideMask(BitMask32.allOff())

		L.TRAINING_GROUND.setCollideMask(BitMask32.allOff())
		wallcollider1=L.TRAINING_GROUND.find("**/terrain_barrier")
		wallcollider1.node().setIntoCollideMask(self.WALL_MASK)
		wallcollider2=L.TRAINING_GROUND.find("**/collision_fence")
		wallcollider2.node().setIntoCollideMask(self.WALL_MASK)

		floorcollider1=L.TRAINING_GROUND.find("**/collision4")
		floorcollider1.node().setIntoCollideMask(self.FLOOR_MASK)
		floorcollider2=L.TRAINING_GROUND.find("**/collision3")
		floorcollider2.node().setIntoCollideMask(self.FLOOR_MASK)
		floorcollider3=L.TRAINING_GROUND.find("**/collision1")
		floorcollider3.node().setIntoCollideMask(self.FLOOR_MASK)

		self.groundHandler.addCollider(self.avatarRay, L.AVATAR_LEGS)

		self.wallHandler.addCollider(self.avatarCollider, L.AVATAR_LEGS)

		self.wallHandler.addCollider(self.avatarCollider2, L.AVATAR_LEGS)

		self.groundHandler.addCollider(self.CavatarRay, L.COACH_LEGS)

		self.wallHandler.addCollider(self.CavatarCollider, L.COACH_LEGS)


		base.cTrav.addCollider(self.avatarRay, self.groundHandler)
		base.cTrav.addCollider(self.avatarCollider, self.wallHandler)
		base.cTrav.addCollider(self.avatarCollider2, self.wallHandler)
		base.cTrav.addCollider(self.avatarSensor, self.colEV)
		base.cTrav.addCollider(self.avatarSensorCoach, self.colEV)

		base.cTrav.addCollider(self.CavatarRay, self.groundHandler)
		base.cTrav.addCollider(self.CavatarCollider, self.wallHandler)
		base.cTrav.addCollider(self.CavatarSensor, self.colEV)

		self.colEV.addInPattern('%fn-into')
		self.colEV.addOutPattern('%fn-out')

		base.accept("arrow_left", self.setKey, ["left",1])
		base.accept("arrow_right", self.setKey, ["right",1])
		base.accept("arrow_up", self.setKey, ["forward",1])
		base.accept("arrow_down", self.setKey, ["backward",1])
		base.accept("arrow_left-up", self.setKey, ["left",0])
		base.accept("arrow_right-up", self.setKey, ["right",0])
		base.accept("arrow_up-up", self.setKey, ["forward",0])
		base.accept("arrow_down-up", self.setKey, ["backward",0])
		base.accept("a", self.setKey, ["left",1])
		base.accept("d", self.setKey, ["right",1])
		base.accept("w", self.setKey, ["forward",1])
		base.accept("s", self.setKey, ["backward",1])
		base.accept("a-up", self.setKey, ["left",0])
		base.accept("d-up", self.setKey, ["right",0])
		base.accept("w-up", self.setKey, ["forward",0])
		base.accept("s-up", self.setKey, ["backward",0])
		base.accept("s-w", self.setKey, ["backward",1])
		base.accept("w-s", self.setKey, ["forward",1])
		base.accept("arrow_down-arrow_up", self.setKey, ["backward",1])
		base.accept("arrow_up-arrow_down", self.setKey, ["forward",1])
		base.accept("space", self.JUMP)
		base.accept('avatarSensor-into', self.checkCollisions)
		base.accept('1', self.COG_SPAWN1)
		self.COACH_WHSP1 = OnscreenText(text="COACH: Welcome to Cog Training! To begin, press the 1 key.", scale=0.06, pos=(-1.1, -0.7, -0.7), wordwrap=7, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
		self.COACH_WHSP1_2 = OnscreenText(text="COACH: Want to get information about a Cog? Just walk up to me.", scale=0.06, pos=(0.7, -0.7, -0.7), wordwrap=9, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
		taskMgr.add(self.move, "movetask")
	def JUMP(self):
		self.isMoving_forward = False
		self.isMoving_side = False
		self.keyMap = {"left":0, "right":0, "forward":0, "backward":0}
		L.RUN_LOOP.stop()
		L.WLK_LOOP.stop()
		base.accept("arrow_left", self.setKey, ["left",0])
		base.accept("arrow_right", self.setKey, ["right",0])
		base.accept("arrow_up", self.setKey, ["forward",0])
		base.accept("arrow_down", self.setKey, ["backward",0])
		base.accept("arrow_left-up", self.setKey, ["left",0])
		base.accept("arrow_right-up", self.setKey, ["right",0])
		base.accept("arrow_up-up", self.setKey, ["forward",0])
		base.accept("arrow_down-up", self.setKey, ["backward",0])
		base.accept("arrow_down-arrow_up", self.setKey, ["backward",0])
		base.accept("arrow_up-arrow_down", self.setKey, ["forward",0])
		base.accept("a", self.setKey, ["left",0])
		base.accept("d", self.setKey, ["right",0])
		base.accept("w", self.setKey, ["forward",0])
		base.accept("s", self.setKey, ["backward",0])
		base.accept("a-up", self.setKey, ["left",0])
		base.accept("d-up", self.setKey, ["right",0])
		base.accept("w-up", self.setKey, ["forward",0])
		base.accept("s-up", self.setKey, ["backward",0])
		base.accept("s-w", self.setKey, ["backward",0])
		base.accept("w-s", self.setKey, ["forward",0])
		base.accept("space", self.nul)
		base.accept("control-up", self.nul)
		base.accept("control", self.nul)
		self.AVATAR_MOTION = 'JUMPING'
		L.AVATAR_HEAD.play("jump")
		L.AVATAR_TORSO.play("jump")
		L.AVATAR_LEGS.play("jump")
		taskMgr.doMethodLater(1.5, self.STOP_JUMP, "stop jump")
	def STOP_JUMP(self, task):
		base.accept("arrow_left", self.setKey, ["left",1])
		base.accept("arrow_right", self.setKey, ["right",1])
		base.accept("arrow_up", self.setKey, ["forward",1])
		base.accept("arrow_down", self.setKey, ["backward",1])
		base.accept("arrow_left-up", self.setKey, ["left",0])
		base.accept("arrow_right-up", self.setKey, ["right",0])
		base.accept("arrow_up-up", self.setKey, ["forward",0])
		base.accept("arrow_down-up", self.setKey, ["backward",0])
		base.accept("arrow_down-arrow_up", self.setKey, ["backward",1])
		base.accept("arrow_up-arrow_down", self.setKey, ["forward",1])
		base.accept("a", self.setKey, ["left",1])
		base.accept("d", self.setKey, ["right",1])
		base.accept("w", self.setKey, ["forward",1])
		base.accept("s", self.setKey, ["backward",1])
		base.accept("a-up", self.setKey, ["left",0])
		base.accept("d-up", self.setKey, ["right",0])
		base.accept("w-up", self.setKey, ["forward",0])
		base.accept("s-up", self.setKey, ["backward",0])
		base.accept("s-w", self.setKey, ["backward",1])
		base.accept("w-s", self.setKey, ["forward",1])
		base.accept("space", self.JUMP)
		base.accept('control-up', self.CHECK_ACTIVE_WEAPON_UP)
		base.accept('control', self.CHECK_ACTIVE_WEAPON_DN)
		self.AVATAR_MOTION = 'NORMAL'
		return task.done
	def nul(self):
		pass
	def RESTART_PIECOUNT(self, task):
		self.COG1_HITS = 0
		task.delayTime = 15
		return task.again
	def PIE_START(self):
		self.lastWeapon = 'TART'
		try:
			self.TOTALHITS += 1
		except:
			pass
		L.PIE.show()
		L.PIE.setPos(0,0,0)
		L.PIE.setHpr(0,0,0)
		L.PIE.reparentTo(L.AVATAR_TORSO.find('**/def_joint_right_hold'))
		L.AVATAR_HEAD.loop("pie", fromFrame=0, toFrame=45)
		L.AVATAR_TORSO.loop("pie", fromFrame=0, toFrame=45)
		L.AVATAR_LEGS.loop("pie", fromFrame=0, toFrame=45)
	def C_CAKE_START(self):
		self.lastWeapon = 'CCAKE'
		try:
			self.TOTALHITS += 1
		except:
			pass
		L.C_CAKE.show()
		L.C_CAKE.setPos(0,0,0)
		L.C_CAKE.setHpr(0,0,0)
		L.C_CAKE.reparentTo(L.AVATAR_TORSO.find('**/def_joint_right_hold'))
		L.AVATAR_HEAD.loop("pie", fromFrame=0, toFrame=45)
		L.AVATAR_TORSO.loop("pie", fromFrame=0, toFrame=45)
		L.AVATAR_LEGS.loop("pie", fromFrame=0, toFrame=45)
	def B_CAKE_START(self):
		self.lastWeapon = 'BCAKE'
		try:
			self.TOTALHITS += 1
		except:
			pass
		L.B_CAKE.show()
		L.B_CAKE.setPos(0,0,0)
		L.B_CAKE.setHpr(0,0,0)
		L.B_CAKE.reparentTo(L.AVATAR_TORSO.find('**/def_joint_right_hold'))
		L.AVATAR_HEAD.loop("pie", fromFrame=0, toFrame=45)
		L.AVATAR_TORSO.loop("pie", fromFrame=0, toFrame=45)
		L.AVATAR_LEGS.loop("pie", fromFrame=0, toFrame=45)
	def COG_SPAWN1(self):
		self.ROUND = 1
		self.weapon = 'TART'
		base.accept('control-up', self.CHECK_ACTIVE_WEAPON_UP)
		base.accept('control', self.CHECK_ACTIVE_WEAPON_DN)
		base.accept('1', self.nul)
		self.COACH_WHSP1.remove()
		self.COACH_WHSP1_2.remove()
		#self.COACH_WHSP2 = OnscreenText(text="COACH: OK, this round is pretty simple. Grab some pies, hit the Cog with them, and don't touch him.", scale=0.06, pos=(-0.9, -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
		self.COACH_WHSP3 = OnscreenText(text="COACH: A Cog is flying in.", scale=0.06, pos=(0.8, -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
		L.COG_1.show()
		self.PIE_COL()
		self.C_CAKE_COL()
		self.B_CAKE_COL()
		L.COG_MUSIC.play()
		L.PROP_IDLE.play()
		taskMgr.doMethodLater(1.5, self.PROP_IN_SFX, "prop in sfx")
		L.COG_1.pose("land", 1)
		L.PROP.reparentTo(L.COG_1.find('**/joint_head'))
		L.PROP.loop("spin", fromFrame=0, toFrame=3)
		taskMgr.doMethodLater(5.5, self.PROP_IN, "propeller in")
		L.COG_1_FLYDOWN_INTERVAL = L.COG_1.posInterval(4,
													Point3(68.30, 53.08, 0.0),
													startPos=(68.30, 53.08, 15.00))
		L.COG_1_FLYDOWN_INTERVAL.start()
		taskMgr.doMethodLater(4, self.COG_LAND1, "cog land 1")
	def PROP_IN_SFX(self, task):
		L.PROP_SFX.play()
		return task.done
	def PROP_IN(self, task):
		L.PROP.play("spin", fromFrame=65, toFrame=87)
		return task.done
	def C_CAKE_COL(self):
		self.CCavatarSensor = L.C_CAKE.attachNewNode(CollisionNode('CCavatarSensor'))
		self.CCavatarSensor.node().addSolid(CollisionSphere(0,0,0,0.3))
		self.CCavatarSensor.node().setFromCollideMask(self.WALL_MASK|self.TRIGGER_MASK|self.FLOOR_MASK)
		self.CCavatarSensor.node().setIntoCollideMask(BitMask32.allOff())
		base.cTrav.addCollider(self.CCavatarSensor, self.colEV)
	def B_CAKE_COL(self):
		self.BavatarSensor = L.B_CAKE.attachNewNode(CollisionNode('BavatarSensor'))
		self.BavatarSensor.node().addSolid(CollisionSphere(0,0,0,1))
		self.BavatarSensor.node().setFromCollideMask(self.WALL_MASK|self.TRIGGER_MASK|self.FLOOR_MASK)
		self.BavatarSensor.node().setIntoCollideMask(BitMask32.allOff())
		base.cTrav.addCollider(self.BavatarSensor, self.colEV)
	def PIE_COL(self):
		self.PavatarSensor = L.PIE.attachNewNode(CollisionNode('PavatarSensor'))
		self.PavatarSensor.node().addSolid(CollisionSphere(0,0,0,1))
		self.PavatarSensor.node().setFromCollideMask(self.WALL_MASK|self.TRIGGER_MASK|self.FLOOR_MASK)
		self.PavatarSensor.node().setIntoCollideMask(BitMask32.allOff())
		base.cTrav.addCollider(self.PavatarSensor, self.colEV)
	def TIE_COL(self):
		self.TavatarSensor = L.TIE.attachNewNode(CollisionNode('TavatarSensor'))
		self.TavatarSensor.node().addSolid(CollisionSphere(0,0,0,0.4))
		self.TavatarSensor.node().setFromCollideMask(self.WALL_MASK|self.TRIGGER_MASK|self.FLOOR_MASK|self.HITBOX_MASK)
		self.TavatarSensor.node().setIntoCollideMask(BitMask32.allOff())
		base.cTrav.addCollider(self.TavatarSensor, self.colEV)
	def KNI_COLL(self):
		self.KavatarSensor = L.KNIFE.attachNewNode(CollisionNode('KavatarSensor'))
		self.KavatarSensor.node().addSolid(CollisionSphere(0,0,0,0.4))
		self.KavatarSensor.setSy(7)
		self.KavatarSensor.setSx(2)
		self.KavatarSensor.node().setFromCollideMask(self.WALL_MASK|self.TRIGGER_MASK|self.FLOOR_MASK|self.HITBOX2_MASK)
		self.KavatarSensor.node().setIntoCollideMask(BitMask32.allOff())
		base.cTrav.addCollider(self.KavatarSensor, self.colEV)
	def CHECK_PIE_COL(self, entry):
		L.PIE_SPLAT_SFX.play()
		L.SPLAT.reparentTo(render)
		L.SPLAT.show()
		L.SPLAT.setPos(L.PIE.getPos())
		L.SPLAT.setBillboardAxis()
		L.SPLAT.play("chan")
		taskMgr.doMethodLater(0.5, self.SPLAT_HIDE, "hide splat")
		if entry.getIntoNodePath().getName() == 'COGLEGSCNODE':
			self.COG1_HITS += 1
			try:
				if self.ROUND == 3:
					self.COG_HEALTH -= 10
					try:
						self.CH_NT_NP.remove()
					except:
						pass
					self.CH_TN = TextNode("damage done to cog")
					self.CH_TN.setText("-10")
					self.CH_NT_NP = render.attachNewNode(self.CH_TN)
					self.CH_NT_NP.reparentTo(L.COG_1.find('**/joint_nameTag'))
					self.CH_NT_NP.setBillboardAxis()
					self.CH_NT_NP.setZ(7)
					self.CH_TN.setAlign(TextNode.ACenter)
					self.CH_TN.setTextColor(0.9, 0, 0, 1.0)
					self.CH_NT_NP.setScale(1.5)
					self.CH_TN.setFont(L.FONT3)
					self.CH_TN_INT = self.CH_NT_NP.posInterval(0.5,
																Point3(0, 0, 9.5),
																startPos=(0, 0, 7),
																blendType='easeInOut')
					self.CH_TN_INT.start()
					taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_COG, "remove cog damage label")
					self.COG_HEALTH_LBL.setText("Cog health: " + str(self.COG_HEALTH))
			except:
				pass
		try:
			if entry.getIntoNodePath().getName() == 'COG2LEGSCNODE':
				self.COG2_HITS += 1
				self.BOSS_HEALTH -= 10
				try:
					self.CH_NT_NP.remove()
				except:
					pass
				self.BH_TN = TextNode("damage done to BOSS")
				self.BH_TN.setText("-10")
				self.BH_NT_NP = render.attachNewNode(self.BH_TN)
				self.BH_NT_NP.reparentTo(L.COG_2.find('**/joint_nameTag'))
				self.BH_NT_NP.setBillboardAxis()
				self.BH_NT_NP.setZ(4)
				self.BH_TN.setAlign(TextNode.ACenter)
				self.BH_TN.setTextColor(0.9, 0, 0, 1.0)
				self.BH_NT_NP.setScale(1.5)
				self.BH_TN.setFont(L.FONT3)
				self.BH_TN_INT = self.BH_NT_NP.posInterval(0.5,
															Point3(0, 0, 6.5),
															startPos=(0, 0, 4),
															blendType='easeInOut')
				self.BH_TN_INT.start()
				taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_BOSS, "remove BOSS damage label")
				self.BOSS_HEALTH_LBL.setText("Boss health: " + str(self.BOSS_HEALTH))
		except:
			pass

		self.trajectory.pause()
		L.PIE.reparentTo(render)
		L.PIE.setPos(0,0,-100)
		L.PIE.setHpr(0,0,0)

	def CHECK_CCAKE_COL(self, entry):
		print entry.getIntoNodePath().getName()
		L.PIE_SPLAT_SFX.play()
		L.SPLAT.reparentTo(render)
		L.SPLAT.show()
		L.SPLAT.setPos(L.C_CAKE.getPos())
		L.SPLAT.setBillboardAxis()
		L.SPLAT.play("chan")
		taskMgr.doMethodLater(0.5, self.SPLAT_HIDE, "hide splat")
		if entry.getIntoNodePath().getName() == 'COGLEGSCNODE':
			self.COG1_HITS += 1
			try:
				if self.ROUND == 3:
					self.COG_HEALTH -= 5
					try:
						self.CH_NT_NP.remove()
					except:
						pass
					self.CH_TN = TextNode("damage done to cog")
					self.CH_TN.setText("-5")
					self.CH_NT_NP = render.attachNewNode(self.CH_TN)
					self.CH_NT_NP.reparentTo(L.COG_1.find('**/joint_nameTag'))
					self.CH_NT_NP.setBillboardAxis()
					self.CH_NT_NP.setZ(7)
					self.CH_TN.setAlign(TextNode.ACenter)
					self.CH_TN.setTextColor(0.9, 0, 0, 1.0)
					self.CH_NT_NP.setScale(1.5)
					self.CH_TN.setFont(L.FONT3)
					self.CH_TN_INT = self.CH_NT_NP.posInterval(0.5,
																Point3(0, 0, 9.5),
																startPos=(0, 0, 7),
																blendType='easeInOut')
					self.CH_TN_INT.start()
					taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_COG, "remove cog damage label")
					self.COG_HEALTH_LBL.setText("Cog health: " + str(self.COG_HEALTH))
			except:
				pass
		try:
			if entry.getIntoNodePath().getName() == 'COG2LEGSCNODE':
				self.COG2_HITS += 1
				self.BOSS_HEALTH -= 5
				try:
					self.CH_NT_NP.remove()
				except:
					pass
				self.BH_TN = TextNode("damage done to BOSS")
				self.BH_TN.setText("-5")
				self.BH_NT_NP = render.attachNewNode(self.BH_TN)
				self.BH_NT_NP.reparentTo(L.COG_2.find('**/joint_nameTag'))
				self.BH_NT_NP.setBillboardAxis()
				self.BH_NT_NP.setZ(4)
				self.BH_TN.setAlign(TextNode.ACenter)
				self.BH_TN.setTextColor(0.9, 0, 0, 1.0)
				self.BH_NT_NP.setScale(1.5)
				self.BH_TN.setFont(L.FONT3)
				self.BH_TN_INT = self.BH_NT_NP.posInterval(0.5,
															Point3(0, 0, 6.5),
															startPos=(0, 0, 4),
															blendType='easeInOut')
				self.BH_TN_INT.start()
				taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_BOSS, "remove BOSS damage label")
				self.BOSS_HEALTH_LBL.setText("Boss health: " + str(self.BOSS_HEALTH))
		except:
			pass

		try:
			self.CCtrajectory.pause()
		except:
			pass
		L.C_CAKE.reparentTo(render)
		L.C_CAKE.setPos(0,0,-250)
		L.C_CAKE.setHpr(0,0,0)

	def CHECK_BCAKE_COL(self, entry):
		L.PIE_SPLAT_SFX.play()
		L.SPLAT.reparentTo(render)
		L.SPLAT.show()
		L.SPLAT.setPos(L.B_CAKE.getPos())
		L.SPLAT.setBillboardAxis()
		L.SPLAT.play("chan")
		taskMgr.doMethodLater(0.5, self.SPLAT_HIDE, "hide splat")
		if entry.getIntoNodePath().getName() == 'COGLEGSCNODE':
			self.COG1_HITS += 1
			try:
				if self.ROUND == 3:
					self.COG_HEALTH -= 15
					try:
						self.CH_NT_NP.remove()
					except:
						pass
					self.CH_TN = TextNode("damage done to cog")
					self.CH_TN.setText("-15")
					self.CH_NT_NP = render.attachNewNode(self.CH_TN)
					self.CH_NT_NP.reparentTo(L.COG_1.find('**/joint_nameTag'))
					self.CH_NT_NP.setBillboardAxis()
					self.CH_NT_NP.setZ(7)
					self.CH_TN.setAlign(TextNode.ACenter)
					self.CH_TN.setTextColor(0.9, 0, 0, 1.0)
					self.CH_NT_NP.setScale(1.5)
					self.CH_TN.setFont(L.FONT3)
					self.CH_TN_INT = self.CH_NT_NP.posInterval(0.5,
																Point3(0, 0, 9.5),
																startPos=(0, 0, 7),
																blendType='easeInOut')
					self.CH_TN_INT.start()
					taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_COG, "remove cog damage label")
					self.COG_HEALTH_LBL.setText("Cog health: " + str(self.COG_HEALTH))
			except:
				pass
		try:
			if entry.getIntoNodePath().getName() == 'COG2LEGSCNODE':
				self.COG2_HITS += 1
				self.BOSS_HEALTH -= 15
				try:
					self.CH_NT_NP.remove()
				except:
					pass
				self.BH_TN = TextNode("damage done to BOSS")
				self.BH_TN.setText("-15")
				self.BH_NT_NP = render.attachNewNode(self.BH_TN)
				self.BH_NT_NP.reparentTo(L.COG_2.find('**/joint_nameTag'))
				self.BH_NT_NP.setBillboardAxis()
				self.BH_NT_NP.setZ(4)
				self.BH_TN.setAlign(TextNode.ACenter)
				self.BH_TN.setTextColor(0.9, 0, 0, 1.0)
				self.BH_NT_NP.setScale(1.5)
				self.BH_TN.setFont(L.FONT3)
				self.BH_TN_INT = self.BH_NT_NP.posInterval(0.5,
															Point3(0, 0, 6.5),
															startPos=(0, 0, 4),
															blendType='easeInOut')
				self.BH_TN_INT.start()
				taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_BOSS, "remove BOSS damage label")
				self.BOSS_HEALTH_LBL.setText("Boss health: " + str(self.BOSS_HEALTH))
		except:
			pass

		self.BCtrajectory.pause()
		L.B_CAKE.reparentTo(render)
		L.B_CAKE.setPos(0,0,-300)
		L.B_CAKE.setHpr(0,0,0)


	def REMOVE_DAMG_LBL_AVA(self, task):
		self.AH_NT_NP.remove()
		return task.done
	def REMOVE_DAMG_LBL_BOSS(self, task):
		self.BH_NT_NP.remove()
		return task.done
	def REMOVE_DAMG_LBL_COG(self, task):
		self.CH_NT_NP.remove()
		return task.done

	def SPLAT_HIDE(self, task):
		L.SPLAT.hide()
		return task.done
	def COG_LAND1(self, task):
		L.COG_1.play("land")
		self.COG_COLL()
		taskMgr.doMethodLater(3, self.COG_STAND, "cog stand 1")
		taskMgr.doMethodLater(3, self.coach_Talk1, "coach talk 1")
		return task.done
	def COG_STAND(self, task):
		L.COG_1.loop("neutral")
		return task.done
	def coach_Talk1(self, task):
		self.ROUND = 1
		print self.ROUND
		self.COACH_WHSP3.remove()
		self.COACH_WHSP3 = OnscreenText(text="COACH: Press control to throw a pie.", scale=0.06, pos=(0.8, -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
		self.COACH_WHSP4 = OnscreenText(text="COACH: This is easy. Hit the Cog in the face!",  scale=0.06, pos=(-0.8, -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
		L.COG_1.loop("neutral")
		base.accept("PavatarSensor-into", self.CHECK_COL_R1)
		return task.done
	def nul_col(self, entry):
		pass
	def CHECK_KNI_COLL(self, entry):
		print entry.getIntoNodePath().getName()
		print "Success"
		if entry.getIntoNodePath().getName() == 'COG2LEGSCNODE':
			print "yes"
			return
		try:
			self.Ktrajectory.finish()
			print "yes2"
		except:
			pass
		L.KNIFE.reparentTo(render)
		L.KNIFE.setPos(0,0,-150)
		L.KNIFE.setHpr(0,0,0)
		print "yes3"
		if entry.getIntoNodePath().getName() == 'LEGSCHIT2':
			print "yes4"
			self.keyMap = {"left":0, "right":0, "forward":0, "backward":0}
			L.RUN_LOOP.stop()
			L.WLK_LOOP.stop()
			base.accept("arrow_left", self.setKey, ["left",0])
			base.accept("arrow_right", self.setKey, ["right",0])
			base.accept("arrow_up", self.setKey, ["forward",0])
			base.accept("arrow_down", self.setKey, ["backward",0])
			base.accept("arrow_left-up", self.setKey, ["left",0])
			base.accept("arrow_right-up", self.setKey, ["right",0])
			base.accept("arrow_up-up", self.setKey, ["forward",0])
			base.accept("arrow_down-up", self.setKey, ["backward",0])
			base.accept("arrow_down-arrow_up", self.setKey, ["backward",0])
			base.accept("arrow_up-arrow_down", self.setKey, ["forward",0])
			base.accept("a", self.setKey, ["left",0])
			base.accept("d", self.setKey, ["right",0])
			base.accept("w", self.setKey, ["forward",0])
			base.accept("s", self.setKey, ["backward",0])
			base.accept("a-up", self.setKey, ["left",0])
			base.accept("d-up", self.setKey, ["right",0])
			base.accept("w-up", self.setKey, ["forward",0])
			base.accept("s-up", self.setKey, ["backward",0])
			base.accept("s-w", self.setKey, ["backward",0])
			base.accept("w-s", self.setKey, ["forward",0])
			base.accept("space", self.nul)
			base.accept("control-up", self.nul)
			base.accept("control", self.nul)
			self.isMoving_forward = False
			self.isMoving_side = False
			L.AVATAR_HEAD.play("slipb")
			L.AVATAR_TORSO.play("slipb")
			L.AVATAR_LEGS.play("slipb")
			try:
				if self.ROUND == 3:
					print "yes5"
					if self.lastWeapon == 'TART':
						self.AVATAR_HEALTH -= 5
						try:
							self.AH_NT_NP.remove()
						except:
							pass
						self.AH_TN = TextNode("damage done to AVA")
						self.AH_TN.setText("-5")
						self.AH_NT_NP = render.attachNewNode(self.AH_TN)
						self.AH_NT_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
						self.AH_NT_NP.setBillboardAxis()
						self.AH_NT_NP.setZ(3.3)
						self.AH_TN.setAlign(TextNode.ACenter)
						self.AH_TN.setTextColor(0.9, 0, 0, 1.0)
						self.AH_NT_NP.setScale(1.5)
						self.AH_TN.setFont(L.FONT3)
						self.AH_TN_INT = self.AH_NT_NP.posInterval(0.5,
																	Point3(0, 0, 5.8),
																	startPos=(0, 0, 3.3),
																	blendType='easeInOut')
						self.AH_TN_INT.start()
						taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_AVA, "remove AVA damage label")
					if self.lastWeapon == 'CCAKE':
						self.AVATAR_HEALTH -= 3
						try:
							self.AH_NT_NP.remove()
						except:
							pass
						self.AH_TN = TextNode("damage done to AVA")
						self.AH_TN.setText("-3")
						self.AH_NT_NP = render.attachNewNode(self.AH_TN)
						self.AH_NT_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
						self.AH_NT_NP.setBillboardAxis()
						self.AH_NT_NP.setZ(3.3)
						self.AH_TN.setAlign(TextNode.ACenter)
						self.AH_TN.setTextColor(0.9, 0, 0, 1.0)
						self.AH_NT_NP.setScale(1.5)
						self.AH_TN.setFont(L.FONT3)
						self.AH_TN_INT = self.AH_NT_NP.posInterval(0.5,
																	Point3(0, 0, 5.8),
																	startPos=(0, 0, 3.3),
																	blendType='easeInOut')
						self.AH_TN_INT.start()
						taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_AVA, "remove AVA damage label")
					if self.lastWeapon == 'BCAKE':
						self.AVATAR_HEALTH -= 10
						try:
							self.AH_NT_NP.remove()
						except:
							pass
						self.AH_TN = TextNode("damage done to AVA")
						self.AH_TN.setText("-10")
						self.AH_NT_NP = render.attachNewNode(self.AH_TN)
						self.AH_NT_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
						self.AH_NT_NP.setBillboardAxis()
						self.AH_NT_NP.setZ(3.3)
						self.AH_TN.setAlign(TextNode.ACenter)
						self.AH_TN.setTextColor(0.9, 0, 0, 1.0)
						self.AH_NT_NP.setScale(1.5)
						self.AH_TN.setFont(L.FONT3)
						self.AH_TN_INT = self.AH_NT_NP.posInterval(0.5,
																	Point3(0, 0, 5.8),
																	startPos=(0, 0, 3.3),
																	blendType='easeInOut')
						self.AH_TN_INT.start()
						taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_AVA, "remove AVA damage label")
					self.AVATAR_HEALTH_LBL.setText("Your health :" + str(self.AVATAR_HEALTH))
			except:
				pass
			taskMgr.doMethodLater(2.5, self.STOP_JUMP, "stop slipb")
	def CHECK_BOSS_HEALTH(self, task):
		if self.BOSS_HEALTH <= 0:
			self.AIBEHAVIORS2.removeAi('pathfollow')
			base.accept('avatarSensor-into', self.nul_col)
			L.COG_2.play("pie")
			taskMgr.doMethodLater(2, self.BOSS_DIE, "BOSS dies")
			return task.done
		return task.cont
	def BOSS_DIE(self, task):
		taskMgr.doMethodLater(1.5, self.DIE_SFX_COG, "cog die sfx")
		taskMgr.doMethodLater(5, self.explode_sfx, "explose sfx")
		L.COG_2.hide()
		L.COG_2_LOSE.reparentTo(render)
		L.COG_2_LOSE.setScale(2.5)
		L.COG_2_LOSE.setPos(L.COG_2.getPos(render))
		L.COG_2_LOSE.setHpr(L.COG_2.getHpr(render))
		L.COG_2_LOSE.show()
		L.TW_HEAD.reparentTo(L.COG_2_LOSE.find('**/joint_head'))
		L.TW_HEAD.show()
		L.COG_2_LOSE.play("lose")
		taskMgr.add(self.CHECK_BOSS_DEATH_FRAME, "check boss death frame")
		return task.done
	def CHECK_COG_LIVES(self, task):
		try:
			if self.COG_LIFE == 'DEAD' and self.BOSS_LIFE == 'DEAD':
				self.AVATAR_WIN()
				return task.done
		except:
			pass
		return task.cont
	def CHECK_BOSS_DEATH_FRAME(self, task):
		if L.COG_2_LOSE.getCurrentFrame("lose") == 150:
			self.BOSS_LIFE = 'DEAD'
			L.COG_2_LOSE.cleanup()
			L.COG_2_LOSE.remove()
			L.COG_2.cleanup()
			L.COG_2.remove()
			return task.done
		return task.cont
	def CHECK_COG_HEALTH(self, task):
		if self.COG_HEALTH <= 0:
			self.AIBEHAVIORS.removeAi('pathfollow')
			base.accept('avatarSensor-into', self.nul_col)
			L.COG_1.play("pie")
			taskMgr.doMethodLater(2, self.COG_DIE, "cog dies")
			return task.done
		return task.cont
	def CHECK_DEATH_FRAME(self, task):
		if L.COG_LOSE.getCurrentFrame("lose") == 150:
			self.COG_LIFE = 'DEAD'
			L.COG_LOSE.cleanup()
			L.COG_LOSE.remove()
			L.COG_1.cleanup()
			L.COG_1.remove()
			return task.done
		return task.cont
	def CHECK_TOTAL_PIE_COUNT(self, task):
		if self.TOTALHITS == 8:
			self.COG_START_HELP()
			return task.done
		return task.cont
	def COG_START_HELP(self):
		self.INCALL = True
		self.AIBEHAVIORS.pauseAi('pathfollow')
		L.COG_1.play("dial", toFrame=55)
		taskMgr.doMethodLater(2.5, self.COG_DIAL_HELP, "cog dials for help")
	def COG_DIAL_HELP(self, task):
		L.COACH_DIAL.play()
		self.COACH_WHSP_BOSS = OnscreenText(text="COACH: He's calling in the boss! Watch out!", scale=0.06, pos=(0 -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
		taskMgr.doMethodLater(4, self.BOSS_WHSP_REMOVE, "remove boss whisper")
		L.COG_1.loop("dial", fromFrame=56, toFrame=90)
		L.MC_HELP1.play()
		taskMgr.doMethodLater(10, self.COG_RESUME_WANDER, "cog resumes wander")
		taskMgr.doMethodLater(9.9, self.LEAVE_DIAL, "leave dial")
		taskMgr.doMethodLater(15, self.COG_SPAWN2, "cog 2 spawns")
		taskMgr.doMethodLater(10, self.CHECK_PIE_COUNT, "check pie count")
		return task.done

	def BOSS_WHSP_REMOVE(self, task):
		self.COACH_WHSP_BOSS.remove()
		return task.done
	def COG_SPAWN2(self, task):
		L.COG_2.setScale(2.5)
		self.KNI_COLL()

		self.COG2_TN = TextNode("Cog 2 nametag")
		self.COG2_TN.setText("BossCog\nUnknown\nLevel 70")
		self.COG2_NT_NP = render.attachNewNode(self.COG2_TN)
		self.COG2_NT_NP.reparentTo(L.COG_2.find('**/joint_nameTag'))
		self.COG2_NT_NP.setBillboardAxis()
		self.COG2_NT_NP.setZ(6)
		self.COG2_TN.setAlign(TextNode.ACenter)
		self.COG2_TN.setCardColor(0.8, 0.8, 0.8, 0.5)
		self.COG2_TN.setCardAsMargin(0,0,0,-0.2)
		self.COG2_TN.setCardDecal(True)
		self.COG2_TN.setTextColor(0,0,0,1.0)
		self.COG2_NT_NP.setScale(0.2)
		self.COG2_TN.setFont(L.FONT2)

		L.COG_2.reparentTo(render)
		L.COG_2.setPos(75.84, 54.42, 0.00)
		L.COG_2.setH(126.87)

		L.PROP_IDLE.play()
		taskMgr.doMethodLater(1.5, self.PROP_IN_SFX, "prop in sfx")
		L.COG_2.pose("land", 1)
		L.PROP.reparentTo(L.COG_2.find('**/joint_head'))
		L.PROP.loop("spin", fromFrame=0, toFrame=3)
		taskMgr.doMethodLater(5.5, self.PROP_IN, "propeller in")
		L.COG_2_FLYDOWN_INTERVAL = L.COG_2.posInterval(4,
													Point3(75.84, 54.42, 0.00),
													startPos=(75.84, 54.42, 15.00))
		L.COG_2_FLYDOWN_INTERVAL.start()
		base.accept('KavatarSensor-into', self.CHECK_KNI_COLL)
		self.BOSS_HEALTH = 550
		self.BOSS_HEALTH_LBL = OnscreenText(text="Boss health: " + str(self.BOSS_HEALTH),  scale=0.06, pos=(0, 0, 0), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6), mayChange=True)
		taskMgr.doMethodLater(0.5, self.BOSS_HEALTH_MOVE, "boss health lbl moves")
		taskMgr.doMethodLater(4, self.COG_LAND2, "cog land 2")
		taskMgr.add(self.CHECK_BOSS_HEALTH, "check boss health")
		return task.done
	def BOSS_HEALTH_MOVE(self, task):
		self.BOSS_HEALTH_LBL_INT = self.BOSS_HEALTH_LBL.posInterval(1,
																	Point3(0.0, -0.9, -0.9),
																	startPos=(0,0,0),
																	blendType='easeInOut')
		self.BOSS_HEALTH_LBL_INT.start()
		return task.done
	def COG_LAND2(self, task):
		L.COG_2.play("land")
		self.COG2_COLL()
		taskMgr.doMethodLater(3, self.COG_INITAI2, "cog wander 2")
		return task.done
	def COG_INITAI2(self, task):
		L.COG_2.loop("walk")
		self.AICOG2 = AICharacter("cog2", L.COG_2, -90, 10, -5)
		self.AIWORLD.addAiChar(self.AICOG2)
		self.AIBEHAVIORS2 = self.AICOG2.getAiBehaviors()
		self.AIBEHAVIORS2.pathFollow(5)
		self.AIBEHAVIORS2.addToPath(L.COG_CP3_NP.getPos())
		self.AIBEHAVIORS2.addToPath(L.COG_CP5_NP.getPos())
		self.AIBEHAVIORS2.addToPath(L.COG_CP1_NP.getPos())
		self.AIBEHAVIORS2.addToPath(L.COG_CP2_NP.getPos())
		self.AIBEHAVIORS2.addToPath(L.COG_CP4_NP.getPos())
		self.AIBEHAVIORS2.addToPath(L.COG_CP7_NP.getPos())
		self.AIBEHAVIORS2.addToPath(L.COG_CP6_NP.getPos())
		self.AIBEHAVIORS2.addToPath(L.COG_CP8_NP.getPos())
		self.AIBEHAVIORS2.startFollow()
		taskMgr.add(self.CHECKCOGPATHSTAT2, "check cog path status 2")
		return task.done
	def COG_STAND2(self, task):
		L.COG_2.loop("neutral")
		return task.done
	def LEAVE_DIAL(self, task):
		self.INCALL = False
		return task.done
	def AVATAR_WIN(self):
		self.COACH_WHSP8.remove()
		self.COACH_WHSP9 = OnscreenText(text="COACH: Yay, you're ready for real Cog fights! Bye!", scale=0.06, pos=(0, -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
		self.keyMap = {"left":0, "right":0, "forward":0, "backward":0}
		L.RUN_LOOP.stop()
		L.WLK_LOOP.stop()
		base.accept("arrow_left", self.setKey, ["left",0])
		base.accept("arrow_right", self.setKey, ["right",0])
		base.accept("arrow_up", self.setKey, ["forward",0])
		base.accept("arrow_down", self.setKey, ["backward",0])
		base.accept("arrow_left-up", self.setKey, ["left",0])
		base.accept("arrow_right-up", self.setKey, ["right",0])
		base.accept("arrow_up-up", self.setKey, ["forward",0])
		base.accept("arrow_down-up", self.setKey, ["backward",0])
		base.accept("arrow_down-arrow_up", self.setKey, ["backward",0])
		base.accept("arrow_up-arrow_down", self.setKey, ["forward",0])
		base.accept("a", self.setKey, ["left",0])
		base.accept("d", self.setKey, ["right",0])
		base.accept("w", self.setKey, ["forward",0])
		base.accept("s", self.setKey, ["backward",0])
		base.accept("a-up", self.setKey, ["left",0])
		base.accept("d-up", self.setKey, ["right",0])
		base.accept("w-up", self.setKey, ["forward",0])
		base.accept("s-up", self.setKey, ["backward",0])
		base.accept("s-w", self.setKey, ["backward",0])
		base.accept("w-s", self.setKey, ["forward",0])
		base.accept("space", self.nul)
		base.accept("control-up", self.nul)
		base.accept("control", self.nul)
		self.isMoving_forward = False
		self.isMoving_side = False
		L.AVATAR_HEAD.play("vd")
		L.AVATAR_TORSO.play("vd")
		L.AVATAR_LEGS.play("vd")
		L.VD_SFX.play()
		taskMgr.doMethodLater(6, self.QUIT, "quit game")
	def DIE_SFX_COG(self, task):
		L.COG_DIE_SFX.play()
		return task.done
	def COG_DIE(self, task):
		taskMgr.doMethodLater(1.5, self.DIE_SFX_COG, "cog die sfx")
		taskMgr.doMethodLater(5, self.explode_sfx, "explose sfx")
		L.COG_1.hide()
		L.COG_LOSE.reparentTo(render)
		L.COG_LOSE.setPos(L.COG_1.getPos(render))
		L.COG_LOSE.setHpr(L.COG_1.getHpr(render))
		L.COG_LOSE.show()
		self.MS.reparentTo(L.COG_LOSE.find('**/joint_head'))
		self.MS.show()
		L.COG_LOSE.play("lose")
		taskMgr.add(self.CHECK_DEATH_FRAME, "check death frame")
		return task.done
	def explode_sfx(self, task):
		L.JUMP_END_SFX.play()
		return task.done
	def CHECK_AVA_HEALTH(self, task):
		if self.AVATAR_HEALTH <= 0:
			self.AVATAR_DIE()
			return task.done
		return task.cont

	def AVATAR_DIE(self):
		self.keyMap = {"left":0, "right":0, "forward":0, "backward":0}
		L.RUN_LOOP.stop()
		L.WLK_LOOP.stop()
		base.accept("arrow_left", self.setKey, ["left",0])
		base.accept("arrow_right", self.setKey, ["right",0])
		base.accept("arrow_up", self.setKey, ["forward",0])
		base.accept("arrow_down", self.setKey, ["backward",0])
		base.accept("arrow_left-up", self.setKey, ["left",0])
		base.accept("arrow_right-up", self.setKey, ["right",0])
		base.accept("arrow_up-up", self.setKey, ["forward",0])
		base.accept("arrow_down-up", self.setKey, ["backward",0])
		base.accept("arrow_down-arrow_up", self.setKey, ["backward",0])
		base.accept("arrow_up-arrow_down", self.setKey, ["forward",0])
		base.accept("a", self.setKey, ["left",0])
		base.accept("d", self.setKey, ["right",0])
		base.accept("w", self.setKey, ["forward",0])
		base.accept("s", self.setKey, ["backward",0])
		base.accept("a-up", self.setKey, ["left",0])
		base.accept("d-up", self.setKey, ["right",0])
		base.accept("w-up", self.setKey, ["forward",0])
		base.accept("s-up", self.setKey, ["backward",0])
		base.accept("s-w", self.setKey, ["backward",0])
		base.accept("w-s", self.setKey, ["forward",0])
		base.accept("space", self.nul)
		base.accept("control-up", self.nul)
		base.accept("control", self.nul)
		self.isMoving_forward = False
		self.isMoving_side = False
		L.AVATAR_HEAD.play("lose", fromFrame=0, toFrame=87)
		L.AVATAR_TORSO.play("lose", fromFrame=0, toFrame=87)
		L.AVATAR_LEGS.play("lose", fromFrame=0, toFrame=87)
		taskMgr.doMethodLater(1.5, self.PLAY_LOSE_SFX, "play loser sfx")
		taskMgr.doMethodLater(5, self.QUIT, "quit")
	def QUIT(self, task):
		sys.exit(0)
		return task.done
	def ASK_TO_RESTART(self, task):
		self.RESTART_LBL1 = OnscreenText(text="You failed!", scale=0.08, fg=(1,1,1,1), pos=(0, 0.05, 0))
		self.RESTART_LBL2 = OnscreenText(text="Press R to restart.", scale=0.08, fg=(1,1,1,1), pos=(0, -0.05, 0))
		base.accept('R', self.RESTART_GAME)
		return task.done
	def RESTART_GAME(self):
		try:
			L.COG_1.remove()
		except:
			pass
		try:
			L.COG_1_LOSE.remove()
		except:
			pass
		try:
			L.COG_2.remove()
		except:
			pass
		try:
			L.COG_2_LOSE.remove()
		except:
			pass
		try:
			self.CCAKE_ICON.remove()
			self.TART_ICON.remove()
			self.BCAKE_ICON.remove()
		except:
			pass
		self.RESTART_LBL1.remove()
		self.RESTART_LBL2.remove()
		self.COG_SPAWN1()
	def PLAY_LOSE_SFX(self, task):
		L.LOSE_SFX.play()
		return task.done
	def CHECK_COL_R1(self, entry):
		L.PIE_SPLAT_SFX.play()
		L.SPLAT.reparentTo(render)
		L.SPLAT.show()
		L.SPLAT.setPos(L.PIE.getPos())
		L.SPLAT.setBillboardAxis()
		L.SPLAT.play("chan")
		taskMgr.doMethodLater(0.5, self.SPLAT_HIDE, "hide splat")
		self.trajectory.pause()
		L.PIE.hide()
		print entry.getIntoNodePath().getName()
		if entry.getIntoNodePath().getName() == 'COGLEGSCNODE':
			base.accept('PavatarSensor-into', self.nul_col)
			self.COACH_WHSP4.remove()
			self.COACH_WHSP3.remove()
			L.COG_1.play("pie")
			print self.ROUND
			self.COACH_WHSP5 = OnscreenText(text="COACH: Good! Try hitting the Cog while he's moving.",  scale=0.06, pos=(0.8, -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
			taskMgr.doMethodLater(2, self.COG_STAND, "cog stand 2")
			taskMgr.doMethodLater(2, self.INIT_ROUND2, "init round 2")
			taskMgr.doMethodLater(5, self.COG_INITAI1, "cog init ai 1")
	def INIT_ROUND2(self, task):
		self.COG_TN.setText("Mover &\nShaker\nSellbot\nLevel 7")
		self.ROUND = 2
		return task.done
	def setWeapon_CCAKE(self):
		self.weapon = 'CCAKE'
		self.CCAKE_ICON.remove()
		self.CCAKE_ICON = OnscreenImage(image="phase_3.5/maps/cupcake_selected.png")
		self.CCAKE_ICON.setTransparency(True)
		self.CCAKE_ICON.setX(1)
		self.CCAKE_ICON.setZ(0.5)
		self.CCAKE_ICON.setScale(0.2)

		self.TART_ICON.remove()
		self.TART_ICON = OnscreenImage(image="phase_3.5/maps/tart_idle.png")
		self.TART_ICON.setTransparency(True)
		self.TART_ICON.setX(1)
		self.TART_ICON.setZ(0.1)
		self.TART_ICON.setScale(0.2)

		self.BCAKE_ICON.remove()
		self.BCAKE_ICON = OnscreenImage(image="phase_3.5/maps/b_cake_idle.png")
		self.BCAKE_ICON.setTransparency(True)
		self.BCAKE_ICON.setX(1)
		self.BCAKE_ICON.setZ(-0.3)
		self.BCAKE_ICON.setScale(0.2)
		base.accept('wheel_up', self.setWeapon_BCAKE)
		base.accept('wheel_down', self.setWeapon_TART)
		L.WEAPON_SELECT.play()

	## WHY ARE SO MANY FILES MISSING IN setWeapon_TART?!
	def setWeapon_TART(self):
		self.weapon = 'TART'

		## ALL OF THIS DOESN'T WORK!
		## WHYYYYY
		#self.CCAKE_ICON.remove()
		#self.CCAKE_ICON = OnscreenImage(image="phase_3.5/maps/cupcake_idle.png")
		#self.CCAKE_ICON.setTransparency(True)
		#self.CCAKE_ICON.setX(1)
		#self.CCAKE_ICON.setZ(0.5)
		#self.CCAKE_ICON.setScale(0.2)

		#self.TART_ICON.remove()
		#self.TART_ICON = OnscreenImage(image="phase_3.5/maps/tart_selected.png")
		#self.TART_ICON.setTransparency(True)
		#self.TART_ICON.setX(1)
		#self.TART_ICON.setZ(0.1)
		#self.TART_ICON.setScale(0.2)

		#self.BCAKE_ICON.remove()
		#self.BCAKE_ICON = OnscreenImage(image="phase_3.5/maps/b_cake_idle.png")
		#self.BCAKE_ICON.setTransparency(True)
		#self.BCAKE_ICON.setX(1)
		#self.BCAKE_ICON.setZ(-0.3)
		#self.BCAKE_ICON.setScale(0.2)
		base.accept('wheel_up', self.setWeapon_CCAKE)
		base.accept('wheel_down', self.setWeapon_BCAKE)
		L.WEAPON_SELECT.play()
	def setWeapon_BCAKE(self):
		self.weapon = 'BCAKE'
		#self.CCAKE_ICON.remove()
		#self.CCAKE_ICON = OnscreenImage(image="phase_3.5/maps/cupcake_idle.png")
		#self.CCAKE_ICON.setTransparency(True)
		#self.CCAKE_ICON.setX(1)
		#self.CCAKE_ICON.setZ(0.5)
		#self.CCAKE_ICON.setScale(0.2)

		#self.TART_ICON.remove()
		#self.TART_ICON = OnscreenImage(image="phase_3.5/maps/tart_idle.png")
		#self.TART_ICON.setTransparency(True)
		#self.TART_ICON.setX(1)
		#self.TART_ICON.setZ(0.1)
		#self.TART_ICON.setScale(0.2)

		#self.BCAKE_ICON.remove()
		#self.BCAKE_ICON = OnscreenImage(image="phase_3.5/maps/b_cake_selected.png")
		#self.BCAKE_ICON.setTransparency(True)
		#self.BCAKE_ICON.setX(1)
		#self.BCAKE_ICON.setZ(-0.3)
		#self.BCAKE_ICON.setScale(0.2)
		base.accept('wheel_up', self.setWeapon_TART)
		base.accept('wheel_down', self.setWeapon_CCAKE)
		L.WEAPON_SELECT.play()

	def CHECK_ACTIVE_WEAPON_UP(self):
		if self.weapon == 'CCAKE':
			self.C_CAKE_THROW()
		if self.weapon == 'TART':
			self.PIE_THROW()
		if self.weapon == 'BCAKE':
			self.B_CAKE_THROW()
	def CHECK_ACTIVE_WEAPON_DN(self):
		if self.weapon == 'CCAKE':
			self.C_CAKE_START()
		if self.weapon == 'TART':
			self.PIE_START()
		if self.weapon == 'BCAKE':
			self.B_CAKE_START()

    ## SO MANY MISSING IMAGES...
	def COG_INITAI1(self, task):
		base.accept('PavatarSensor-into', self.CHECK_PIE_COL)
		base.accept('CCavatarSensor-into', self.CHECK_CCAKE_COL)
		base.accept('BavatarSensor-into', self.CHECK_BCAKE_COL)
		base.accept('TavatarSensor-into', self.CHECK_TIE_COL)
		self.weapon = 'TART'

		## ALL OF THIS DOESN'T WORK!
		#self.CCAKE_ICON = OnscreenImage(image="phase_3.5/maps/cupcake_idle.png")
		#self.CCAKE_ICON.setTransparency(True)
		#self.CCAKE_ICON.setX(1)
		#self.CCAKE_ICON.setZ(0.5)
		#self.CCAKE_ICON.setScale(0.2)
		#self.TART_ICON = OnscreenImage(image="phase_3.5/maps/tart_selected.png")
		#self.TART_ICON.setTransparency(True)
		#self.TART_ICON.setX(1)
		#self.TART_ICON.setZ(0.1)
		#self.TART_ICON.setScale(0.2)
		#self.BCAKE_ICON = OnscreenImage(image="phase_3.5/maps/b_cake_idle.png")
		#self.BCAKE_ICON.setTransparency(True)
		#self.BCAKE_ICON.setX(1)
		#self.BCAKE_ICON.setZ(-0.3)
		#self.BCAKE_ICON.setScale(0.2)
		base.accept('control-up', self.CHECK_ACTIVE_WEAPON_UP)
		base.accept('control', self.CHECK_ACTIVE_WEAPON_DN)
		base.accept('wheel_up', self.setWeapon_CCAKE)
		base.accept('wheel_down', self.setWeapon_BCAKE)
		base.accept('1', self.setWeapon_CCAKE)
		base.accept('2', self.setWeapon_TART)
		base.accept('3', self.setWeapon_BCAKE)
		self.TIE_COL()
		taskMgr.add(self.CHECK_PIE_COUNT, "check pie count")
		taskMgr.add(self.RESTART_PIECOUNT, "restart pie count")
		self.COACH_WHSP5.remove()
		self.AIWORLD = AIWorld(render)
		self.AICOG = AICharacter("cog", L.COG_1, -75, 10, -5)
		self.AIWORLD.addAiChar(self.AICOG)
		self.AIBEHAVIORS = self.AICOG.getAiBehaviors()
		if self.ROUND == 2:
			self.COACH_WHSP6 = OnscreenText(text="COACH: If you touch the Cog, jump before he hits the ground!",  scale=0.06, pos=(0.8, -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
			self.COACH_WHSP7 = OnscreenText(text="COACH: Press space to jump.",  scale=0.06, pos=(-0.8, -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
			self.COACH_WHSP7_2 = OnscreenText(text="COACH: Don't throw pies too fast, he will try to attack you!",  scale=0.06, pos=(0.1, -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
			self.AIBEHAVIORS.pathFollow(5)
			self.AIBEHAVIORS.addToPath(L.COG_CP1_NP.getPos())
			self.AIBEHAVIORS.addToPath(L.COG_CP2_NP.getPos())
		taskMgr.add(self.COG_WANDER1, "cog wander 1")
		return task.done
	def PIE_THROW(self):
		L.AVATAR_HEAD.play("pie", fromFrame=45, toFrame=90)
		L.AVATAR_TORSO.play("pie", fromFrame=45, toFrame=90)
		L.AVATAR_LEGS.play("pie", fromFrame=45, toFrame=90)
		taskMgr.doMethodLater(0.7, self.PIE_RELEASE, "pie release")
	def C_CAKE_THROW(self):
		L.AVATAR_HEAD.play("pie", fromFrame=45, toFrame=90)
		L.AVATAR_TORSO.play("pie", fromFrame=45, toFrame=90)
		L.AVATAR_LEGS.play("pie", fromFrame=45, toFrame=90)
		taskMgr.doMethodLater(0.7, self.C_CAKE_RELEASE, "pie release")

	def B_CAKE_THROW(self):
		L.AVATAR_HEAD.play("pie", fromFrame=45, toFrame=90)
		L.AVATAR_TORSO.play("pie", fromFrame=45, toFrame=90)
		L.AVATAR_LEGS.play("pie", fromFrame=45, toFrame=90)
		taskMgr.doMethodLater(0.7, self.B_CAKE_RELEASE, "pie release")
	def PIE_RELEASE(self, task):
		L.PIE_THROW_SFX.play()
		self.PIE_NP = NodePath("PIEPATH")
		self.PIE_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
		self.PIE_NP.setPos(0, 50, 0)
		self.PIE_NP.setHpr(90, -90, 90)

		L.PIE.reparentTo(render)

		self.trajectory = ProjectileInterval(L.PIE,
									startPos = (L.AVATAR_LEGS.getX(), L.AVATAR_LEGS.getY(), L.AVATAR_LEGS.getZ() +4),
									endPos = self.PIE_NP.getPos(render),
									gravityMult = 0.7, duration = 1)
		L.PIE.setHpr(self.PIE_NP.getHpr(render))
		self.trajectory.start()
	def C_CAKE_RELEASE(self, task):
		L.PIE_THROW_SFX.play()
		self.CCAKE_NP = NodePath("CCAKEPATH")
		self.CCAKE_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
		self.CCAKE_NP.setPos(0, 50, 0)
		self.CCAKE_NP.setHpr(90, -90, 90)

		L.C_CAKE.reparentTo(render)

		self.CCtrajectory = ProjectileInterval(L.C_CAKE,
									startPos = (L.AVATAR_LEGS.getX(), L.AVATAR_LEGS.getY(), L.AVATAR_LEGS.getZ() +4),
									endPos = self.CCAKE_NP.getPos(render),
									gravityMult = 0.7, duration = 1)
		L.C_CAKE.setHpr(self.CCAKE_NP.getHpr(render))
		self.CCtrajectory.start()
	def B_CAKE_RELEASE(self, task):
		L.PIE_THROW_SFX.play()
		self.BC_NP = NodePath("BCPATH")
		self.BC_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
		self.BC_NP.setPos(0, 50, 0)
		self.BC_NP.setHpr(90, -90, 90)

		L.B_CAKE.reparentTo(render)

		self.BCtrajectory = ProjectileInterval(L.B_CAKE,
									startPos = (L.AVATAR_LEGS.getX(), L.AVATAR_LEGS.getY(), L.AVATAR_LEGS.getZ() +4),
									endPos = self.BC_NP.getPos(render),
									gravityMult = 0.7, duration = 1)
		L.B_CAKE.setHpr(self.BC_NP.getHpr(render))
		self.BCtrajectory.start()
	def COG_COLL(self):
		self.COLEGSNP = NodePath('COGlegsnp')
		self.COLEGSNP.reparentTo(L.COG_1)
		self.COLEGSNP.setZ(5)
		self.COavatarCollider = L.COG_1.attachNewNode(CollisionNode('COGLEGSCNODE'))
		self.COavatarCollider.node().addSolid(CollisionSphere(0,0,0,2.5))
		self.COavatarCollider.setSz(3)
		self.COavatarCollider.node().setFromCollideMask(BitMask32.allOff())
		self.COavatarCollider.node().setIntoCollideMask(self.WALL_MASK)
		self.COavatarSensor = L.COG_1.attachNewNode(CollisionNode('COGavatarSensor'))
		self.COavatarSensor.node().addSolid(CollisionSphere(0,0,0,1.2))
		self.COavatarSensor.node().setFromCollideMask(self.WALL_MASK|self.TRIGGER_MASK)
		self.COavatarSensor.node().setIntoCollideMask(BitMask32.allOff())
		self.COraygeometry = CollisionRay(0, 0, 2, 0, 0, -1)
		self.COavatarRay = self.COLEGSNP.attachNewNode(CollisionNode('COGavatarRay'))
		self.COavatarRay.node().addSolid(self.raygeometry)
		self.COavatarRay.node().setFromCollideMask(self.FLOOR_MASK)
		self.COavatarRay.node().setIntoCollideMask(BitMask32.allOff())

		self.groundHandler.addCollider(self.COavatarRay, L.COG_1)

		self.wallHandler.addCollider(self.COavatarCollider, L.COG_1)

		base.cTrav.addCollider(self.COavatarRay, self.groundHandler)
		base.cTrav.addCollider(self.COavatarCollider, self.wallHandler)
		base.cTrav.addCollider(self.COavatarSensor, self.colEV)
	def COG2_COLL(self):
		self.CO2LEGSNP = NodePath('COG2legsnp')
		self.CO2LEGSNP.reparentTo(L.COG_2)
		self.CO2LEGSNP.setZ(5)
		self.CO2avatarCollider = L.COG_2.attachNewNode(CollisionNode('COG2LEGSCNODE'))
		self.CO2avatarCollider.node().addSolid(CollisionSphere(0,0,0,2.5))
		self.CO2avatarCollider.setSz(3)
		self.CO2avatarCollider.node().setFromCollideMask(BitMask32.allOff())
		self.CO2avatarCollider.node().setIntoCollideMask(self.WALL_MASK)
		self.CO2avatarSensor = L.COG_2.attachNewNode(CollisionNode('COG2avatarSensor'))
		self.CO2avatarSensor.node().addSolid(CollisionSphere(0,0,0,1.2))
		self.CO2avatarSensor.node().setFromCollideMask(self.WALL_MASK|self.TRIGGER_MASK)
		self.CO2avatarSensor.node().setIntoCollideMask(BitMask32.allOff())
		self.CO2raygeometry = CollisionRay(0, 0, 2, 0, 0, -1)
		self.CO2avatarRay = self.CO2LEGSNP.attachNewNode(CollisionNode('COG2avatarRay'))
		self.CO2avatarRay.node().addSolid(self.raygeometry)
		self.CO2avatarRay.node().setFromCollideMask(self.FLOOR_MASK)
		self.CO2avatarRay.node().setIntoCollideMask(BitMask32.allOff())

		self.groundHandler.addCollider(self.CO2avatarRay, L.COG_2)

		self.wallHandler.addCollider(self.CO2avatarCollider, L.COG_2)

		base.cTrav.addCollider(self.CO2avatarRay, self.groundHandler)
		base.cTrav.addCollider(self.CO2avatarCollider, self.wallHandler)
		base.cTrav.addCollider(self.CO2avatarSensor, self.colEV)
	def COG_WANDER1(self, task):
		if self.ROUND == 3:
			self.AIBEHAVIORS.removeAi('pathfollow')
			self.AIBEHAVIORS.pathFollow(5)
			self.AIBEHAVIORS.addToPath(L.COG_CP1_NP.getPos())
			self.AIBEHAVIORS.addToPath(L.COG_CP2_NP.getPos())
			self.AIBEHAVIORS.addToPath(L.COG_CP3_NP.getPos())
			self.AIBEHAVIORS.addToPath(L.COG_CP4_NP.getPos())
			self.AIBEHAVIORS.addToPath(L.COG_CP5_NP.getPos())
			self.AIBEHAVIORS.addToPath(L.COG_CP6_NP.getPos())
			self.AIBEHAVIORS.addToPath(L.COG_CP7_NP.getPos())
			self.AIBEHAVIORS.addToPath(L.COG_CP8_NP.getPos())
		self.AIBEHAVIORS.startFollow()

		L.COG_1.loop("walk")
		if self.ROUND == 1 or 2:
			taskMgr.add(self.AICOGUPDATE, "ai cog update")
			taskMgr.add(self.CHECKCOGPATHSTAT, "check cog path status")
			base.accept('avatarSensor-into', self.CHECK_COG_COL)
		return task.done
	def CHECK_COG_COL(self, entry):
		print entry.getIntoNodePath().getName()
		if entry.getIntoNodePath().getName() == 'COGLEGSCNODE':
			L.COG_GRUNT.play()
			taskMgr.doMethodLater(1, self.COG_JUMP, "cog jumps")
		if entry.getIntoNodePath().getName() == 'COG2LEGSCNODE':
			L.BOSS_GRUNT.setVolume(6)
			L.BOSS_GRUNT.play()
			self.AVA_BOSS_FALL()

	def AVA_BOSS_FALL(self):
		self.keyMap = {"left":0, "right":0, "forward":0, "backward":0}
		L.RUN_LOOP.stop()
		L.WLK_LOOP.stop()
		base.accept("arrow_left", self.setKey, ["left",0])
		base.accept("arrow_right", self.setKey, ["right",0])
		base.accept("arrow_up", self.setKey, ["forward",0])
		base.accept("arrow_down", self.setKey, ["backward",0])
		base.accept("arrow_left-up", self.setKey, ["left",0])
		base.accept("arrow_right-up", self.setKey, ["right",0])
		base.accept("arrow_up-up", self.setKey, ["forward",0])
		base.accept("arrow_down-up", self.setKey, ["backward",0])
		base.accept("arrow_down-arrow_up", self.setKey, ["backward",0])
		base.accept("arrow_up-arrow_down", self.setKey, ["forward",0])
		base.accept("a", self.setKey, ["left",0])
		base.accept("d", self.setKey, ["right",0])
		base.accept("w", self.setKey, ["forward",0])
		base.accept("s", self.setKey, ["backward",0])
		base.accept("a-up", self.setKey, ["left",0])
		base.accept("d-up", self.setKey, ["right",0])
		base.accept("w-up", self.setKey, ["forward",0])
		base.accept("s-up", self.setKey, ["backward",0])
		base.accept("s-w", self.setKey, ["backward",0])
		base.accept("w-s", self.setKey, ["forward",0])
		base.accept("space", self.nul)
		base.accept("control-up", self.nul)
		base.accept("control", self.nul)
		self.isMoving_forward = False
		self.isMoving_side = False
		L.AVATAR_HEAD.play("slipb")
		L.AVATAR_TORSO.play("slipb")
		L.AVATAR_LEGS.play("slipb")
		try:
			if self.ROUND == 3:
				self.AVATAR_HEALTH -= 3
				try:
					self.AH_NT_NP.remove()
				except:
					pass
				self.AH_TN = TextNode("damage done to AVA")
				self.AH_TN.setText("-3")
				self.AH_NT_NP = render.attachNewNode(self.AH_TN)
				self.AH_NT_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
				self.AH_NT_NP.setBillboardAxis()
				self.AH_NT_NP.setZ(3.3)
				self.AH_TN.setAlign(TextNode.ACenter)
				self.AH_TN.setTextColor(0.9, 0, 0, 1.0)
				self.AH_NT_NP.setScale(1.5)
				self.AH_TN.setFont(L.FONT3)
				self.AH_TN_INT = self.AH_NT_NP.posInterval(0.5,
															Point3(0, 0, 5.8),
															startPos=(0, 0, 3.3),
															blendType='easeInOut')
				self.AH_TN_INT.start()
				taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_AVA, "remove AVA damage label")
				self.AVATAR_HEALTH_LBL.setText("Your health: " + str(self.AVATAR_HEALTH))
		except:
			pass
		taskMgr.doMethodLater(1, self.STOP_JUMP, "stop fall")

	def COG_JUMP(self, task):
		L.JUMP_START_SFX.play()
		try:
			self.AIBEHAVIORS.pauseAi('pathfollow')
		except:
			pass
		L.COG_1.play("jump")
		taskMgr.doMethodLater(1.4, self.CHECK_JUMP_DAMAGE, "check cog jump damage")
		taskMgr.doMethodLater(1.8, self.COG_RESUME_WANDER, "cog resumes wander")
		return task.done
	def CHECK_PIE_COUNT(self, task):
		if self.ROUND == 3:
			if self.COG1_HITS == 4:
				try:
					if self.INCALL == True:
						return task.done
				except:
					pass
				L.COG_STATEMENT.play()
				self.COG_START_TIE()
				self.COG1_HITS = 0
				return task.cont
			if self.COG2_HITS == 2:
				L.BOSS_STATEMENT.setVolume(6)
				L.BOSS_STATEMENT.play()
				self.BOSS_START_KNIFE()
				self.COG2_HITS = 0
				return task.cont
		if self.COG1_HITS == 7:
			L.COG_STATEMENT.play()
			self.COG_START_TIE()
			self.COG1_HITS = 0
		return task.cont
	def BOSS_START_KNIFE(self):
		self.AIBEHAVIORS2.pauseAi('pathfollow')
		L.COG_2.setH(L.AVATAR_LEGS.getH() - 180)
		L.COG_2.play("knife")
		taskMgr.doMethodLater(0.5, self.BOSS_RELEASE_KNIFE, "boss releases knife")
		taskMgr.doMethodLater(2, self.BOSS_RESUME_WANDER, "boss resume wander")
	def BOSS_RESUME_WANDER(self, task):
		self.AIBEHAVIORS2.resumeAi('pathfollow')
		L.COG_2.loop("walk")
		return task.done
	def BOSS_RELEASE_KNIFE(self, task):
		self.KNI_NP = NodePath("KNIFEPATH")
		self.KNI_NP.reparentTo(L.COG_2.find('**/joint_nameTag'))
		self.KNI_NP.setPos(0, 50, 0)

		L.KNIFE.show()

		L.KNIFE.reparentTo(render)
		L.KNIFE.setH(self.KNI_NP.getH(render))

		self.Ktrajectory = L.KNIFE.posInterval(0.8,
									Point3(self.KNI_NP.getPos(render)),
									startPos=(L.COG_2.getX(), L.COG_2.getY(), L.COG_2.getZ() + 3))
		self.Ktrajectory.start()
		return task.done
	def COG_POS(self, task):
		print L.COG_1.getPos(render)
		return task.again
	def CHECK_TIE_COL(self, entry):
		print entry.getIntoNodePath().getName()
		if entry.getIntoNodePath().getName() == 'COGLEGSCNODE':
			return
		try:
			self.Ttrajectory.finish()
		except:
			pass
		L.TIE.reparentTo(render)
		L.TIE.setPos(0,0,-200)
		L.TIE.setHpr(0,0,0)
		if entry.getIntoNodePath().getName() == 'LEGSCHIT':
			self.keyMap = {"left":0, "right":0, "forward":0, "backward":0}
			L.RUN_LOOP.stop()
			L.WLK_LOOP.stop()
			base.accept("arrow_left", self.setKey, ["left",0])
			base.accept("arrow_right", self.setKey, ["right",0])
			base.accept("arrow_up", self.setKey, ["forward",0])
			base.accept("arrow_down", self.setKey, ["backward",0])
			base.accept("arrow_left-up", self.setKey, ["left",0])
			base.accept("arrow_right-up", self.setKey, ["right",0])
			base.accept("arrow_up-up", self.setKey, ["forward",0])
			base.accept("arrow_down-up", self.setKey, ["backward",0])
			base.accept("arrow_down-arrow_up", self.setKey, ["backward",0])
			base.accept("arrow_up-arrow_down", self.setKey, ["forward",0])
			base.accept("a", self.setKey, ["left",0])
			base.accept("d", self.setKey, ["right",0])
			base.accept("w", self.setKey, ["forward",0])
			base.accept("s", self.setKey, ["backward",0])
			base.accept("a-up", self.setKey, ["left",0])
			base.accept("d-up", self.setKey, ["right",0])
			base.accept("w-up", self.setKey, ["forward",0])
			base.accept("s-up", self.setKey, ["backward",0])
			base.accept("s-w", self.setKey, ["backward",0])
			base.accept("w-s", self.setKey, ["forward",0])
			base.accept("space", self.nul)
			base.accept("control-up", self.nul)
			base.accept("control", self.nul)
			self.isMoving_forward = False
			self.isMoving_side = False
			L.AVATAR_HEAD.play("slipb")
			L.AVATAR_TORSO.play("slipb")
			L.AVATAR_LEGS.play("slipb")
			try:
				if self.ROUND == 3:
					if self.lastWeapon == 'TART':
						self.AVATAR_HEALTH -= 3
						try:
							self.AH_NT_NP.remove()
						except:
							pass
						self.AH_TN = TextNode("damage done to AVA")
						self.AH_TN.setText("-3")
						self.AH_NT_NP = render.attachNewNode(self.AH_TN)
						self.AH_NT_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
						self.AH_NT_NP.setBillboardAxis()
						self.AH_NT_NP.setZ(3.3)
						self.AH_TN.setAlign(TextNode.ACenter)
						self.AH_TN.setTextColor(0.9, 0, 0, 1.0)
						self.AH_NT_NP.setScale(1.5)
						self.AH_TN.setFont(L.FONT3)
						self.AH_TN_INT = self.AH_NT_NP.posInterval(0.5,
																	Point3(0, 0, 5.8),
																	startPos=(0, 0, 3.3),
																	blendType='easeInOut')
						self.AH_TN_INT.start()
						taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_AVA, "remove AVA damage label")
					if self.lastWeapon == 'CCAKE':
						self.AVATAR_HEALTH -= 1
						try:
							self.AH_NT_NP.remove()
						except:
							pass
						self.AH_TN = TextNode("damage done to AVA")
						self.AH_TN.setText("-1")
						self.AH_NT_NP = render.attachNewNode(self.AH_TN)
						self.AH_NT_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
						self.AH_NT_NP.setBillboardAxis()
						self.AH_NT_NP.setZ(3.3)
						self.AH_TN.setAlign(TextNode.ACenter)
						self.AH_TN.setTextColor(0.9, 0, 0, 1.0)
						self.AH_NT_NP.setScale(1.5)
						self.AH_TN.setFont(L.FONT3)
						self.AH_TN_INT = self.AH_NT_NP.posInterval(0.5,
																	Point3(0, 0, 5.8),
																	startPos=(0, 0, 3.3),
																	blendType='easeInOut')
						self.AH_TN_INT.start()
						taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_AVA, "remove AVA damage label")
					if self.lastWeapon == 'BCAKE':
						self.AVATAR_HEALTH -= 5
						try:
							self.AH_NT_NP.remove()
						except:
							pass
						self.AH_TN = TextNode("damage done to AVA")
						self.AH_TN.setText("-5")
						self.AH_NT_NP = render.attachNewNode(self.AH_TN)
						self.AH_NT_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
						self.AH_NT_NP.setBillboardAxis()
						self.AH_NT_NP.setZ(3.3)
						self.AH_TN.setAlign(TextNode.ACenter)
						self.AH_TN.setTextColor(0.9, 0, 0, 1.0)
						self.AH_NT_NP.setScale(1.5)
						self.AH_TN.setFont(L.FONT3)
						self.AH_TN_INT = self.AH_NT_NP.posInterval(0.5,
																	Point3(0, 0, 5.8),
																	startPos=(0, 0, 3.3),
																	blendType='easeInOut')
						self.AH_TN_INT.start()
						taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_AVA, "remove AVA damage label")
					self.AVATAR_HEALTH_LBL.setText("Your health :" + str(self.AVATAR_HEALTH))
			except:
				pass
			taskMgr.doMethodLater(2.5, self.STOP_JUMP, "stop slipb")
	def COG_START_TIE(self):
		self.AIBEHAVIORS.pauseAi('pathfollow')
		L.COG_1.setH(L.AVATAR_LEGS.getH() - 180)
		L.COG_1.play("throw")
		L.TIE.show()
		L.TIE.setPos(0,0,-0.5)
		L.TIE.reparentTo(L.COG_1.find('**/joint_Rhold'))
		taskMgr.doMethodLater(2.8, self.COG_RELEASE_TIE, "cog releases his tie")
		taskMgr.doMethodLater(4, self.COG_RESUME_WANDER, "cog resumes wander")
	def COG_RELEASE_TIE(self, task):
		self.TIE_NP = NodePath("TIEPATH")
		self.TIE_NP.reparentTo(L.COG_1.find('**/joint_nameTag'))
		self.TIE_NP.setPos(0, 50, 0)

		L.TIE.reparentTo(render)

		self.Ttrajectory = ProjectileInterval(L.TIE,
									startPos = (L.COG_1.getX(), L.COG_1.getY(), L.COG_1.getZ() +3),
									endPos = self.TIE_NP.getPos(render),
									gravityMult = 0.7, duration = 1)
		self.Ttrajectory.start()
	def CHECK_JUMP_DAMAGE(self, task):
		L.JUMP_END_SFX.play()
		if self.AVATAR_MOTION == 'JUMPING':
			return task.done
		if self.AVATAR_MOTION == 'NORMAL' or 'MOVING':
			self.keyMap = {"left":0, "right":0, "forward":0, "backward":0}
			L.RUN_LOOP.stop()
			L.WLK_LOOP.stop()
			base.accept("arrow_left", self.setKey, ["left",0])
			base.accept("arrow_right", self.setKey, ["right",0])
			base.accept("arrow_up", self.setKey, ["forward",0])
			base.accept("arrow_down", self.setKey, ["backward",0])
			base.accept("arrow_left-up", self.setKey, ["left",0])
			base.accept("arrow_right-up", self.setKey, ["right",0])
			base.accept("arrow_up-up", self.setKey, ["forward",0])
			base.accept("arrow_down-up", self.setKey, ["backward",0])
			base.accept("arrow_down-arrow_up", self.setKey, ["backward",0])
			base.accept("arrow_up-arrow_down", self.setKey, ["forward",0])
			base.accept("a", self.setKey, ["left",0])
			base.accept("d", self.setKey, ["right",0])
			base.accept("w", self.setKey, ["forward",0])
			base.accept("s", self.setKey, ["backward",0])
			base.accept("a-up", self.setKey, ["left",0])
			base.accept("d-up", self.setKey, ["right",0])
			base.accept("w-up", self.setKey, ["forward",0])
			base.accept("s-up", self.setKey, ["backward",0])
			base.accept("s-w", self.setKey, ["backward",0])
			base.accept("w-s", self.setKey, ["forward",0])
			base.accept("space", self.nul)
			base.accept("control-up", self.nul)
			base.accept("control", self.nul)
			self.isMoving_forward = False
			self.isMoving_side = False
			L.AVATAR_HEAD.play("slipf")
			L.AVATAR_TORSO.play("slipf")
			L.AVATAR_LEGS.play("slipf")
			try:
				if self.ROUND == 3:
					self.AVATAR_HEALTH -= 5
					try:
						self.AH_NT_NP.remove()
					except:
						pass
					self.AH_TN = TextNode("damage done to AVA")
					self.AH_TN.setText("-5")
					self.AH_NT_NP = render.attachNewNode(self.AH_TN)
					self.AH_NT_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
					self.AH_NT_NP.setBillboardAxis()
					self.AH_NT_NP.setZ(3.3)
					self.AH_TN.setAlign(TextNode.ACenter)
					self.AH_TN.setTextColor(0.9, 0, 0, 1.0)
					self.AH_NT_NP.setScale(1.5)
					self.AH_TN.setFont(L.FONT3)
					self.AH_TN_INT = self.AH_NT_NP.posInterval(0.5,
																Point3(0, 0, 5.8),
																startPos=(0, 0, 3.3),
																blendType='easeInOut')
					self.AH_TN_INT.start()
					taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_AVA, "remove AVA damage label")
					self.AVATAR_HEALTH_LBL.setText("Your health: " + str(self.AVATAR_HEALTH))
			except:
				pass
			taskMgr.doMethodLater(1, self.STOP_JUMP, "stop fall")
			return task.done
		return task.done
	def COG_RESUME_WANDER(self, task):
		try:
			self.AIBEHAVIORS.resumeAi('pathfollow')
		except:
			pass
		L.COG_1.loop("walk")
		return task.done
	def CHECKCOGPATHSTAT(self, task):
		if self.AIBEHAVIORS.behaviorStatus('pathfollow') == 'done':
			if self.ROUND == 2:
				L.COG_1.loop("neutral")
				taskMgr.doMethodLater(1, self.coach_Talk_b4_round3, "coach talks b4 round 3")
				return task.done
			if self.ROUND == 3:
				self.AIBEHAVIORS.startFollow()
		return task.cont
	def CHECKCOGPATHSTAT2(self, task):
		if self.AIBEHAVIORS2.behaviorStatus('pathfollow') == 'done':
			self.AIBEHAVIORS2.startFollow()
		return task.cont
	def coach_Talk_b4_round3(self, task):
		if self.ROUND == 3:
			sys.exit(0)
		L.COG_MUSIC.stop()
		L.R3_BGM.play()
		self.COACH_WHSP5.remove()
		self.COACH_WHSP6.remove()
		self.COACH_WHSP7.remove()
		self.COACH_WHSP7_2.remove()
		self.COACH_WHSP8 = OnscreenText(text="COACH: Now, you and the Cog will be given health. Go battle!",  scale=0.06, pos=(0.0, -0.6, -0.6), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
		taskMgr.doMethodLater(2, self.INITROUND3, "initialize round3")
		return task.done
	def COACH_ANNOUNCE_TOONUP(self, task):
		L.COACH_DIAL.play()
		base.accept('avatarSensorCoach-into', self.COACH_START_TOONUP)
		self.WHSP_100 = OnscreenText(text="COACH: If you need a toonup, come here! This is your only chance!",  scale=0.06, pos=(0.0, -0.58, -0.58), wordwrap=8, align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6))
		taskMgr.doMethodLater(10, self.REMOVE_COACH_ANNOUNCE_TOONUP, "remove coach annount toonup")
		return task.done
	def COACH_START_TOONUP(self, entry):
		base.accept('avatarSensorCoach-into', self.nul_col)
		base.accept("arrow_left", self.setKey, ["left",0])
		base.accept("arrow_right", self.setKey, ["right",0])
		base.accept("arrow_up", self.setKey, ["forward",0])
		base.accept("arrow_down", self.setKey, ["backward",0])
		base.accept("arrow_left-up", self.setKey, ["left",0])
		base.accept("arrow_right-up", self.setKey, ["right",0])
		base.accept("arrow_up-up", self.setKey, ["forward",0])
		base.accept("arrow_down-up", self.setKey, ["backward",0])
		base.accept("arrow_down-arrow_up", self.setKey, ["backward",0])
		base.accept("arrow_up-arrow_down", self.setKey, ["forward",0])
		base.accept("a", self.setKey, ["left",0])
		base.accept("d", self.setKey, ["right",0])
		base.accept("w", self.setKey, ["forward",0])
		base.accept("s", self.setKey, ["backward",0])
		base.accept("a-up", self.setKey, ["left",0])
		base.accept("d-up", self.setKey, ["right",0])
		base.accept("w-up", self.setKey, ["forward",0])
		base.accept("s-up", self.setKey, ["backward",0])
		base.accept("s-w", self.setKey, ["backward",0])
		base.accept("w-s", self.setKey, ["forward",0])
		base.accept("space", self.nul)
		base.accept("control-up", self.nul)
		base.accept("control", self.nul)
		L.FEATHER.reparentTo(L.COACH_TORSO.find('**/def_joint_right_hold'))
		L.AVATAR_LEGS.setY(L.COACH_LEGS.getY() - 7)
		L.COACH_LEGS.lookAt(L.AVATAR_LEGS)
		L.AVATAR_LEGS.lookAt(L.COACH_LEGS)
		L.COACH_LEGS.play("tickle")
		L.COACH_TORSO.play("tickle")
		L.FEATHER.play("chan")
		L.TICKLE_SFX.play()
		taskMgr.doMethodLater(2, self.TOON_GET_TOONUP, "toon gets a toonup")
	def TOON_GET_TOONUP(self, task):
		L.AVATAR_LEGS.play("cringe")
		L.AVATAR_TORSO.play("cringe")
		L.AVATAR_HEAD.play("cringe")
		self.ADDED_HEALTH = self.AVATAR_START_HEALTH - self.AVATAR_HEALTH
		if self.AVATAR_HEALTH <= 20:
			self.AVATAR_HEALTH += 10
			self.ADDED_HEALTH = 10
		if self.AVATAR_HEALTH == 21:
			self.AVATAR_HEALTH += 9
			self.ADDED_HEALTH = 9
		if self.AVATAR_HEALTH == 22:
			self.AVATAR_HEALTH += 8
			self.ADDED_HEALTH = 8
		if self.AVATAR_HEALTH == 23:
			self.AVATAR_HEALTH += 7
			self.ADDED_HEALTH = 7
		if self.AVATAR_HEALTH == 24:
			self.AVATAR_HEALTH += 6
			self.ADDED_HEALTH = 6
		if self.AVATAR_HEALTH == 25:
			self.AVATAR_HEALTH += 5
			self.ADDED_HEALTH = 5
		if self.AVATAR_HEALTH == 26:
			self.AVATAR_HEALTH += 4
			self.ADDED_HEALTH = 4
		if self.AVATAR_HEALTH == 27:
			self.AVATAR_HEALTH += 3
			self.ADDED_HEALTH = 3
		if self.AVATAR_HEALTH == 28:
			self.AVATAR_HEALTH += 2
			self.ADDED_HEALTH = 2
		if self.AVATAR_HEALTH == 29:
			self.AVATAR_HEALTH += 1
			self.ADDED_HEALTH = 1
		if self.AVATAR_HEALTH == 30:
			self.AVATAR_HEALTH += 0
			self.ADDED_HEALTH = 0

		self.AH_TN = TextNode("damage done to AVA")
		self.AH_TN.setText("+" + str(self.ADDED_HEALTH))
		self.AH_NT_NP = render.attachNewNode(self.AH_TN)
		self.AH_NT_NP.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
		self.AH_NT_NP.setBillboardAxis()
		self.AH_NT_NP.setZ(3.3)
		self.AH_TN.setAlign(TextNode.ACenter)
		self.AH_TN.setTextColor(0, 0.9, 0, 1.0)
		self.AH_NT_NP.setScale(1.5)
		self.AH_TN.setFont(L.FONT3)
		self.AH_TN_INT = self.AH_NT_NP.posInterval(0.5,
													Point3(0, 0, 5.8),
													startPos=(0, 0, 3.3),
													blendType='easeInOut')
		self.AH_TN_INT.start()
		self.AVATAR_HEALTH_LBL.setText("Your health: " + str(self.AVATAR_HEALTH))
		taskMgr.doMethodLater(0.9, self.REMOVE_DAMG_LBL_AVA, "remove AVA damage label")
		taskMgr.doMethodLater(2, self.STOP_JUMP, "stop jump?")
		taskMgr.doMethodLater(2, self.HIDE_FEATHER, "hide feather")
		return task.done
	def HIDE_FEATHER(self, task):
		L.FEATHER.hide()
		return task.done
	def REMOVE_COACH_ANNOUNCE_TOONUP(self, task):
		self.WHSP_100.remove()
		return task.done
	def INITROUND3(self, task):
		if self.ROUND == 2:
			self.COG_TN.setText("Mover &\nShaker\nSellbot\nLevel 9")
		taskMgr.add(self.CHECK_COG_LIVES, "check cog lives")
		taskMgr.doMethodLater(45, self.COACH_ANNOUNCE_TOONUP, "coach announces available toonup")
		self.ROUND = 3
		self.TOTALHITS = 0
		taskMgr.add(self.CHECK_TOTAL_PIE_COUNT, "check total pie count")
		print self.ROUND
		self.AVATAR_HEALTH = 30
		self.COG_HEALTH = 300
		self.AVATAR_START_HEALTH = 30
		self.AVATAR_HEALTH_LBL = OnscreenText(text="Your health: " + str(self.AVATAR_HEALTH), scale=0.06, pos=(0.0, 0, 0), align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6), mayChange=True)
		self.COG_HEALTH_LBL = OnscreenText(text="Cog health: " + str(self.COG_HEALTH), scale=0.06, pos=(0.0, 0, 0), align=TextNode.ALeft, bg=(0.8, 0, 0, 0.6), mayChange=True)
		self.COG_HEALTH_LBL.hide()
		taskMgr.doMethodLater(0.5, self.AVA_HEALTH_INT, "ava health int")
		return task.done
	def AVA_HEALTH_INT(self, task):
		self.AVA_HEALTH_LBL_INT = self.AVATAR_HEALTH_LBL.posInterval(1,
																	Point3(-0.9, -0.9, -0.9),
																	startPos=(0,0,0),
																	blendType='easeInOut')
		self.AVA_HEALTH_LBL_INT.start()
		taskMgr.doMethodLater(1.5, self.COG_HEALTH_SHOW, " ")
		return task.done
	def COG_HEALTH_SHOW(self, task):
		self.COG_HEALTH_LBL.show()
		taskMgr.doMethodLater(0.5, self.COG_HEALTH_INT, " ")
		return task.done
	def COG_HEALTH_INT(self, task):
		self.COG_HEALTH_LBL_INT = self.COG_HEALTH_LBL.posInterval(1,
																	Point3(0.8, -0.9, -0.9),
																	startPos=(0,0,0),
																	blendType='easeInOut')
		self.COG_HEALTH_LBL_INT.start()
		taskMgr.doMethodLater(1.5, self.COG_WANDER1, "cog wander 1")
		taskMgr.add(self.CHECK_COG_HEALTH, "check cog health")
		taskMgr.add(self.CHECK_AVA_HEALTH, "check avatar health")
		self.COACH_WHSP8.remove()
		return task.done
	def AICOGUPDATE(self, task):
		self.AIWORLD.update()
		return task.cont

	def checkCollisions(self, entry):
		if entry.getIntoNodePath().getName() == 'CLEGSCNODE':
			L.COACH_DIAL.setVolume(0.7)
			L.COACH_DIAL.play()
			if self.ROUND == 1:
				return
			self.COG_BIO_MENU()
	def COG_BIO_MENU(self):
		self.keyMap = {"left":0, "right":0, "forward":0, "backward":0}
		L.RUN_LOOP.stop()
		L.WLK_LOOP.stop()
		base.accept("arrow_left", self.setKey, ["left",0])
		base.accept("arrow_right", self.setKey, ["right",0])
		base.accept("arrow_up", self.setKey, ["forward",0])
		base.accept("arrow_down", self.setKey, ["backward",0])
		base.accept("arrow_left-up", self.setKey, ["left",0])
		base.accept("arrow_right-up", self.setKey, ["right",0])
		base.accept("arrow_up-up", self.setKey, ["forward",0])
		base.accept("arrow_down-up", self.setKey, ["backward",0])
		base.accept("arrow_down-arrow_up", self.setKey, ["backward",0])
		base.accept("arrow_up-arrow_down", self.setKey, ["forward",0])
		base.accept("a", self.setKey, ["left",0])
		base.accept("d", self.setKey, ["right",0])
		base.accept("w", self.setKey, ["forward",0])
		base.accept("s", self.setKey, ["backward",0])
		base.accept("a-up", self.setKey, ["left",0])
		base.accept("d-up", self.setKey, ["right",0])
		base.accept("w-up", self.setKey, ["forward",0])
		base.accept("s-up", self.setKey, ["backward",0])
		base.accept("s-w", self.setKey, ["backward",0])
		base.accept("w-s", self.setKey, ["forward",0])
		base.accept("space", self.nul)
		base.accept("1", self.nul)
		self.isMoving_forward = False
		self.isMoving_side = False
		L.AVATAR_LEGS.loop("neutral")
		L.AVATAR_TORSO.loop("neutral")
		L.AVATAR_HEAD.loop("neutral")
		self.MENU_BOX = OnscreenImage(image=L.DIALOG_BOX, scale=1)
		self.INFO_BTN = DirectButton(geom=(L.GENBTN.find('**/QuitBtn_UP'),
												L.GENBTN.find('**/QuitBtn_DN'),
												L.GENBTN.find('**/QuitBtn_RLVR')), clickSound=L.FWD, rolloverSound=L.RLVR, relief=None, text="Cog Info", text_scale=0.053, text_pos=(0, -0.015), pos=(0, 0, 0.2), scale=1.5, command=self.INIT_BIO)
	def INIT_BIO(self):
		self.CLOSE_BTN = DirectButton(geom=(L.DB_BTNS.find('**/CloseBtn_UP'),
											L.DB_BTNS.find('**/CloseBtn_DN'),
											L.DB_BTNS.find('**/CloseBtn_Rllvr')), clickSound=L.FWD, rolloverSound=L.RLVR, relief=None, pos=(0, 0, -0.5), scale=0.8, command=self.EXIT_BIO)
		self.MOVERSHAKER_BIO()
	def MOVERSHAKER_BIO(self):
		self.MENU_BOX.setScale(1.9, 1.3, 1.3)
		self.INFO_BTN.remove()
		self.MOVERSHAKER_IMG = OnscreenImage(image="phase_4/maps/cog_movershaker.tif", scale=0.5)
		self.MOVERSHAKER_IMG.setTransparency(True)
		self.MOVERSHAKER_IMG.setX(-0.5)
		self.MOVERSHAKER_IMG.setZ(-0.1)
		self.MOVERSHAKER_LBL = OnscreenText(text="Mover & Shaker", scale=0.08, pos=(0, 0.5, 0))
		self.MS_MAXDAMG_LBL = OnscreenText(text="Max Damage: 5", scale=0.065, pos=(0.4, 0.3, 0))
		self.MS_HEALTH_LBL = OnscreenText(text="Health: 300", scale=0.065, pos=(0.4, 0.2, 0))
		self.MS_PRIMATT_LBL = OnscreenText(text="Primary Attack: Clip-On-Tie", scale=0.065, pos=(0.4, 0.1, 0))
		self.MS_SECATT_LBL = OnscreenText(text="Secondary Attack: Quake", scale=0.065, pos=(0.4, 0, 0))
		self.MS_ATTRATE_LBL = OnscreenText(text="Attack Rate: Rare-Medium", scale=0.065, pos=(0.4, -0.1, 0))
		self.MS_SPEED_LBL = OnscreenText(text="Speed: Medium-Fast", scale=0.065, pos=(0.4, -0.2, 0))
		self.MS_SIZE_LBL = OnscreenText(text="Size: Thin, Small", scale=0.065, pos=(0.45, -0.3, 0))

		self.NEXT_BTN = DirectButton(geom=(L.ARROWS.find('**/CrtATn_R_Arrow_UP'),
											L.ARROWS.find('**/CrtATn_R_Arrow_DN'),
											L.ARROWS.find('**/CrtATn_R_Arrow_RLVR')), clickSound=L.FWD, rolloverSound=L.RLVR, relief=None, pos=(0.1, 0, -0.5), scale=0.3, command=self.GOTO_BOSSBIO)
	def GOTO_BOSSBIO(self):
		self.MOVERSHAKER_LBL.remove()
		self.MOVERSHAKER_IMG.remove()
		self.MS_MAXDAMG_LBL.remove()
		self.MS_HEALTH_LBL.remove()
		self.MS_PRIMATT_LBL.remove()
		self.MS_SECATT_LBL.remove()
		self.MS_ATTRATE_LBL.remove()
		self.MS_SPEED_LBL.remove()
		self.MS_SIZE_LBL.remove()
		self.NEXT_BTN.remove()
		self.BOSS_BIO()
	def GOTO_MSBIO(self):
		self.BOSS_LBL.remove()
		self.BOSS_IMG.remove()
		self.B_MAXDAMG_LBL.remove()
		self.B_HEALTH_LBL.remove()
		self.B_PRIMATT_LBL.remove()
		self.B_SECATT_LBL.remove()
		self.B_ATTRATE_LBL.remove()
		self.B_SPEED_LBL.remove()
		self.B_SIZE_LBL.remove()
		self.PREV_BTN.remove()
		self.MOVERSHAKER_BIO()
	def BOSS_BIO(self):
		self.MENU_BOX.setScale(1.9, 1.3, 1.3)
		self.BOSS_IMG = OnscreenImage(image="phase_4/maps/cog_boss.tif", scale=0.5)
		self.BOSS_IMG.setTransparency(True)
		self.BOSS_IMG.setX(-0.45)
		self.BOSS_IMG.setZ(-0.1)
		self.BOSS_LBL = OnscreenText(text="CogBoss", scale=0.08, pos=(0, 0.5, 0))
		self.B_MAXDAMG_LBL = OnscreenText(text="Max Damage: 10", scale=0.065, pos=(0.45, 0.3, 0))
		self.B_HEALTH_LBL = OnscreenText(text="Health: 550", scale=0.065, pos=(0.45, 0.2, 0))
		self.B_PRIMATT_LBL = OnscreenText(text="Primary Attack: Glower Power", scale=0.065, pos=(0.45, 0.1, 0))
		self.B_SECATT_LBL = OnscreenText(text="Secondary Attack: Force Field", scale=0.065, pos=(0.45, 0, 0))
		self.B_ATTRATE_LBL = OnscreenText(text="Attack Rate: Frequent", scale=0.065, pos=(0.45, -0.1, 0))
		self.B_SPEED_LBL = OnscreenText(text="Speed: Slow-Medium", scale=0.065, pos=(0.45, -0.2, 0))
		self.B_SIZE_LBL = OnscreenText(text="Size: Fat, Very Large", scale=0.065, pos=(0.45, -0.3, 0))
		self.PREV_BTN = DirectButton(geom=(L.ARROWS.find('**/CrtATn_R_Arrow_UP'),
											L.ARROWS.find('**/CrtATn_R_Arrow_DN'),
											L.ARROWS.find('**/CrtATn_R_Arrow_RLVR')), clickSound=L.FWD, rolloverSound=L.RLVR, relief=None, hpr=(180, 0, 0), pos=(-0.1, 0, -0.5), scale=0.3, command=self.GOTO_MSBIO)
	def EXIT_BIO(self):
		try:
			self.BOSS_LBL.remove()
			self.BOSS_IMG.remove()
			self.B_MAXDAMG_LBL.remove()
			self.B_HEALTH_LBL.remove()
			self.B_PRIMATT_LBL.remove()
			self.B_SECATT_LBL.remove()
			self.B_ATTRATE_LBL.remove()
			self.B_SPEED_LBL.remove()
			self.B_SIZE_LBL.remove()
			self.PREV_BTN.remove()
		except:
			pass

		try:
			self.MOVERSHAKER_LBL.remove()
			self.MOVERSHAKER_IMG.remove()
			self.MS_MAXDAMG_LBL.remove()
			self.MS_HEALTH_LBL.remove()
			self.MS_PRIMATT_LBL.remove()
			self.MS_SECATT_LBL.remove()
			self.MS_ATTRATE_LBL.remove()
			self.MS_SPEED_LBL.remove()
			self.MS_SIZE_LBL.remove()
			self.NEXT_BTN.remove()
		except:
			pass
		self.CLOSE_BTN.remove()
		self.MENU_BOX.remove()
		base.accept("arrow_left", self.setKey, ["left",1])
		base.accept("arrow_right", self.setKey, ["right",1])
		base.accept("arrow_up", self.setKey, ["forward",1])
		base.accept("arrow_down", self.setKey, ["backward",1])
		base.accept("arrow_left-up", self.setKey, ["left",0])
		base.accept("arrow_right-up", self.setKey, ["right",0])
		base.accept("arrow_up-up", self.setKey, ["forward",0])
		base.accept("arrow_down-up", self.setKey, ["backward",0])
		base.accept("arrow_down-arrow_up", self.setKey, ["backward",1])
		base.accept("arrow_up-arrow_down", self.setKey, ["forward",1])
		base.accept("a", self.setKey, ["left",1])
		base.accept("d", self.setKey, ["right",1])
		base.accept("w", self.setKey, ["forward",1])
		base.accept("s", self.setKey, ["backward",1])
		base.accept("a-up", self.setKey, ["left",0])
		base.accept("d-up", self.setKey, ["right",0])
		base.accept("w-up", self.setKey, ["forward",0])
		base.accept("s-up", self.setKey, ["backward",0])
		base.accept("s-w", self.setKey, ["backward",1])
		base.accept("w-s", self.setKey, ["forward",1])
		base.accept("space", self.JUMP)
		base.accept('avatarSensor-into', self.checkCollisions)
		base.accept('1', self.COG_SPAWN1)

	def setKey(self, key, value):
		self.keyMap[key] = value
	def move(self, task):
		try:
			if (self.keyMap["left"]!=0):
				L.AVATAR_LEGS.setH(L.AVATAR_LEGS.getH() + 75 * globalClock.getDt())
			if (self.keyMap["right"]!=0):
				L.AVATAR_LEGS.setH(L.AVATAR_LEGS.getH() - 75 * globalClock.getDt())
			if (self.keyMap["forward"]!=0):
				L.AVATAR_LEGS.setY(L.AVATAR_LEGS, 25 * globalClock.getDt())
			if (self.keyMap["backward"]!=0):
				L.AVATAR_LEGS.setY(L.AVATAR_LEGS, -12.5 * globalClock.getDt())
		except:
			pass

		if (self.keyMap["forward"]!=0):
			if self.isMoving_forward is False:
				self.isMoving_side = False
				self.AVATAR_MOTION = 'MOVING'
				L.WLK_LOOP.stop()
				L.RUN_LOOP.play()
				L.AVATAR_HEAD.loop("run")
				L.AVATAR_TORSO.loop("run")
				L.AVATAR_LEGS.loop("run")
				self.isMoving_forward = True
		elif (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0) or (self.keyMap["backward"]!=0):
			if self.isMoving_side is False:
				self.isMoving_forward = False
				self.AVATAR_MOTION = 'MOVING'
				L.WLK_LOOP.play()
				L.RUN_LOOP.stop()
				L.AVATAR_HEAD.loop("walk")
				L.AVATAR_TORSO.loop("walk")
				L.AVATAR_LEGS.loop("walk")
				self.isMoving_side = True
		else:
			if self.isMoving_forward or self.isMoving_side:
				self.AVATAR_MOTION = 'NORMAL'
				L.WLK_LOOP.stop()
				L.RUN_LOOP.stop()
				L.AVATAR_HEAD.loop("neutral")
				L.AVATAR_TORSO.loop("neutral")
				L.AVATAR_LEGS.loop("neutral")
				self.isMoving_side = False
				self.isMoving_forward = False
		return task.cont
class CAMERA:
	def __init__(self):
		camera.reparentTo(L.AVATAR_LEGS.find('**/joint_nameTag'))
		camera.setPos(0, -15.5, 3.89)
		#self.POS_BTN = DirectButton(text="Get Pos.", command=self.givePos, scale=0.08, pos=(1.0, 0, 0))
		#self.HPR_BTN = DirectButton(text="Get Hpr.", command=self.giveHpr, scale=0.08, pos=(-1.0, 0, 0))
	def givePos(self):
		print "Pos:"
		print camera.getPos()
	def giveHpr(self):
		print "Hpr:"
		print camera.getHpr()

L = LOAD()
L.loadGame()
S = SCENE()
S.initScene()
C = CAMERA()
run()
