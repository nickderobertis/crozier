

import typing

from .armor import Armor
from .equipment_pack import EquipmentPack
from .gear import Gear
from .weapon import Weapon

Equipment = typing.Union[Weapon, Armor, Gear, EquipmentPack]
