

import typing

from .choice import Choice
from .trait_trait_specific_breath_weapon import TraitTraitSpecificBreathWeapon

TraitTraitSpecific = typing.Union[Choice, TraitTraitSpecificBreathWeapon]
