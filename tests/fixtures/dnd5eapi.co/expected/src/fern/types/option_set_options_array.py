

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class OptionSetOptionsArray(UniversalBaseModel):
    option_set_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of option set; determines other attributes.
    """

    options_array: typing.Optional[typing.List["Option"]] = pydantic.Field(default=None)
    """
    Array of options to choose from.
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

update_forward_refs(
    OptionSetOptionsArray,
    Choice=Choice,
    Option=Option,
    OptionChoice=OptionChoice,
    OptionItems=OptionItems,
    OptionSet=OptionSet,
)
