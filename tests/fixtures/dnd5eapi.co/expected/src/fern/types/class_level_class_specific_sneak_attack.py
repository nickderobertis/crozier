

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .class_level_class_specific_sneak_attack_sneak_attack import ClassLevelClassSpecificSneakAttackSneakAttack


class ClassLevelClassSpecificSneakAttack(UniversalBaseModel):
    """
    Bard Rogue Specific Features
    """

    sneak_attack: typing.Optional[ClassLevelClassSpecificSneakAttackSneakAttack] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
