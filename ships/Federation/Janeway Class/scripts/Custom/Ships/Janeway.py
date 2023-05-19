#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Janeway"
iconName = "Janeway"
longName = "U.S.S. Voyager J"
shipFile = "Janeway"
species = App.SPECIES_GALAXY
menuGroup = "Future Ships"
playerMenuGroup = "Future Ships"
Foundation.ShipDef.Janeway = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Janeway.desc = "The 10th generation of Voyager, from the 32nd Century, Janeway Class"


if menuGroup:           Foundation.ShipDef.Janeway.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Janeway.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.Janeway.dTechs = { 'Breen Drainer Immune': 1,'Drainer Immune': 1,'Ablative Armour': 405000, 'ChronitonTorpe Immune': 1, 'Regenerative Shields': 75}
Foundation.ShipDef.Janeway.CloakingSFX   = "FutureBattleCloak"
Foundation.ShipDef.Janeway.DeCloakingSFX = "FutureBattleDecloak"


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
      