

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OptionString(UniversalBaseModel):
    option_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of option; determines other attributes.
    """

    string: typing.Optional[str] = pydantic.Field(default=None)
    """
    The string.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
