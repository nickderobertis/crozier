

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .api_reference import ApiReference
from .prerequisite import Prerequisite


class Multiclassing(UniversalBaseModel):
    """
    `Multiclassing`
    """

    prerequisite_options: typing.Optional[typing.List["Choice"]] = pydantic.Field(default=None)
    """
    List of choices of prerequisites to meet for.
    """

    prerequisites: typing.Optional[typing.List[Prerequisite]] = pydantic.Field(default=None)
    """
    List of prerequisites that must be met.
    """

    proficiencies: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of proficiencies available when multiclassing.
    """

    proficiency_choices: typing.Optional[typing.List["Choice"]] = pydantic.Field(default=None)
    """
    List of choices of proficiencies that are given when multiclassing.
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
    Multiclassing,
    Choice=Choice,
    Option=Option,
    OptionChoice=OptionChoice,
    OptionItems=OptionItems,
    OptionSet=OptionSet,
    OptionSetOptionsArray=OptionSetOptionsArray,
)
