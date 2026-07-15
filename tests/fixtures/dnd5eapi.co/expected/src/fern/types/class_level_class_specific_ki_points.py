

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .class_level_class_specific_ki_points_martial_arts import ClassLevelClassSpecificKiPointsMartialArts


class ClassLevelClassSpecificKiPoints(UniversalBaseModel):
    """
    Monk Class Specific Features
    """

    ki_points: typing.Optional[float] = None
    martial_arts: typing.Optional[ClassLevelClassSpecificKiPointsMartialArts] = None
    unarmored_movement: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
