#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Saturn"
iconName = "Saturn"
longName = "U.S.S. Gateway"
shipFile = "Saturn"
species = App.SPECIES_GALAXY
menuGroup = "Future Ships"
playerMenuGroup = "Future Ships"
Foundation.ShipDef.Saturn = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.Saturn.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Ablative Armour': 475000,
	'ChronitonTorpe Immune': 1,
	"Phased Torpedo Immune": 1,
	'Regenerative Shields': 80
}
Foundation.ShipDef.Saturn.CloakingSFX   = "FutureBattleCloak"
Foundation.ShipDef.Saturn.DeCloakingSFX = "FutureBattleDecloak"


Foundation.ShipDef.Saturn.desc = "The Saturn class was a type of Federation starship operated by Starfleet during the 32nd century (The U.S.S. Gateway being fitted with 32nd century refit arrays and reflux quantum torpedo launchers). In 3189, the fleet at Federation Headquarters included a ship of this class. The collective energy of this fleet sustained a distortion field that concealed the headquarters' location. In 3190, ships of this class were present at the re-opening of Starfleet Academy and the unveiling of the Archer Spacedock."


if menuGroup:           Foundation.ShipDef.Saturn.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Saturn.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
