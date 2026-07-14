

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference
from .class_level_class_specific import ClassLevelClassSpecific
from .class_level_spellcasting import ClassLevelSpellcasting


class ClassLevel(UniversalBaseModel):
    """
    `ClassLevel`
    """

    ability_score_bonuses: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total number of ability score bonuses gained, added from previous levels.
    """

    class_specific: typing.Optional[ClassLevelClassSpecific] = pydantic.Field(default=None)
    """
    Class specific information such as dice values for bard songs and number of warlock invocations.
    """

    features: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Features automatically gained at this level.
    """

    index: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource index for shorthand searching.
    """

    level: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number value for the current level object.
    """

    prof_bonus: typing.Optional[float] = pydantic.Field(default=None)
    """
    Proficiency bonus for this class at the specified level.
    """

    spellcasting: typing.Optional[ClassLevelSpellcasting] = pydantic.Field(default=None)
    """
    Summary of spells known at this level.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the referenced resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
