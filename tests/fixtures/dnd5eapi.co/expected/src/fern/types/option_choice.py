

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class OptionChoice(UniversalBaseModel):
    choice: typing.Optional["Choice"] = None
    option_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of option; determines other attributes.
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
from .option_items import OptionItems
from .option_set import OptionSet
from .option_set_options_array import OptionSetOptionsArray

update_forward_refs(
    OptionChoice,
    Choice=Choice,
    Option=Option,
    OptionItems=OptionItems,
    OptionSet=OptionSet,
    OptionSetOptionsArray=OptionSetOptionsArray,
)
