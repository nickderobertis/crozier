

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .ability_bonus import AbilityBonus
from .api_reference import ApiReference


class Race(ApiReference):
    """
    `Race`
    """

    ability_bonuses: typing.Optional[typing.List[AbilityBonus]] = pydantic.Field(default=None)
    """
    Racial bonuses to ability scores.
    """

    age: typing.Optional[str] = pydantic.Field(default=None)
    """
    Flavor description of possible ages for this race.
    """

    alignment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Flavor description of likely alignments this race takes.
    """

    language_desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Flavor description of the languages this race knows.
    """

    languages: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Starting languages for all new characters of this race.
    """

    size: typing.Optional[str] = pydantic.Field(default=None)
    """
    Size class of this race.
    """

    size_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Flavor description of height and weight for this race.
    """

    speed: typing.Optional[float] = pydantic.Field(default=None)
    """
    Base move speed for this race (in feet per round).
    """

    starting_proficiencies: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Starting proficiencies for all new characters of this race.
    """

    starting_proficiency_options: typing.Optional["Choice"] = pydantic.Field(default=None)
    """
    Starting proficiency options for all new characters of this race.
    """

    subraces: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    All possible subraces that this race includes.
    """

    traits: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Racial traits that provide benefits to its members.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .choice import Choice
from .option import Option
from .option_choice import OptionChoice
from .option_items import OptionItems
from .option_set import OptionSet
from .option_set_options_array import OptionSetOptionsArray

update_forward_refs(
    Race,
    Choice=Choice,
    Option=Option,
    OptionChoice=OptionChoice,
    OptionItems=OptionItems,
    OptionSet=OptionSet,
    OptionSetOptionsArray=OptionSetOptionsArray,
)
