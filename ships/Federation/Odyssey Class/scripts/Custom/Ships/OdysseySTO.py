#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "OdysseySTO"
iconName = "OdysseySTO"
longName = "USS Enterprise F"
shipFile = "OdysseySTO"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.OdysseySTO = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.OdysseySTO.dTechs = {
   'Breen Drainer Immune': 1,
   'Multivectral Shields': 3,
   "Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}}


Foundation.ShipDef.OdysseySTO.desc = "Odyssey Class Starship badged as NCC - 1701 - F, a late 24th century to early 25th century Federation Flagship."


if menuGroup:           Foundation.ShipDef.OdysseySTO.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.OdysseySTO.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
