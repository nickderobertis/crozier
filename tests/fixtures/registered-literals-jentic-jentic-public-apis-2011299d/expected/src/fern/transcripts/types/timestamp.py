

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Timestamp(UniversalBaseModel):
    """
    Timestamp containing a start and end property in milliseconds
    """

    start: int = pydantic.Field()
    """
    The start time in milliseconds
    """

    end: int = pydantic.Field()
    """
    The end time in milliseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
