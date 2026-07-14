

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClassLevelClassSpecificBrutalCriticalDice(UniversalBaseModel):
    """
    Barbarian Class Specific Features
    """

    brutal_critical_dice: typing.Optional[float] = None
    rage_count: typing.Optional[float] = None
    rage_damage_bonus: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
