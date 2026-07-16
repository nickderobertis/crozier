

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Range(UniversalBaseModel):
    """
    The range of a number value between the specified lower and upper bounds.
    """

    max: typing.Optional[str] = pydantic.Field(default=None)
    """
    The upper bound of the number range.
    """

    min: typing.Optional[str] = pydantic.Field(default=None)
    """
    The lower bound of the number range.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
