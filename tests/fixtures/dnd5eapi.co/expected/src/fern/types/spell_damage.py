

import typing

from .damage_at_character_level import DamageAtCharacterLevel
from .damage_at_slot_level import DamageAtSlotLevel

SpellDamage = typing.Union[DamageAtCharacterLevel, DamageAtSlotLevel]
