import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('injured_kwi')
	mobileTemplate.setLevel(60)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Herbivore Meat")
	mobileTemplate.setMeatAmount(100)
	mobileTemplate.setHideType("Leathery Hide")
	mobileTemplate.setHideAmount(85)
	mobileTemplate.setBoneType("Animal Bones")
	mobileTemplate.setBoneAmount(75)
	mobileTemplate.setSocialGroup("kwi")
	mobileTemplate.setAssistRange(12)
	mobileTemplate.setStalker(False)
	mobileTemplate.setOptionsBitmask(Options.AGGRESSIVE | Options.ATTACKABLE)
	
	templates = Vector()
	templates.add('object/mobile/shared_kwi.iff')
	mobileTemplate.setTemplates(templates)
	
	
	attacks = Vector()
	attacks.add('bm_bite_4')
	attacks.add('bm_hamstring_4')
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('injured_kwi', mobileTemplate)