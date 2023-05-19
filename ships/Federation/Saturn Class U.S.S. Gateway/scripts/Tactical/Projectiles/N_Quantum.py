#script modified by D&G Productions

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(175.0 / 255.0, 225.0 / 255.0, 255.0 / 255.0, 10.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(92.0 / 255.0, 181.0 / 255.0, 253.0 / 255.0, 10.000000)	


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/PhaserLights.tga",
					kCoreColor, 
					0.55,
					6.0,	 
					"data/Textures/Tactical/Quantum03Glow.tga", 
					kGlowColor,
					3.0,	
					2.2,	 
					2.35,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					35,		
					0.275,		
					1.85)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.35)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.RAPIDQUANTUM)

	return(0)

def GetLaunchSpeed():
	return(200.0)

def GetLaunchSound():
	return("32ndCenQuantum")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Type Z Quantum")

def GetDamage():
	return 4800.0

def GetGuidanceLifetime():
	return 45.0

def GetMaxAngularAccel():
	return 1.5