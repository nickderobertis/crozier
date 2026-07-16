

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference
from .subclass_level_spellcasting import SubclassLevelSpellcasting


class SubclassLevel(UniversalBaseModel):
    """
    `SubclassLevel`
    """

    ability_score_bonuses: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total number of ability score bonuses gained, added from previous levels.
    """

    classspecific: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Class specific information such as dice values for bard songs and number of warlock invocations.
    """

    features: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of features gained at this level.
    """

    index: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource index for shorthand searching.
    """

    level: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number value for the current level object.
    """

    prof_bonus: typing.Optional[float] = pydantic.Field(default=None)
    """
    Proficiency bonus for this class at the specified level.
    """

    spellcasting: typing.Optional[SubclassLevelSpellcasting] = pydantic.Field(default=None)
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
