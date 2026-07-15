

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .ability_bonus import AbilityBonus
from .api_reference import ApiReference


class Subrace(ApiReference):
    """
    `Subrace`
    """

    ability_bonuses: typing.Optional[typing.List[AbilityBonus]] = pydantic.Field(default=None)
    """
    Additional ability bonuses for the subrace.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the subrace.
    """

    language_options: typing.Optional["Choice"] = pydantic.Field(default=None)
    """
    Starting languages to choose from for the subrace.
    """

    languages: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Starting languages for all new characters of the subrace.
    """

    race: typing.Optional[ApiReference] = pydantic.Field(default=None)
    """
    Parent race for the subrace.
    """

    racial_traits: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of traits that for the subrace.
    """

    starting_proficiencies: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    Starting proficiencies for all new characters of the subrace.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .choice import Choice

update_forward_refs(Subrace)
