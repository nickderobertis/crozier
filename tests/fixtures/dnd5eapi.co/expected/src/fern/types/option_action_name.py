

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .option_action_name_type import OptionActionNameType


class OptionActionName(UniversalBaseModel):
    action_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the action.
    """

    count: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of times this action can be repeated if chosen.
    """

    option_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of option; determines other attributes.
    """

    type: typing.Optional[OptionActionNameType] = pydantic.Field(default=None)
    """
    For attack options that can be melee, ranged, abilities, or thrown.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
